# scripts/generate_fake_data.py
import os
import pandas as pd
import random

os.makedirs("data", exist_ok=True)

# 商品池（固定的50個ID與名稱）
product_pool = [
    {"id": f"P{i:03}", "name": f"iPhone 模型 {i}"} for i in range(1, 51)
]

months = ["2025_01", "2025_02", "2025_03", "2025_04", "2025_05", "2025_06"]

for month in months:
    top15 = random.sample(product_pool, 15)
    for rank, item in enumerate(top15, start=1):
        item["rank"] = rank
        item["month"] = month
        item["price"] = random.randint(20000, 40000)
    df = pd.DataFrame(top15)
    df.to_csv(f"data/iphone_{month}.csv", index=False, encoding="utf-8-sig")

print("✅ 六個月的假資料已產生完畢！")
