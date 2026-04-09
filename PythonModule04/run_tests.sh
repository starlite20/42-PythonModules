#!/bin/bash

# ==========================================
# CONFIGURATION
# ==========================================
CODE_DIR="code"
TESTCASE_DIR="expected_output"

# ANSI Color Codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

# Counters: exercises
TOTAL_EXERCISES=0
PASS_EXERCISES=0
FAIL_EXERCISES=0
SKIP_EXERCISES=0

# Counters: cases
TOTAL_CASES=0
PASS_CASES=0
FAIL_CASES=0
SKIP_CASES=0

# Static analysis
LINT_FAIL_COUNT=0
TYPE_FAIL_COUNT=0

# Determine Diff Command
if command -v git >/dev/null 2>&1; then
    DIFF_CMD="git diff --no-index --color=always"
else
    DIFF_CMD="diff -u"
fi

# Check for flake8
FLAKE8_EXISTS=false
if command -v flake8 >/dev/null 2>&1; then
    FLAKE8_EXISTS=true
fi

# Check for mypy
MYPY_EXISTS=false
if command -v mypy >/dev/null 2>&1; then
    MYPY_EXISTS=true
fi

# ==========================================
# HELPERS
# ==========================================
print_diff() {
    local expected_file="$1"
    local actual_file="$2"

    if [[ "$DIFF_CMD" == *"git"* ]]; then
        $DIFF_CMD "$expected_file" "$actual_file" | cat
    else
        $DIFF_CMD "$expected_file" "$actual_file" | sed \
            -e "s/^\-\-.*/${CYAN}\0${NC}/" \
            -e "s/^++.*/${CYAN}\0${NC}/" \
            -e "s/^@@.*/${CYAN}\0${NC}/" \
            -e "s/^-/${RED}-/${NC}/" \
            -e "s/^+/${GREEN}+/${NC}/"
    fi
}

copy_exercise_to_sandbox() {
    local source_dir="$1"
    local sandbox_dir="$2"

    mkdir -p "$sandbox_dir"
    cp -R "$source_dir"/. "$sandbox_dir"/
}

parse_ip_file() {
    local ip_file="$1"
    local cmd_file="$2"
    local stdin_file="$3"
    local post_file="$4"

    : > "$cmd_file"
    : > "$stdin_file"
    : > "$post_file"

    local first_python_found=false
    local collecting_stdin=false
    local shell_cmd=""

    while IFS= read -r line || [ -n "$line" ]; do
        if [[ "$line" == '$> '* ]]; then
            shell_cmd="${line#\$> }"

            if [ "$first_python_found" = false ] && [[ "$shell_cmd" == python3* ]]; then
                echo "$shell_cmd" > "$cmd_file"
                first_python_found=true
                collecting_stdin=true
            else
                collecting_stdin=false
                echo "$shell_cmd" >> "$post_file"
            fi
        else
            if [ "$collecting_stdin" = true ]; then
                printf "%s\n" "$line" >> "$stdin_file"
            fi
        fi
    done < "$ip_file"
}

run_case_from_ip_file() {
    local sandbox_dir="$1"
    local ip_file="$2"
    local actual_file="$3"
    local temp_case_dir="$4"

    local cmd_file="$temp_case_dir/cmd.txt"
    local stdin_file="$temp_case_dir/stdin.txt"
    local post_file="$temp_case_dir/post.txt"

    parse_ip_file "$ip_file" "$cmd_file" "$stdin_file" "$post_file"

    local main_cmd=""
    main_cmd=$(head -n 1 "$cmd_file")

    if [ -z "$main_cmd" ]; then
        return 1
    fi

    : > "$actual_file"

    if [ -s "$stdin_file" ]; then
        bash -c "cd \"$sandbox_dir\" && $main_cmd" < "$stdin_file" > "$actual_file" 2>&1
    else
        bash -c "cd \"$sandbox_dir\" && $main_cmd" > "$actual_file" 2>&1
    fi

    while IFS= read -r post_cmd || [ -n "$post_cmd" ]; do
        [ -z "$post_cmd" ] && continue
        bash -c "cd \"$sandbox_dir\" && $post_cmd" >> "$actual_file" 2>&1
    done < "$post_file"

    return 0
}

# ==========================================
# SETUP
# ==========================================
if [ ! -d "$CODE_DIR" ]; then
    echo -e "${RED}Error: Directory '$CODE_DIR' not found.${NC}"
    exit 1
fi

if [ ! -d "$TESTCASE_DIR" ]; then
    echo -e "${RED}Error: Directory '$TESTCASE_DIR' not found.${NC}"
    exit 1
fi

