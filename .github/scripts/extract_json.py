import json
import re
import sys

raw = open('/tmp/review_raw.txt').read()

# ```json ... ``` 블록 추출 시도
m = re.search(r'```json\s*(.*?)```', raw, re.DOTALL)
if not m:
    m = re.search(r'```\s*(.*?)```', raw, re.DOTALL)
if m:
    text = m.group(1)
else:
    text = raw

# 첫 번째 { 부터 마지막 } 까지 추출
start = text.find('{')
end = text.rfind('}')
if start == -1 or end == -1:
    print('ERROR: No JSON found in Claude output', file=sys.stderr)
    print('Raw output:', raw[:500], file=sys.stderr)
    sys.exit(1)

json_str = text[start:end+1]
data = json.loads(json_str)
json.dump(data, open('/tmp/review.json', 'w'), ensure_ascii=False, indent=2)
print('JSON extracted successfully')
