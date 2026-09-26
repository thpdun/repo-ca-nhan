import urllib.request
import json

def call_rpc(method, params):
    req = urllib.request.Request(
        'https://cloudflare-eth.com',
        data=json.dumps({"jsonrpc":"2.0","method":method,"params":params,"id":1}).encode('utf-8'),
        headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    )
    res = urllib.request.urlopen(req)
    return json.loads(res.read().decode('utf-8'))

# 1. decimals() -> 0x313ce567
res_dec = call_rpc("eth_call", [{"to": "0xdAC17F958D2ee523a2206206994597C13D831ec7", "data": "0x313ce567"}, "latest"])
decimals = int(res_dec['result'], 16)
print(f"DECIMALS: {decimals}")

# 2. totalSupply() -> 0x18160ddd
res_ts = call_rpc("eth_call", [{"to": "0xdAC17F958D2ee523a2206206994597C13D831ec7", "data": "0x18160ddd"}, "latest"])
ts = int(res_ts['result'], 16)
print(f"TOTAL_SUPPLY: {ts}")

# 3. balanceOf(...) -> 0x70a08231
addr = "0xF977814e90dA44bFA03b6295A0616a897441aceC".replace("0x", "").lower().zfill(64)
res_bal = call_rpc("eth_call", [{"to": "0xdAC17F958D2ee523a2206206994597C13D831ec7", "data": "0x70a08231" + addr}, "latest"])
bal = int(res_bal['result'], 16)
print(f"BALANCE: {bal}")
