import json
import re
import sys

raw = open('/tmp/review_raw.txt').read()

# ```json 이후의 내용만 추출 (closing ```이 없어도 동작)
if '```json' in raw:
    text = raw.split('```json', 1)[1]
    # closing ``` 가 있으면 그 전까지만
    if '```' in text:
        text = text.split('```', 1)[0]
elif '```' in raw:
    text = raw.split('```', 1)[1]
    if '```' in text:
        text = text.split('```', 1)[0]
else:
    text = raw

# 첫 번째 { 부터 마지막 } 까지 추출
start = text.find('{')
end = text.rfind('}')
if start == -1 or end == -1:
    # raw 전체에서 다시 시도
    start = raw.find('{')
    end = raw.rfind('}')
    if start == -1 or end == -1:
        print('ERROR: No JSON found in Claude output', file=sys.stderr)
        print('Raw output (first 500):', raw[:500], file=sys.stderr)
        sys.exit(1)
    json_str = raw[start:end+1]
else:
    json_str = text[start:end+1]

try:
    data = json.loads(json_str)
except json.JSONDecodeError as e:
    print(f'ERROR: Invalid JSON: {e}', file=sys.stderr)
    print('JSON string (first 500):', json_str[:500], file=sys.stderr)
    sys.exit(1)

json.dump(data, open('/tmp/review.json', 'w'), ensure_ascii=False, indent=2)
print('JSON extracted successfully')
