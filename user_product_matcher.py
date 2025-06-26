import pandas as pd

# --- STEP 1: Load and Clean User Data ---
df = pd.read_csv("Train.csv")
df.rename(columns={'Spending Score (1-100)': 'Spending_Score'}, inplace=True)
df['Spending_Score'] = pd.to_numeric(df['Spending_Score'], errors='coerce').fillna(0)

# Convert Spending Score to categories
def spending_score_category(score):
    if score > 60:
        return 'High'
    elif score >= 40:
        return 'Average'
    else:
        return 'Low'

df['Spending_Score_Category'] = df['Spending_Score'].apply(spending_score_category)

# Estimate Family Size
if 'Family_Size' in df.columns:
    df['FamilySize'] = df['Family_Size']
elif 'Kidhome' in df.columns:
    df['FamilySize'] = df['Ever_Married'].map({'Yes': 2, 'No': 1}) + df['Kidhome']
else:
    df['FamilySize'] = df['Ever_Married'].map({'Yes': 2, 'No': 1}) + df['Work_Experience'].fillna(0)

# --- STEP 2: Define Scoring Functions ---
def score_fashion(u):
    s = 0
    if 18 <= u.Age <= 35: s += 2
    if u.Spending_Score_Category == 'High': s += 2
    if u.Gender == 'Female': s += 1
    return min(s, 5)

def score_tech(u):
    s = 0
    if u.Age <= 40: s += 2
    if u.Spending_Score_Category == 'High': s += 2
    if isinstance(u.Profession, str) and u.Profession.strip().lower() == 'engineer': s += 1
    return min(s, 5)

def score_home(u):
    s = 0
    if u.Ever_Married == 'Yes': s += 2
    if u.FamilySize > 2: s += 2
    if u.Spending_Score_Category in ['High', 'Average']: s += 1
    return min(s, 5)

def score_budget(u):
    s = 0
    if u.Spending_Score_Category == 'Low': s += 2
    if u.FamilySize > 3: s += 2
    if u.Ever_Married == 'No': s += 1
    return min(s, 5)

# --- STEP 3: Apply Scores to All Users ---
for name, fn in [('Fashion', score_fashion), ('Tech', score_tech),
                 ('Home & Decor', score_home), ('Budget', score_budget)]:
    df[name] = df.apply(fn, axis=1)

# --- STEP 4: Save User Bucket Scores ---
df[['ID', 'Fashion', 'Tech', 'Home & Decor', 'Budget']].to_csv('user_bucket_scores.csv', index=False)
print("Saved scores to 'user_bucket_scores.csv'")

# --- STEP 5: Load Product Data and Match Users ---
user_df = df[['ID', 'Fashion', 'Tech', 'Home & Decor', 'Budget']].copy()
product_df = pd.read_csv('flipkart_buckets_single_label.csv')

# Map Team B's bucket names to user bucket categories
bucket_mapping = {
    "Clothing": "Fashion",
    "Tech & Gadgets": "Tech",
    "Home & Decor": "Home & Decor",
    "Budget Essentials": "Budget"
}

# Keep only products we can match
product_df = product_df[product_df['final_bucket'].isin(bucket_mapping)].copy()
product_df['UserBucket'] = product_df['final_bucket'].map(bucket_mapping)

matches = []
for _, row in product_df.iterrows():
    bucket = row['UserBucket']
    product_name = row['product_name']
    final_bucket = row['final_bucket']

    # Skip if the bucket isn't available
    if bucket not in user_df.columns:
        continue

    top_users = user_df.sort_values(by=bucket, ascending=False).head(3)

    matches.append({
        'Product Name': product_name,
        'Final Bucket': final_bucket,
        'User 1 ID': top_users.iloc[0]['ID'],
        'User 1 Score': top_users.iloc[0][bucket],
        'User 2 ID': top_users.iloc[1]['ID'],
        'User 2 Score': top_users.iloc[1][bucket],
        'User 3 ID': top_users.iloc[2]['ID'],
        'User 3 Score': top_users.iloc[2][bucket],
    })

# --- STEP 6: Save Matches to CSV ---
match_df = pd.DataFrame(matches)
match_df.to_csv('product_user_matches.csv', index=False)
print("Saved product-to-user matches to 'product_user_matches.csv'")

# --- Optional: Make it runnable as a script ---
if __name__ == "__main__":
    print("User-product matching completed successfully.")
