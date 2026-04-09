#!/bin/bash

# ==========================================
# CONFIGURATION
# ==========================================
CODE_DIR="code"
DIRECTORY_EXPECTED_OUTPUT="expected_output"

# ANSI Color Codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BLUE='\033[0;34m'
BOLD='\033[1m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

# Counters for Summary
TOTAL_FILES=0
TOTAL_CASES=0
CASES_PASSED=0
CASES_FAILED=0
SKIP_COUNT=0
LINT_FAIL_COUNT=0
TYPE_FAIL_COUNT=0

# Determine Diff Command
if command -v git &> /dev/null; then
    DIFF_CMD="git diff --no-index --color=always"
else
    DIFF_CMD="diff -u"
fi

# Check for tools
FLAKE8_EXISTS=false
if command -v flake8 &> /dev/null; then
    FLAKE8_EXISTS=true
fi
MYPY_EXISTS=false
if command -v mypy &> /dev/null; then
    MYPY_EXISTS=true
fi

# ==========================================
# SETUP
# ==========================================
if [ ! -d "$CODE_DIR" ]; then
    echo -e "${RED}Error: Directory '$CODE_DIR' not found.${NC}"
    exit 1
fi

if [ ! -d "$DIRECTORY_EXPECTED_OUTPUT" ]; then
    echo -e "${RED}Error: Directory '$DIRECTORY_EXPECTED_OUTPUT' not found.${NC}"
    exit 1
fi

echo "========================================"
echo -e "${CYAN}Starting Automated Test Runner${NC}"
echo "Using Diff Tool: $(echo $DIFF_CMD | cut -d' ' -f1)"
if [ "$FLAKE8_EXISTS" = true ]; then
    echo "Linting Tool: flake8"
else
    echo -e "${YELLOW}Warning: flake8 not found. Skipping lint checks.${NC}"
fi
echo "========================================"

# ==========================================
# HELPER FUNCTION: RUN SINGLE TEST CASE
# ==========================================
run_single_case() {
    local py_file="$1"
    local args="$2"
    local expected_block="$3"
    local case_id="$4"
    local input_file="$5"
    
    local temp_output="temp_actual_output.txt"
    local temp_expected="temp_expected_output.txt"

    # Write expected block to a temp file for comparison
    echo -n "$expected_block" > "$temp_expected"

    # Construct the command safely using eval
    # We use eval to properly handle quoted arguments like "Data Quest"
    local run_cmd="python3 \"$py_file\" $args"

    # Execute
    if [ -f "$input_file" ]; then
        eval "$run_cmd" < "$input_file" > "$temp_output" 2>&1
    else
        eval "$run_cmd" > "$temp_output" 2>&1
    fi

    # Compare
    if cmp -s "$temp_output" "$temp_expected"; then
        echo -e "  ${GREEN}[PASS]${NC} Case $case_id"
        ((CASES_PASSED++))
    else
        echo -e "  ${RED}[FAIL]${NC} Case $case_id"
        echo -e "  ${YELLOW}Arguments:${NC} $args"
        
        # Show compact diff
        if [[ "$DIFF_CMD" == *"git"* ]]; then
            $DIFF_CMD "$temp_expected" "$temp_output" | cat
        else
            $DIFF_CMD "$temp_expected" "$temp_output" | sed \
                -e "s/^\-\-.*/${CYAN}\0${NC}/" \
                -e "s/^++.*/${CYAN}\0${NC}/" \
                -e "s/^@@.*/${CYAN}\0${NC}/" \
                -e "s/^-/${RED}-/${NC}/" \
                -e "s/^+/${GREEN}+/${NC}/"
        fi
        echo "  --------------------------------------"
        ((CASES_FAILED++))
    fi

    # Cleanup temp files
    rm -f "$temp_output" "$temp_expected"
}

