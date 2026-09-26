import re
with open(r'C:\Users\Thao\.gemini\antigravity-ide\brain\d985158b-50cf-4fb4-ae33-a12f1d007eb3\.system_generated\steps\118\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Meta Description (contains summary of tx)
desc_m = re.search(r'<meta property="og:description" content="(.*?)"', text)
if desc_m: print('OG_DESC:', desc_m.group(1))

# 2. Tx Hash
tx_m = re.search(r'<title>\s*.*?Transaction Hash:\s*([a-zA-Z0-9x]+)\.\.\.', text)
if tx_m: print('TX_HASH:', tx_m.group(1))

# 3. Status
stat_m = re.search(r'm_imgStatus.*?>(.*?)<', text)
if not stat_m:
    stat_m = re.search(r'class="badge.*?>(Success|Fail.*?)</', text)
if stat_m: print('STATUS:', stat_m.group(1))

# 4. From
from_m = re.search(r'id="ContentPlaceHolder1_hdnFromAddress"\s*value="([^"]+)"', text)
if from_m: print('FROM:', from_m.group(1))

# 5. To
to_m = re.search(r'data-clipboard-text="(0x[a-fA-F0-9]{40})"', text)
if to_m:
    print('TOs:', re.findall(r'data-clipboard-text="(0x[a-fA-F0-9]{40})"', text))

# 6. Value
val_m = re.search(r'id="ContentPlaceHolder1_spanValue">.*?<span id=\'data-val\'.*?>(.*?)</span>', text)
if val_m: print('VALUE:', val_m.group(1))

# 7. Fee
fee_m = re.search(r'id="ContentPlaceHolder1_spanTxFee">.*?<span id=\'data-txfee\'.*?>(.*?)</span>', text)
if fee_m: print('FEE:', fee_m.group(1))
