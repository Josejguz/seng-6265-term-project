from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017") 
try: 
    db = client['budget_app_test'] 
    print(db.list_collection_names()) 
    print("Connection successful!") 
except Exception as e: 
    print(f"Error: {e}")