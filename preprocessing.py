import pandas as pd
import os
from config import USER_DATA, SATISFACTION_DATA

def load_and_clean():
    print(f"Loading data from: {USER_DATA}")
    try:
        users = pd.read_csv(USER_DATA)
        print(f"Loaded {len(users)} user records")
    except FileNotFoundError:
        raise FileNotFoundError(f"User data not found at {USER_DATA}")

    # Clean spending score
    users['Spending_Score'] = users['Spending_Score'].str.title().map({
        'Low': 1, 'Average': 2, 'High': 3
    }).fillna(2)
    
    # Load satisfaction data
    satisfaction = pd.read_csv(SATISFACTION_DATA)
    satisfaction['Quality_Score'] = (
        0.7 * satisfaction['ProductQuality'] + 
        0.3 * satisfaction['ServiceQuality']
    )
    
    # Merge datasets on demographics
    users = users.merge(
        satisfaction.groupby(['Age', 'Gender'])['Quality_Score'].mean().reset_index(),
        on=['Age', 'Gender'],
        how='left'
    ).fillna(5)  # Default score
    
    return users

if __name__ == "__main__":
    clean_data = load_and_clean()
    clean_data.to_csv("data/cleaned_users.csv", index=False)