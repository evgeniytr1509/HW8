import json
from pymongo import MongoClient

# Подключение к базе данных Atlas MongoDB
client = MongoClient('mongodb+srv://userweb12:!123456!@cluster1.adkti2c.mongodb.net/')

# Выбор коллекции авторов
authors_collection = client['your_database_name']['authors']

# Загрузка данных авторов из JSON-файла
with open('authors.json') as f:
    authors_data = json.load(f)

# Вставка данных авторов в коллекцию
authors_collection.insert_many(authors_data)

# Выбор коллекции цитат
quotes_collection = client['your_database_name']['quotes']

# Загрузка данных цитат из JSON-файла
with open('quotes.json') as f:
    quotes_data = json.load(f)

# Вставка данных цитат в коллекцию
quotes_collection.insert_many(quotes_data)

# Закрытие подключения к базе данных
client.close()