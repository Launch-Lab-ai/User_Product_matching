import pandas as pd

recs = pd.read_csv("output/recommendations.csv")

print("📊 Bucket Distribution:")
print(recs['product_bucket'].value_counts())

print("\n👤 Top User Profiles per Bucket:")
for bucket, group in recs.groupby('product_bucket'):
    print(f"\n{bucket.upper():<15} Avg Age: {group['user_age'].mean():.1f}")
    print(group[['user_age','user_gender','user_profession']].value_counts().head(3))