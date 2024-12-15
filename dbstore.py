## 4. Data Storage via Mongo
from pymongo import MongoClient
from datetime import datetime
from typing import List, Dict
import os
from dotenv import load_dotenv
load_dotenv()
# MongoDB Configuration
DATABASE_NAME = "news_data"
COLLECTION_NAME = "articles"

# MongoDB Client Initialization
client = MongoClient(os.getenv('MONGO_URI'))
print(os.getenv('MONGO_URI'))
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def store_article_data(url: str, article_text: str, entities: Dict[str, List[str]], sentiment: str) -> None:
    
    # Prepare the data for storage
    document = {
        "url": url,
        "article_text": article_text,
        "entities": {
            "persons": entities.get("PERSON", []),
            "organizations": entities.get("ORG", [])
        },
        "sentiment": sentiment,
        "timestamp": datetime.utcnow()
    }

    # Insert the document into MongoDB
    result = collection.insert_one(document)
    print(f"Data stored successfully. Document ID: {result.inserted_id}")
