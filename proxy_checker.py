import requests

def check_proxy(proxy_url):
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    try:
        res = requests.get("https://ipapi.co/json", proxies=proxies, timeout=10)
        return res.json()
    except Exception as e:
        return {"proxy": proxy_url, "error": str(e)}

results = []

with open("proxies.txt", "r") as f:
    for line in f:
        proxy = line.strip()
        if proxy:
            result = check_proxy(proxy)
            results.append(result)

# 將所有結果寫入檔案
import json
with open("proxy_result.json", "w") as out:
    json.dump(results, out, indent=2)

print("Finished checking proxies.")
