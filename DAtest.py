#撈取pchome api資料，keyword為iphone，結果會透過爬蟲取出關鍵字前15名的資料。
#相關檔案為iphone_2025_06.csv

import requests
import pandas as pd
from datetime import datetime

def fetch_top15_products(keyword, output_path):
    base_url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results"
    params = {
        "q": keyword,
        "page": 1,
        "sort": "rnk_dc"
    }

    resp = requests.get(base_url, params=params)
    resp.raise_for_status()
    data = resp.json()

    prods = data.get("prods", [])[:15]  # 只取前15名
    now = datetime.now()
    month_tag = now.strftime("%Y_%m")

    results = []
    for rank, item in enumerate(prods, start=1):
        results.append({
            "month": month_tag,
            "rank": rank,
            "id": item.get("Id"),
            "name": item.get("name"),
            "price": item.get("price"),
            "origin_price": item.get("origin_price")
        })

    df = pd.DataFrame(results)
    filename = f"data/{keyword}_{month_tag}.csv"
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"✅ 已儲存 {filename}")

# 範例：執行一次
fetch_top15_products("iphone", output_path="data/")
