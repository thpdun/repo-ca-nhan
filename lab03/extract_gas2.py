import re
with open(r'C:\Users\Thao\.gemini\antigravity-ide\brain\d985158b-50cf-4fb4-ae33-a12f1d007eb3\.system_generated\steps\204\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

clean = re.sub(r'<[^>]+>', '', text)
lines = clean.split('\n')
for line in lines:
    if 'Block' in line or 'Gas' in line or 'Nonce' in line:
        print(line.strip())
