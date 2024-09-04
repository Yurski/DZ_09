from pymongo import MongoClient
import json

def upload_to_mongodb():
    client = MongoClient('mongodb://root:example@localhost:27017/')
    db = client['quotes_db']
    
    # Вставка цитат
    with open('quotes.json', 'r') as f:
        quotes = json.load(f)
        db.quotes.insert_many(quotes)

    # Вставка авторів
    with open('authors.json', 'r') as f:
        authors = json.load(f)
        db.authors.insert_many(authors)

if __name__ == "__main__":
    upload_to_mongodb()
