import pandas as pd
from config import BUCKET_MAPPING

def calculate_scores(users):
    def _score_bucket(row, bucket):
        rules = {
            'Fashion': [
                (row['Age'] <= 40, 2),          # Age preference
                (row['Gender'] == 'Female', 2),  # Gender emphasis
                (row['Spending_Score'] == 3, 2), # Spending power
                (row['Quality_Score'] > 6, 1)    # Quality sensitivity
            ],
            'Luxury': [
                (row['Spending_Score'] == 3, 3), # Primary factor
                (row['Gender'] == 'Female', 2),  # Target gender
                (35 <= row['Age'] <= 65, 2),     # Ideal age range
                (row['Profession'] in ['Doctor','Executive','Lawyer'], 2),
                (row['Quality_Score'] > 7, 1)    # Quality expectation
            ],
            'Tech': [
                (row['Age'] <= 50, 2),           # Tech-savvy age
                (row['Quality_Score'] > 7, 3),   # Critical factor
                (row['Profession'] in ['Engineer','Doctor','Artist'], 2),
                (row['Spending_Score'] > 1, 1)   # Minimum spending
            ],
            'Home': [
                (row['Ever_Married'] == 'Yes', 3), # Family orientation
                (row['Family_Size'] > 2, 2),       # Household size
                (row['Age'] > 30, 1),              # Settled age
                (row['Quality_Score'] > 5, 1)      # Basic quality
            ],
            'Furniture': [
                (row['Family_Size'] > 3, 3),       # Large households
                (row['Ever_Married'] == 'Yes', 2),
                (row['Age'] > 35, 1)
            ],
            'Beauty': [
                (row['Gender'] == 'Female', 3),    # Primary market
                (row['Age'] < 50, 2),              # Target age
                (row['Spending_Score'] > 1, 1)     # Some spending power
            ],
            'Auto': [
                (row['Gender'] == 'Male', 3),      # Gender preference
                (row['Age'] > 25, 2),              # Driving age
                (row['Spending_Score'] == 3, 1)    # High spenders
            ],
            'Media': [
                (row['Age'] <= 35, 3),             # Younger audience
                (row['Spending_Score'] < 3, 1)     # Budget-conscious
            ],
            'Footwear': [
                (row['Age'] <= 40, 2),
                (row['Gender'] == 'Female', 2),
                (row['Spending_Score'] > 1, 1)
            ],
            'Gifts': [
                (row['Ever_Married'] == 'Yes', 2), # Gift-giving likelihood
                (row['Spending_Score'] > 1, 1)
            ],
            'Other': [
                (True, 1)  # Catch-all default
            ]
        }
        return sum(points for (condition, points) in rules[bucket] if condition)

    # Calculate scores for all buckets
    for bucket in BUCKET_MAPPING.values():
        users[bucket] = users.apply(lambda x: _score_bucket(x, bucket), axis=1)
    
    return users

if __name__ == "__main__":
    users = pd.read_csv("data/cleaned_users.csv")
    scored_users = calculate_scores(users)
    scored_users.to_csv("data/scored_users.csv", index=False)
    print("✅ User bucket scores calculated and saved")
