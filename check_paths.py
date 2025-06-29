from config import USER_DATA, PRODUCT_DATA, SATISFACTION_DATA
import os

print("🔍 Path Verification:")
for name, path in [('User Data', USER_DATA), 
                  ('Product Data', PRODUCT_DATA),
                  ('Satisfaction Data', SATISFACTION_DATA)]:
    exists = os.path.exists(path)
    print(f"{'✅' if exists else '❌'} {name}: {path}")
    if not exists:
        print(f"    Current dir: {os.getcwd()}")