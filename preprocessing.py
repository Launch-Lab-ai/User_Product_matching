import pandas as pd
from config import USER_DATA, SATISFACTION_DATA, PRODUCT_DATA

def load_and_clean():
    print(f"📂 Loading data from: {USER_DATA}")
    
    try:
        users = pd.read_csv(USER_DATA)
        print(f"✅ Loaded {len(users)} user records")
    except FileNotFoundError as e:
        raise SystemExit(f"❌ Critical error: {str(e)}")

    # Clean spending scores
    users['Spending_Score'] = (
        users['Spending_Score']
        .str.title()
        .map({'Low': 1, 'Average': 2, 'High': 3})
        .fillna(2)
    )
    
    # Process product data to reduce uncategorized items
    try:
        products = pd.read_csv(PRODUCT_DATA)
        products['final_bucket'] = products.apply(
            lambda x: 'Home & Decor' if 'decor' in str(x['product_name']).lower()
            else 'Clothing' if any(kw in str(x['product_name']).lower() 
                                 for kw in ['shirt','dress','pant'])
            else x['final_bucket'],
            axis=1
        )
        products.to_csv(PRODUCT_DATA, index=False)
        print("✅ Processed product categories")
    except FileNotFoundError:
        print("⚠️ Product data not found - proceeding without preprocessing")

    # Process satisfaction data
    satisfaction = pd.read_csv(SATISFACTION_DATA)
    satisfaction['Quality_Score'] = (
        0.7 * satisfaction['ProductQuality'] + 
        0.3 * satisfaction['ServiceQuality']
    )
    
    # Merge datasets
    return users.merge(
        satisfaction.groupby(['Age', 'Gender'])['Quality_Score'].mean().reset_index(),
        on=['Age', 'Gender'],
        how='left'
    ).fillna(5)  # Default neutral score

if __name__ == "__main__":
    clean_data = load_and_clean()
    clean_data.to_csv("data/cleaned_users.csv", index=False)
    print("✅ Cleaned data saved to data/cleaned_users.csv")
