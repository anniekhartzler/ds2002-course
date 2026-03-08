import os
from pymongo import MongoClient

# Read environment variables
MONGO_URL = os.getenv("MONGODB_ATLAS_URL")
MONGO_USER = os.getenv("MONGODB_ATLAS_USER")
MONGO_PWD = os.getenv("MONGODB_ATLAS_PWD")

def main():
    # Connect to MongoDB Atlas
    client = MongoClient(MONGO_URL, username=MONGO_USER, password=MONGO_PWD)
    
    # Select database and collection
    db = client.bookstore
    authors = db.authors

    # Print total number of authors
    total = authors.count_documents({})
    print(f"Total authors: {total}\n")

    # Print list of authors
    for author in authors.find({}, {"_id": 0, "name": 1, "nationality": 1, "birthday": 1}):
        print(f"Name: {author['name']}, Nationality: {author['nationality']}, Birthday: {author.get('birthday', 'N/A')}")
    
    # Close connection
    client.close()

if __name__ == "__main__":
    main()
