import urllib.request
import json
import time

def call_etherscan_proxy(data_payload):
    url = f"https://api.etherscan.io/api?module=proxy&action=eth_call&to=0xdAC17F958D2ee523a2206206994597C13D831ec7&data={data_payload}&tag=latest"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req)
    return json.loads(res.read().decode('utf-8'))

try:
    # 1. decimals() -> 0x313ce567
    res_dec = call_etherscan_proxy("0x313ce567")
    decimals = int(res_dec['result'], 16)
    print(f"DECIMALS: {decimals}")
    time.sleep(6) # sleep to avoid rate limiting (5 sec on Etherscan without API key)

    # 2. totalSupply() -> 0x18160ddd
    res_ts = call_etherscan_proxy("0x18160ddd")
    ts = int(res_ts['result'], 16)
    print(f"TOTAL_SUPPLY: {ts}")
    time.sleep(6)

    # 3. balanceOf(...) -> 0x70a08231
    addr = "0xF977814e90dA44bFA03b6295A0616a897441aceC".replace("0x", "").lower().zfill(64)
    res_bal = call_etherscan_proxy("0x70a08231" + addr)
    bal = int(res_bal['result'], 16)
    print(f"BALANCE: {bal}")
    time.sleep(6)

    # 4. Fetch ABI from Etherscan
    url = "https://api.etherscan.io/api?module=contract&action=getsourcecode&address=0xdAC17F958D2ee523a2206206994597C13D831ec7"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    result = data['result'][0]
    
    print(f"VERIFIED: {result['ABI'] != 'Contract source code not verified'}")
    
    if result['ABI'] != 'Contract source code not verified':
        abi = json.loads(result['ABI'])
        write_funcs = []
        for item in abi:
            if item.get('type') == 'function':
                if item.get('stateMutability') not in ('view', 'pure', 'constant'):
                    write_funcs.append(item['name'])
        if write_funcs:
            print("WRITE_FUNCS:", ", ".join(write_funcs))
            
except Exception as e:
    print(f"Etherscan error: {e}")
