#!/usr/bin/env python
from tokenizer import tokenize
from parser import parse
from evaluator import evaluate

# Test cases for ternary operator
test_cases = [
    ('true ? 1 : 2', 1),
    ('false ? 1 : 2', 2),
    ('5 > 3 ? "yes" : "no"', 'yes'),
    ('5 < 3 ? "yes" : "no"', 'no'),
    ('x = 10; x > 5 ? x * 2 : x', 20),  # Should evaluate true branch
    ('y = 3; y > 5 ? y * 2 : y', 3),    # Should evaluate false branch
    ('0 ? 99 : 88', 88),                # 0 is falsy
    ('"" ? 99 : 88', 88),               # empty string is falsy
    ('"hello" ? 99 : 88', 99),          # non-empty string is truthy
    ('[] ? 99 : 88', 88),               # empty list is falsy
    ('[1] ? 99 : 88', 99),              # non-empty list is truthy
    ('true ? true ? 1 : 2 : 3', 1),     # nested ternary, left side true
    ('true ? false ? 1 : 2 : 3', 2),    # nested ternary, right side evaluated
    ('false ? 1 : true ? 2 : 3', 2),    # nested ternary on right
]

print("Testing Ternary Operator Implementation\n")
passed_count = 0
failed_count = 0

for code, expected in test_cases:
    env = {}
    try:
        result, status = evaluate(parse(tokenize(code)), env)
        is_pass = result == expected
        if is_pass:
            passed_count += 1
            status_msg = 'PASS'
        else:
            failed_count += 1
            status_msg = 'FAIL'
        
        print(f'{status_msg} | {code:50} => {result} (expected: {expected})')
    except Exception as e:
        failed_count += 1
        print(f'ERROR | {code:50} => {str(e)}')

print(f'\n{passed_count} passed, {failed_count} failed out of {len(test_cases)} tests')
