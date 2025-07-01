import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

USER_DATA = os.path.join(DATA_DIR, 'customer_data.csv')
PRODUCT_DATA = os.path.join(DATA_DIR, 'flipkart_buckets_single_label.csv')
SATISFACTION_DATA = os.path.join(DATA_DIR, 'customer_feedback_satisfaction.csv')

BUCKET_MAPPING = {
    "Clothing": "Fashion",
    "Jewelry": "Luxury",
    "Tech & Gadgets": "Tech",
    "Home & Decor": "Home",
    "Furniture & Fixtures": "Furniture",
    "Footwear": "Footwear",
    "Auto & Industrial": "Auto",
    "Books & Media": "Media",
    "Beauty & Personal Care": "Beauty",
    "Gifts & Collectibles": "Gifts",
    "Uncategorized": "Other"
}

THRESHOLDS = {
    'Fashion': 3,
    'Luxury': 4,
    'Tech': 4,
    'Home': 3,
    'Furniture': 3,
    'Footwear': 2,
    'Auto': 3,
    'Media': 2,
    'Beauty': 3,
    'Gifts': 2,
    'Other': 1
}
