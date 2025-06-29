import pandas as pd
from config import *

def calculate_scores(users):
    def score_bucket(row, bucket):
        rules = {
            'Fashion': [
                (row['Age'] <= 35, 2),
                (row['Gender'] == 'Female', 1),
                (row['Spending_Score'] == 3, 2)
            ],
            'Tech': [
                (row['Age'] <= 45, 2),
                (row['Quality_Score'] > 7, 2),
                (row['Profession'] in ['Engineer','Doctor'], 1)
            ],
            'Home': [
                (row['Ever_Married'] == 'Yes', 2),
                (row['Family_Size'] > 2, 1)
            ],
            'Budget': [
                (row['Spending_Score'] == 1, 3),
                (row['Quality_Score'] < 5, 1)
            ],
            'Luxury': [
                (row['Spending_Score'] == 3, 3),
                (row['Quality_Score'] > 8, 2),
                (row['Age'] > 30, 1)
            ],
            'Beauty': [
                (row['Gender'] == 'Female', 2),
                (row['Age'] < 45, 1)
            ],
            'Furniture': [
                (row['Ever_Married'] == 'Yes', 2),
                (row['Family_Size'] > 3, 2)
            ],
            'Footwear': [
                (row['Age'] <= 40, 2),
                (row['Spending_Score'] > 1, 1)
            ],
            'Auto': [
                (row['Gender'] == 'Male', 2),
                (row['Age'] > 25, 1)
            ],
            'Media': [
                (row['Age'] <= 30, 2),
                (row['Spending_Score'] < 3, 1)
            ],
            'Gifts': [
                (row['Ever_Married'] == 'Yes', 1),
                (row['Quality_Score'] > 6, 1)
            ],
            'Other': [
                (True, 1)  # Default catch-all
            ]
        }
        return sum(points for (condition, points) in rules[bucket] if condition)

    for bucket in BUCKET_MAPPING.values():
        users[bucket] = users.apply(lambda x: score_bucket(x, bucket), axis=1)
    
    return users

if __name__ == "__main__":
    users = pd.read_csv("data/cleaned_users.csv")
    scored_users = calculate_scores(users)
    scored_users.to_csv("data/scored_users.csv", index=False)