# easy_mongodb

`easy_mongodb` — это простой интерфейс для взаимодействия с MongoDB с использованием Python.

## Установка

```bash
pip install easy_mongodb

## Пример использования

from easy_mongodb import EasyMongoDB

# Создаем подключение к базе данных
db = EasyMongoDB('my_database')

# Вставляем данные
db.insert('my_collection', {'name': 'John', 'age': 30})

# Ищем данные
docs = db.find('my_collection', {'name': 'John'})
print(docs)
