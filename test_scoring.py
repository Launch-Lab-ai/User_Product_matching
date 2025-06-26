from user_product_matcher import score_fashion, score_tech, score_home, score_budget

import pandas as pd

# Example manual test function:
def test_scoring_functions():
    test_users = pd.DataFrame([
        {'Age': 25, 'Spending_Score': 70, 'Gender': 'Female', 'Ever_Married': 'No',
         'Profession': 'Engineer', 'Work_Experience': 3, 'FamilySize': 1},
        {'Age': 45, 'Spending_Score': 30, 'Gender': 'Male', 'Ever_Married': 'Yes',
         'Profession': 'Doctor', 'Work_Experience': 10, 'FamilySize': 4},
        {'Age': 38, 'Spending_Score': 55, 'Gender': 'Female', 'Ever_Married': 'Yes',
         'Profession': 'Engineer', 'Work_Experience': 8, 'FamilySize': 3},
    ])

    # Add Spending_Score_Category manually for testing
    def spending_score_category(score):
        if score > 60:
            return 'High'
        elif score >= 40:
            return 'Average'
        else:
            return 'Low'

    test_users['Spending_Score_Category'] = test_users['Spending_Score'].apply(spending_score_category)

    # Assume scoring functions imported or defined here
    for idx, user in test_users.iterrows():
        print(f"User {idx} scores:")
        print(f"  Fashion: {score_fashion(user)}")
        print(f"  Tech: {score_tech(user)}")
        print(f"  Home & Decor: {score_home(user)}")
        print(f"  Budget: {score_budget(user)}")
        print('---')

if __name__ == '__main__':
    test_scoring_functions()
