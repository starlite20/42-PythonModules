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
NC='\033[0m' # No Color

# Counters for Summary
TOTAL_COUNT=0
PASS_COUNT=0
FAIL_COUNT=0
SKIP_COUNT=0
LINT_FAIL_COUNT=0

# Determine Diff Command
if command -v git &> /dev/null; then
    DIFF_CMD="git diff --no-index --color=always"
else
    DIFF_CMD="diff -u"
fi

# Check for flake8
FLAKE8_EXISTS=false
if command -v flake8 &> /dev/null; then
    FLAKE8_EXISTS=true
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
# MAIN LOOP
# ==========================================
for dir in "$CODE_DIR"/*/ ; do
    if [ -d "$dir" ]; then
        ((TOTAL_COUNT++))
        
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
        # 1. LINTING CHECK (flake8)
        # ------------------------------------------
        if [ "$FLAKE8_EXISTS" = true ]; then
            echo -e "${BLUE}[LINT]${NC} Checking style with flake8..."
            
            # Capture flake8 output
            LINT_OUTPUT=$(flake8 "$py_file" 2>&1)
            
            if [ -z "$LINT_OUTPUT" ]; then
                echo -e "${GREEN}[LINT OK]${NC} No style issues found."
            else
                echo -e "${YELLOW}[LINT WARN]${NC} Style issues detected:"
                echo "$LINT_OUTPUT"
                ((LINT_FAIL_COUNT++))
            fi
        fi

        # ------------------------------------------
        # 2. EXECUTION & OUTPUT COMPARISON
        # ------------------------------------------
        output_file="${dir}output.txt"
        file_expected="$DIRECTORY_EXPECTED_OUTPUT/${name_of_exercise}_eo.txt"
        input_file="${dir}input.txt"

        # Run Python
        if [ -f "$input_file" ]; then
            python3 "$py_file" < "$input_file" > "$output_file" 2>&1
        else
            python3 "$py_file" > "$output_file" 2>&1
        fi

        # Compare
        if [ ! -f "$file_expected" ]; then
            echo -e "${YELLOW}[MISSING]${NC} Expected output file not found: $file_expected"
            ((SKIP_COUNT++))
        else
            if cmp -s "$output_file" "$file_expected"; then
                echo -e "${GREEN}[SUCCESS]${NC} Output matches expected result."
                ((PASS_COUNT++))
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
                ((FAIL_COUNT++))
            fi
        fi

        # ------------------------------------------
        # 3. CLEANUP
        # ------------------------------------------
        # Remove the generated output file to keep directory clean
        rm -f "$output_file"
    fi
done

# ==========================================
# FINAL SUMMARY
# ==========================================
echo -e "\n\n${BOLD}========================================${NC}"
echo -e "${BOLD}              FINAL SUMMARY            ${NC}"
echo -e "${BOLD}========================================${NC}"
echo -e "Total Exercises:   ${BOLD}${TOTAL_COUNT}${NC}"
echo -e "Passed (Output):   ${GREEN}${PASS_COUNT}${NC}"
echo -e "Failed (Output):   ${RED}${FAIL_COUNT}${NC}"
echo -e "Skipped:           ${YELLOW}${SKIP_COUNT}${NC}"

if [ "$FLAKE8_EXISTS" = true ]; then
    if [ "$LINT_FAIL_COUNT" -gt 0 ]; then
        echo -e "Lint Issues:       ${YELLOW}${LINT_FAIL_COUNT}${NC} (files with style errors)"
    else
        echo -e "Lint Issues:       ${GREEN}0 (All clean!)${NC}"
    fi
fi

echo -e "${BOLD}========================================${NC}"

# Final status logic
if [ "$FAIL_COUNT" -gt 0 ]; then
    echo -e "${RED}Status: TESTS FAILED${NC}"
    exit 1
elif [ "$LINT_FAIL_COUNT" -gt 0 ]; then
    echo -e "${YELLOW}Status: TESTS PASSED but LINTING ISSUES DETECTED${NC}"
    exit 0
else
    echo -e "${GREEN}Status: ALL TESTS PASSED & CODE CLEAN${NC}"
    exit 0
fi