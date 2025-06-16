# scripts/analyze.py
import pandas as pd
import glob
import os

os.makedirs("output", exist_ok=True)

# 讀入所有 csv
files = glob.glob("data/iphone_*.csv")
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# 統計出現次數與平均排名
summary = (
    df.groupby(["id", "name"])
    .agg(appear_count=("rank", "count"), avg_rank=("rank", "mean"))
    .reset_index()
    .sort_values(by=["appear_count", "avg_rank"], ascending=[False, True])
)

summary.to_csv("output/summary.csv", index=False, encoding="utf-8-sig")
print("✅ 分析完成，輸出至 iphone_rank_analytics/output/summary.csv")
