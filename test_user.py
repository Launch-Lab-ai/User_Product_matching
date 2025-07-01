import pandas as pd
from bucket_scoring import calculate_scores
from config import BUCKET_MAPPING, THRESHOLDS

def validate_user(user_data):
    """Ensure test user has all required fields"""
    required = ['Age','Gender','Profession','Spending_Score','Quality_Score',
               'Ever_Married','Family_Size','ID']
    missing = [field for field in required if field not in user_data]
    if missing:
        raise ValueError(f"Missing fields: {missing}")

def test_user_profile(user_profile):
    """Test scoring for a single user profile"""
    validate_user(user_profile)
    test_df = pd.DataFrame([user_profile])
    
    # Initialize all bucket columns
    for bucket in BUCKET_MAPPING.values():
        test_df[bucket] = 0
        
    # Calculate scores
    scored = calculate_scores(test_df)
    
    # Display results
    print("\n🧪 Test Results:")
    print(f"User: {user_profile['ID']} ({user_profile['Age']}yo {user_profile['Gender']} {user_profile['Profession']})")
    
    print("\n📊 Scores:")
    recommendations = []
    for bucket in sorted(BUCKET_MAPPING.values()):
        score = scored[bucket].iloc[0]
        threshold = THRESHOLDS[bucket]
        status = "✅" if score >= threshold else "❌"
        print(f"{status} {bucket:<15}: {score}/5 (Threshold: {threshold})")
        if score >= threshold:
            recommendations.append(bucket)
    
    print("\n💡 Recommended Categories:", recommendations or "None")

if __name__ == "__main__":
    # Sample test cases
    test_users = [
        {
            'ID': "TEST_DOCTOR",
            'Age': 32,
            'Gender': 'Female',
            'Profession': 'Doctor',
            'Spending_Score': 3,
            'Quality_Score': 8,
            'Ever_Married': 'Yes',
            'Family_Size': 2
        },
        {
            'ID': "TEST_SENIOR",
            'Age': 60,
            'Gender': 'Male', 
            'Profession': 'Executive',
            'Spending_Score': 3,
            'Quality_Score': 7,
            'Ever_Married': 'Yes',
            'Family_Size': 4
        }
    ]
    
    for user in test_users:
        test_user_profile(user)
        print("\n" + "="*50)
