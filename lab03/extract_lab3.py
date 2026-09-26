import re
import json

with open(r'C:\Users\Thao\.gemini\antigravity-ide\brain\d985158b-50cf-4fb4-ae33-a12f1d007eb3\.system_generated\steps\204\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

results = {}

# Status
stat_m = re.search(r'class="badge.*?>(Success|Fail.*?)</', text)
if not stat_m: stat_m = re.search(r'm_imgStatus.*?>(.*?)<', text)
results['Status'] = stat_m.group(1) if stat_m else '[KHÔNG ĐỌC ĐƯỢC]'

# Block
block_m = re.search(r'href="/block/(\d+)">', text)
results['Block'] = block_m.group(1) if block_m else '[KHÔNG ĐỌC ĐƯỢC]'

# Timestamp
ts_m = re.search(r'data-bs-title="(.*?)"', text)
# Alternatively, looking for Timestamp string directly
ts_m2 = re.search(r'<span id="clock"></span>\s*(.*?)\s*<', text)
if not ts_m2:
    ts_m2 = re.search(r'Timestamp:.*?<div.*?>.*?<i.*?</i>(.*?)</div>', text, re.DOTALL)
# Etherscan timestamp format
ts_m3 = re.search(r'(\d+ \w+ ago \([^)]+\))', text)
if ts_m3:
    results['Timestamp'] = ts_m3.group(1).split(' (')[1].replace(')','')
else:
    ts_alt = re.search(r'(\w+-\d+-\d+\s+\d+:\d+:\d+\s+[A-Z]+)', text)
    results['Timestamp'] = ts_alt.group(1) if ts_alt else '[KHÔNG ĐỌC ĐƯỢC]'

# From
from_m = re.search(r'id="ContentPlaceHolder1_hdnFromAddress"\s*value="([^"]+)"', text)
results['From'] = from_m.group(1) if from_m else '[KHÔNG ĐỌC ĐƯỢC]'

# To
to_m = re.findall(r'data-clipboard-text="(0x[a-fA-F0-9]{40})"', text)
results['To'] = to_m[-1] if to_m else '[KHÔNG ĐỌC ĐƯỢC]'
if len(to_m) > 1:
    results['To'] = to_m[1] # typically index 1 is 'to' if 0 is 'from'

# Value
val_m = re.search(r'id="ContentPlaceHolder1_spanValue">.*?<span id=\'data-val\'.*?>(.*?)</span>', text)
if val_m: 
    results['Value'] = re.sub(r'<[^>]+>', '', val_m.group(1)).replace('<b>.</b>', '.')
else:
    results['Value'] = '[KHÔNG ĐỌC ĐƯỢC]'

# Transaction Fee
fee_m = re.search(r'id="ContentPlaceHolder1_spanTxFee">.*?<span id=\'data-txfee\'.*?>(.*?)</span>', text)
if fee_m:
    results['Transaction Fee'] = re.sub(r'<[^>]+>', '', fee_m.group(1)).replace('<b>.</b>', '.')
else:
    results['Transaction Fee'] = '[KHÔNG ĐỌC ĐƯỢC]'

# Gas Price
gp_m = re.search(r'id="ContentPlaceHolder1_spanGasPrice".*?<span id=\'data-gas\'>(.*?)</span>', text)
if gp_m:
    results['Gas Price'] = re.sub(r'<[^>]+>', '', gp_m.group(1)).replace('<b>.</b>', '.')
else:
    results['Gas Price'] = '[KHÔNG ĐỌC ĐƯỢC]'

# Gas Limit & Gas Used & Nonce
# Usually these are inside specific elements. Let's find them around labels.
gl_m = re.search(r'Gas Limit &amp; Usage by Txn:.*?<span.*?>([\d,]+)</span>\s*\|\s*<span.*?>([\d,]+)</span>', text, re.DOTALL)
if gl_m:
    results['Gas Limit'] = gl_m.group(1)
    results['Gas Used'] = gl_m.group(2)
else:
    gl_m2 = re.search(r'Gas Limit:.*?([\d,]+)', text)
    gu_m2 = re.search(r'Gas Used:.*?([\d,]+)', text)
    # Etherscan has 'Gas Limit & Usage by Txn' 
    # Let's search broadly
    gl_m3 = re.search(r'>Gas Limit &amp; Usage by Txn:.*?([\d,]+)\s*\|\s*([\d,]+)', text, re.IGNORECASE | re.DOTALL)
    if gl_m3:
        results['Gas Limit'] = gl_m3.group(1)
        results['Gas Used'] = gl_m3.group(2)
    else:
        results['Gas Limit'] = '[KHÔNG ĐỌC ĐƯỢC]'
        results['Gas Used'] = '[KHÔNG ĐỌC ĐƯỢC]'

nonce_m = re.search(r'>Nonce:.*?<span.*?>(\d+)</span>', text, re.IGNORECASE | re.DOTALL)
if nonce_m:
    results['Nonce'] = nonce_m.group(1)
else:
    nonce_m2 = re.search(r'>Nonce.*?<div.*?>(\d+)', text, re.IGNORECASE | re.DOTALL)
    if nonce_m2:
        results['Nonce'] = nonce_m2.group(1)
    else:
        results['Nonce'] = '[KHÔNG ĐỌC ĐƯỢC]'

# Write output to json
with open('lab03/parsed.json', 'w', encoding='utf-8') as fw:
    json.dump(results, fw)
