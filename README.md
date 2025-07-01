# **User Preference Bucketing System**  

**Automated User Segmentation for Personalized Recommendations**  

This system processes user data, scores their interests across different product categories, and assigns them to optimized recommendation buckets (e.g., "Fashion Lovers," "Tech Enthusiasts"). Perfect for marketing personalization and product targeting.

---

## **📖 How It Works**  

The system follows a clear pipeline to transform raw data into actionable insights:

### **Data Processing Pipeline**
1. **`preprocessing.py`**  
   - 📂 Loads raw customer data from `customer_data.csv`  
   - 🧹 Cleans and normalizes user profiles (age, gender, profession)  
   - 🏷️ Categorizes product preferences into standardized groups  
   - 💾 Outputs cleaned data to `data/cleaned_users.csv`  

2. **`bucket_scoring.py`**  
   - 🔢 Calculates weighted interest scores across categories  
   - ✅ Applies smart thresholds to identify significant preferences  
   - 📊 Generates final recommendation buckets for each user  

3. **`test_user.py`** *(Validation Tool)*  
   - 🧪 Tests system with sample user profiles  
   - ✔️/❌ Clearly shows passing/failing categories  
   - 💡 Provides instant recommendation feedback  

4. **`quick_check.py`** *(Analytics Dashboard)*  
   - 📈 Shows category distribution and popularity  
   - 👥 Reveals demographic trends per bucket  
   - 🔍 Offers quick insights into user segments  

---

## **🚀 Quick Start Guide**  

### **1. Installation**  
```bash
pip install pandas numpy  # Core dependencies
```

### **2. Run the Pipeline**  
```bash
# Standard processing flow:
python preprocessing.py      # Clean the data
python bucket_scoring.py     # Generate recommendations
python quick_check.py       # View analytics

# Test specific users:
python test_user.py         # Verify recommendations
```

### **3. Configuration**  
- Adjust scoring thresholds in `bucket_scoring.py`  
- Modify test users in `test_user.py`  
