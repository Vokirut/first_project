import os
from dotenv import load_dotenv

def print_author():
    # Загружаем переменные из .env файла
    load_dotenv()
    
    # Читаем значение переменной AUTHOR
    author = os.getenv('AUTHOR')
    
    # Печатаем имя автора
    print(f"Автор проекта: {author}")

# Вызов функции для проверки
if __name__ == "__main__":
    print_author()
    print('Hello from main!')  # Это можно оставить или удалить

print('Hello from main!') 