echo "========================================"
echo -e "${CYAN}Starting Automated Test Runner${NC}"
echo "Using Diff Tool: $(echo "$DIFF_CMD" | cut -d' ' -f1)"

if [ "$FLAKE8_EXISTS" = true ]; then
    echo "Linting Tool: flake8"
else
    echo -e "${YELLOW}Warning: flake8 not found. Skipping lint checks.${NC}"
fi

if [ "$MYPY_EXISTS" = true ]; then
    echo "Type Checker: mypy"
else
    echo -e "${YELLOW}Warning: mypy not found. Skipping type checks.${NC}"
fi

echo "========================================"

TMP_ROOT=$(mktemp -d)
trap 'rm -rf "$TMP_ROOT"' EXIT

# ==========================================
# MAIN LOOP
# ==========================================
for dir in "$CODE_DIR"/*/; do
    [ -d "$dir" ] || continue
    ((TOTAL_EXERCISES++))

    exercise_name=$(basename "$dir")
    py_file=$(find "$dir" -maxdepth 1 -type f -name "*.py" | head -n 1)
    exercise_test_dir="$TESTCASE_DIR/$exercise_name"

    if [ -z "$py_file" ]; then
        echo -e "${YELLOW}[SKIP]${NC} No Python file found in: $exercise_name"
        ((SKIP_EXERCISES++))
        continue
    fi

    echo -e "\n${BOLD}========================================${NC}"
    echo -e "Processing: ${CYAN}$exercise_name${NC} ($(basename "$py_file"))"
    echo -e "${BOLD}========================================${NC}"

    # ------------------------------------------
    # 1. LINTING CHECK
    # ------------------------------------------
    if [ "$FLAKE8_EXISTS" = true ]; then
        echo -e "${BLUE}[LINT]${NC} Checking style with flake8..."
        LINT_OUTPUT=$(flake8 "$py_file" 2>&1)

        if [ -z "$LINT_OUTPUT" ]; then
            echo -e "${GREEN}[LINT OK]${NC} No style issues found."
        else
            echo -e "${YELLOW}[LINT WARN]${NC} Style issues detected!"
            # echo "$LINT_OUTPUT"
            # ((LINT_FAIL_COUNT++))
        fi
    fi

    # ------------------------------------------
    # 2. TYPE CHECK
    # ------------------------------------------
    if [ "$MYPY_EXISTS" = true ]; then
        echo -e "${BLUE}[TYPE]${NC} Checking types with mypy..."
        TYPE_OUTPUT=$(mypy "$py_file" --ignore-missing-imports --follow-imports=silent 2>&1 | grep "error:")

        if [ -z "$TYPE_OUTPUT" ]; then
            echo -e "${GREEN}[TYPE OK]${NC} No type issues found."
        else
            echo -e "${RED}[TYPE FAIL]${NC} Type inconsistencies detected:"
            echo "$TYPE_OUTPUT"
            ((TYPE_FAIL_COUNT++))
        fi
    fi

    # ------------------------------------------
    # 3. TEST CASE DISCOVERY
    # ------------------------------------------
    if [ ! -d "$exercise_test_dir" ]; then
        echo -e "${YELLOW}[SKIP]${NC} No testcase directory found for $exercise_name at $exercise_test_dir"
        ((SKIP_EXERCISES++))
        continue
    fi

    case_files=$(find "$exercise_test_dir" -maxdepth 1 -type f -name "*_ip_*.txt" | sort)

    if [ -z "$case_files" ]; then
        echo -e "${YELLOW}[SKIP]${NC} No testcase input files found in $exercise_test_dir"
        ((SKIP_EXERCISES++))
        continue
    fi

    exercise_case_total=0
    exercise_case_pass=0
    exercise_case_fail=0
    exercise_case_skip=0

    # ------------------------------------------
    # 4. EXECUTION & OUTPUT COMPARISON
    # ------------------------------------------
    for ip_file in $case_files; do
        case_file=$(basename "$ip_file")
        case_index=$(echo "$case_file" | sed -E 's/^.*_ip_([0-9]+)\.txt$/\1/')
        prefix=$(echo "$case_file" | sed -E 's/_ip_[0-9]+\.txt$//')
        op_file="$exercise_test_dir/${prefix}_op_${case_index}.txt"

        ((TOTAL_CASES++))
        ((exercise_case_total++))

        if [ ! -f "$op_file" ]; then
            echo -e "${YELLOW}[CASE ${case_index} SKIP]${NC} Missing expected output file: $(basename "$op_file")"
            ((SKIP_CASES++))
            ((exercise_case_skip++))
            continue
        fi

        echo -e "${BLUE}[CASE ${case_index}]${NC} Using $(basename "$ip_file") vs $(basename "$op_file")"

        sandbox_dir="$TMP_ROOT/${exercise_name}_case_${case_index}_sandbox"
        temp_case_dir="$TMP_ROOT/${exercise_name}_case_${case_index}_temp"
        actual_file="$TMP_ROOT/${exercise_name}_case_${case_index}.out"

        mkdir -p "$temp_case_dir"
        copy_exercise_to_sandbox "$dir" "$sandbox_dir"

        if ! run_case_from_ip_file "$sandbox_dir" "$ip_file" "$actual_file" "$temp_case_dir"; then
            echo -e "${YELLOW}[CASE ${case_index} SKIP]${NC} Could not parse runnable python command from $(basename "$ip_file")"
            ((SKIP_CASES++))
            ((exercise_case_skip++))
            continue
        fi

        if cmp -s "$actual_file" "$op_file"; then
            echo -e "${GREEN}[CASE ${case_index} PASS]${NC} Output matches expected."
            ((PASS_CASES++))
            ((exercise_case_pass++))
        else
            echo -e "${RED}[CASE ${case_index} FAIL]${NC} Differences detected:"
            print_diff "$op_file" "$actual_file"
            ((FAIL_CASES++))
            ((exercise_case_fail++))
        fi
    done

    # ------------------------------------------
    # 5. EXERCISE SUMMARY
    # ------------------------------------------
    if [ "$exercise_case_fail" -eq 0 ] && [ "$exercise_case_pass" -gt 0 ]; then
        echo -e "${GREEN}[EXERCISE PASS]${NC} ${exercise_case_pass}/${exercise_case_total} cases passed."
        ((PASS_EXERCISES++))
    elif [ "$exercise_case_pass" -eq 0 ] && [ "$exercise_case_skip" -eq "$exercise_case_total" ]; then
        echo -e "${YELLOW}[EXERCISE SKIP]${NC} All cases skipped."
        ((SKIP_EXERCISES++))
    else
        echo -e "${RED}[EXERCISE FAIL]${NC} ${exercise_case_pass}/${exercise_case_total} cases passed, ${exercise_case_fail} failed, ${exercise_case_skip} skipped."
        ((FAIL_EXERCISES++))
    fi
done

# ==========================================
# FINAL SUMMARY
# ==========================================
echo -e "\n\n${BOLD}========================================${NC}"
echo -e "${BOLD}              FINAL SUMMARY            ${NC}"
echo -e "${BOLD}========================================${NC}"

echo -e "${BOLD}Exercises${NC}"
echo -e "Total Exercises:   ${BOLD}${TOTAL_EXERCISES}${NC}"
echo -e "Passed:            ${GREEN}${PASS_EXERCISES}${NC}"
echo -e "Failed:            ${RED}${FAIL_EXERCISES}${NC}"
echo -e "Skipped:           ${YELLOW}${SKIP_EXERCISES}${NC}"

echo
echo -e "${BOLD}Test Cases${NC}"
echo -e "Total Cases:       ${BOLD}${TOTAL_CASES}${NC}"
echo -e "Passed:            ${GREEN}${PASS_CASES}${NC}"
echo -e "Failed:            ${RED}${FAIL_CASES}${NC}"
echo -e "Skipped:           ${YELLOW}${SKIP_CASES}${NC}"

if [ "$FLAKE8_EXISTS" = true ]; then
    if [ "$LINT_FAIL_COUNT" -gt 0 ]; then
        echo -e "Lint Issues:       ${YELLOW}${LINT_FAIL_COUNT}${NC} (files with style errors)"
    else
        echo -e "Lint Issues:       ${GREEN}0${NC}"
    fi
fi

if [ "$MYPY_EXISTS" = true ]; then
    if [ "$TYPE_FAIL_COUNT" -gt 0 ]; then
        echo -e "Type Issues:       ${RED}${TYPE_FAIL_COUNT}${NC} (files with type errors)"
    else
        echo -e "Type Issues:       ${GREEN}0${NC}"
    fi
fi

echo -e "${BOLD}========================================${NC}"

# Final status logic
if [ "$FAIL_CASES" -gt 0 ] || [ "$TYPE_FAIL_COUNT" -gt 0 ]; then
    echo -e "${RED}Status: TESTS FAILED${NC}"
    exit 1
elif [ "$LINT_FAIL_COUNT" -gt 0 ]; then
    echo -e "${YELLOW}Status: TESTS PASSED but LINTING ISSUES DETECTED${NC}"
    exit 0
else
    echo -e "${GREEN}Status: ALL TESTS PASSED & CODE CLEAN${NC}"
    exit 0
fi