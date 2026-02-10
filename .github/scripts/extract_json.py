import json
import sys

raw = open('/tmp/review_raw.txt').read()

# 첫 번째 { 부터 중괄호 매칭으로 JSON 추출
start = raw.find('{')
if start == -1:
    print('ERROR: No { found in Claude output', file=sys.stderr)
    sys.exit(1)

depth = 0
end = -1
in_string = False
escape = False

for i in range(start, len(raw)):
    c = raw[i]
    if escape:
        escape = False
        continue
    if c == '\\':
        if in_string:
            escape = True
        continue
    if c == '"' and not escape:
        in_string = not in_string
        continue
    if in_string:
        continue
    if c == '{':
        depth += 1
    elif c == '}':
        depth -= 1
        if depth == 0:
            end = i
            break

if end == -1:
    print('ERROR: Unmatched braces in Claude output', file=sys.stderr)
    print('Raw output (first 500):', raw[:500], file=sys.stderr)
    sys.exit(1)

json_str = raw[start:end+1]

try:
    data = json.loads(json_str)
except json.JSONDecodeError as e:
    print(f'ERROR: Invalid JSON: {e}', file=sys.stderr)
    print('JSON string (first 500):', json_str[:500], file=sys.stderr)
    sys.exit(1)

json.dump(data, open('/tmp/review.json', 'w'), ensure_ascii=False, indent=2)
print('JSON extracted successfully')
