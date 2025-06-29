import pandas as pd
import os
from config import *

def generate_recommendations():
    """
    Generates product recommendations for users based on their bucket preferences
    """
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    
    print("\n🔄 Loading and preparing data...")
    
    try:
        # Load scored users data
        users = pd.read_csv("data/scored_users.csv")
        print(f"✅ Loaded {len(users)} scored user records")
        
        # Load product data
        products = pd.read_csv(PRODUCT_DATA)
        print(f"✅ Loaded {len(products)} product records")
        
    except FileNotFoundError as e:
        print(f"❌ Critical file missing: {e}")
        return

    # Filter and prepare products
    print("\n🔍 Filtering valid products...")
    valid_products = products[
        products['final_bucket'].isin(BUCKET_MAPPING.keys())
    ].copy()  # Explicit copy to avoid SettingWithCopyWarning
    
    # Map product buckets to user bucket categories
    valid_products.loc[:, 'UserBucket'] = valid_products['final_bucket'].map(BUCKET_MAPPING)
    print(f"📦 Valid products after filtering: {len(valid_products)}/{len(products)}")

    # Generate recommendations
    print("\n🎯 Generating recommendations...")
    results = []
    
    for _, product in valid_products.iterrows():
        bucket = product['UserBucket']
        
        # Find qualified users
        qualified_users = users[users[bucket] >= THRESHOLDS[bucket]]
        
        if len(qualified_users) == 0:
            continue  # Skip if no users qualify
            
        # Get top 3 matching users
        top_users = qualified_users.sort_values(bucket, ascending=False).head(3)
        
        for rank, (_, user) in enumerate(top_users.iterrows(), 1):
            results.append({
                'product_id': product.name,
                'product_name': str(product['product_name'])[:50],  # Truncate long names
                'product_bucket': product['final_bucket'],
                'user_id': user['ID'],
                'user_age': user['Age'],
                'user_gender': user['Gender'],
                'user_profession': user['Profession'],
                'match_score': user[bucket],
                'match_threshold': THRESHOLDS[bucket],
                'match_rank': rank,
                'match_reason': get_match_reason(user, bucket)
            })

    # Save results
    if results:
        output_path = os.path.join('output', 'recommendations.csv')
        pd.DataFrame(results).to_csv(output_path, index=False)
        print(f"\n✅ Success! Saved {len(results)} recommendations to:\n{os.path.abspath(output_path)}")
        
        # Print summary
        rec_df = pd.DataFrame(results)
        print("\n📊 Recommendation Summary:")
        print(rec_df['product_bucket'].value_counts())
        
    else:
        print("\n⚠️ No recommendations generated. Possible issues:")
        print("- User scores below thresholds")
        print("- Product bucket mismatch")
        print("- Insufficient qualifying users")

def get_match_reason(user, bucket):
    """Generates human-readable match explanations"""
    reasons = {
        'Fashion': f"Fashion-conscious {user['Age']}yo {user['Gender']}",
        'Tech': f"Tech-inclined {user['Profession']} with high quality preference",
        'Luxury': f"High-spending {user['Age']}yo with premium tastes",
        'Home': f"Home-focused family of {user.get('Family_Size', 2)}",
        'Beauty': f"Beauty-interested {user['Gender']}",
        'Budget': f"Value-conscious {user['Profession']}"
    }
    return reasons.get(bucket, "Strong preference match")

if __name__ == "__main__":
    print("="*50)
    print("🚀 LAUNCH LAB RECOMMENDATION ENGINE")
    print("="*50)
    
    generate_recommendations()
    
    print("\n" + "="*50)
    print("✨ Recommendation generation complete")
    print("="*50)