# ==========================================
# MAIN LOOP
# ==========================================
for dir in "$CODE_DIR"/*/ ; do
    if [ -d "$dir" ]; then
        ((TOTAL_FILES++))
        
        name_of_exercise=$(basename "$dir")
        
        # Find the single Python file
        py_file=$(find "$dir" -maxdepth 1 -type f -name "*.py" | head -n 1)

        if [ -z "$py_file" ]; then
            echo -e "${YELLOW}[SKIP]${NC} No Python file found in: $name_of_exercise"
            ((SKIP_COUNT++))
            continue
        fi

        echo -e "\n${BOLD}========================================${NC}"
        echo -e "Processing: ${CYAN}$name_of_exercise${NC} ($(basename "$py_file"))"
        echo -e "${BOLD}========================================${NC}"

        # ------------------------------------------
        # 1. STATIC CHECKS (Run once per file)
        # ------------------------------------------
        if [ "$FLAKE8_EXISTS" = true ]; then
            LINT_OUTPUT=$(flake8 "$py_file" 2>&1)
            if [ -z "$LINT_OUTPUT" ]; then
                echo -e "${GREEN}[LINT OK]${NC}"
            else
                echo -e "${YELLOW}[LINT WARN]${NC} Style issues detected:"
                echo "$LINT_OUTPUT"
                ((LINT_FAIL_COUNT++))
            fi
        fi
        
        if [ "$MYPY_EXISTS" = true ]; then
            TYPE_OUTPUT=$(mypy "$py_file" --ignore-missing-imports --follow-imports=silent 2>&1 | grep "error:")
            if [ -z "$TYPE_OUTPUT" ]; then
                echo -e "${GREEN}[TYPE OK]${NC}"
            else
                echo -e "${RED}[TYPE FAIL]${NC} Type inconsistencies detected:"
                echo "$TYPE_OUTPUT"
                ((TYPE_FAIL_COUNT++))
            fi
        fi

        # ------------------------------------------
        # 2. DYNAMIC TESTING
        # ------------------------------------------
        file_expected="$DIRECTORY_EXPECTED_OUTPUT/${name_of_exercise}_eo.txt"
        input_file="${dir}input.txt"

        if [ ! -f "$file_expected" ]; then
            echo -e "${YELLOW}[MISSING]${NC} Expected output file not found: $file_expected"
            ((SKIP_COUNT++))
            continue
        fi

        # CHECK FOR MULTI-CASE MODE ($> syntax)
        if grep -q '^\$>' "$file_expected"; then
            echo -e "${MAGENTA}Mode: Multi-Case Detected${NC}"
            
            # Parsing variables
            local_args=""
            local_expected_block=""
            case_count=0
            
            # Read file line by line
            while IFS= read -r line || [ -n "$line" ]; do
                if [[ "$line" == \$\>* ]]; then
                    # If we have a previous block accumulated, run it
                    if [ $case_count -gt 0 ]; then
                        run_single_case "$py_file" "$local_args" "$local_expected_block" "$case_count" "$input_file"
                    fi
                    
                    # Start new case
                    ((case_count++))
                    ((TOTAL_CASES++))
                    
                    # Parse Arguments
                    # Remove "$> python3 script.py "
                    # Strategy: Remove prefix "$> ", then remove the python3 command and the script name
                    
                    # 1. Strip "$> "
                    stripped="${line#\$> }"
                    
                    # 2. Strip python3 (or python)
                    stripped="${stripped#python3 }"
                    stripped="${stripped#python }"
                    
                    # 3. Strip the script filename (first word remaining)
                    # We assume the script name in the txt file matches the actual file logic
                    local_args="${stripped#* }"
                    
                    # Reset expected block
                    local_expected_block=""
                else
                    # Accumulate output lines
                    if [ $case_count -gt 0 ]; then
                        local_expected_block="${local_expected_block}${line}"$'\n'
                    fi
                fi
            done < "$file_expected"

            # Run the last accumulated case
            if [ $case_count -gt 0 ]; then
                run_single_case "$py_file" "$local_args" "$local_expected_block" "$case_count" "$input_file"
            fi

        else
            # LEGACY MODE (Single run)
            ((TOTAL_CASES++))
            echo -e "${MAGENTA}Mode: Standard${NC}"
            
            output_file="${dir}output.txt"
            
            # Run Python
            if [ -f "$input_file" ]; then
                python3 "$py_file" < "$input_file" > "$output_file" 2>&1
            else
                python3 "$py_file" > "$output_file" 2>&1
            fi

            # Compare
            if cmp -s "$output_file" "$file_expected"; then
                echo -e "${GREEN}[SUCCESS]${NC} Output matches expected result."
                ((CASES_PASSED++))
            else
                echo -e "${RED}[FAILED]${NC} Differences detected:"
                if [[ "$DIFF_CMD" == *"git"* ]]; then
                    $DIFF_CMD "$file_expected" "$output_file" | cat
                else
                    $DIFF_CMD "$file_expected" "$output_file" | sed \
                        -e "s/^\-\-.*/${CYAN}\0${NC}/" \
                        -e "s/^++.*/${CYAN}\0${NC}/" \
                        -e "s/^@@.*/${CYAN}\0${NC}/" \
                        -e "s/^-/${RED}-/${NC}/" \
                        -e "s/^+/${GREEN}+/${NC}/"
                fi
                ((CASES_FAILED++))
            fi
            
            # Cleanup
            rm -f "$output_file"
        fi
    fi
done

# ==========================================
# FINAL SUMMARY
# ==========================================
echo -e "\n\n${BOLD}========================================${NC}"
echo -e "${BOLD}              FINAL SUMMARY            ${NC}"
echo -e "${BOLD}========================================${NC}"
echo -e "Files Processed:   ${BOLD}${TOTAL_FILES}${NC}"
echo -e "Total Test Cases:  ${BOLD}${TOTAL_CASES}${NC}"
echo -e "Cases Passed:      ${GREEN}${CASES_PASSED}${NC}"
echo -e "Cases Failed:      ${RED}${CASES_FAILED}${NC}"
echo -e "Files Skipped:     ${YELLOW}${SKIP_COUNT}${NC}"

if [ "$FLAKE8_EXISTS" = true ]; then
    if [ "$LINT_FAIL_COUNT" -gt 0 ]; then
        echo -e "Lint Issues:       ${YELLOW}${LINT_FAIL_COUNT}${NC} (files with style errors)"
    else
        echo -e "Lint Issues:       ${GREEN}0 (All clean!)${NC}"
    fi
fi

if [ "$MYPY_EXISTS" = true ]; then
    if [ "$TYPE_FAIL_COUNT" -gt 0 ]; then
        echo -e "Type Issues:       ${RED}${TYPE_FAIL_COUNT}${NC} (files with type errors)"
    else
        echo -e "Type Issues:       ${GREEN}0 (All types sound!)${NC}"
    fi
fi

echo -e "${BOLD}========================================${NC}"

# Final status logic
if [ "$CASES_FAILED" -gt 0 ] || [ "$TYPE_FAIL_COUNT" -gt 0 ]; then
    echo -e "${RED}Status: TESTS FAILED${NC}"
    exit 1
elif [ "$LINT_FAIL_COUNT" -gt 0 ]; then
    echo -e "${YELLOW}Status: TESTS PASSED but LINTING ISSUES DETECTED${NC}"
    exit 0
else
    echo -e "${GREEN}Status: ALL TESTS PASSED & CODE CLEAN${NC}"
    exit 0
fi