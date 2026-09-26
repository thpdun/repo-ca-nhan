import re

with open(r'C:\Users\Thao\.gemini\antigravity-ide\brain\d985158b-50cf-4fb4-ae33-a12f1d007eb3\.system_generated\steps\204\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

b = re.search(r'data-bs-content="(\d+) Block Confirmations"', text)
if b: print('BLOCK CONFIRMATIONS:', b.group(1))

bb = re.search(r'href="/block/(\d+)"', text)
if bb: print('BLOCK:', bb.group(1))

gl = re.search(r'>(\d{1,3}(,\d{3})*)</span>\s*\|\s*<span[^>]+>(\d{1,3}(,\d{3})*).*?%.*?</span>', text)
if gl: print('GAS LIMIT:', gl.group(1), 'GAS USED:', gl.group(3))
else:
    # Alternative format
    gl2 = re.search(r'Gas Limit:.*?(\d{1,3}(,\d{3})*)', text, re.DOTALL)
    gu2 = re.search(r'Gas Used:.*?(\d{1,3}(,\d{3})*)', text, re.DOTALL)
    if gl2: print('GAS LIMIT:', gl2.group(1))
    if gu2: print('GAS USED:', gu2.group(1))
