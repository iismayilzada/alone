
from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Файл для хранения уникальных IP
VISITORS_FILE = 'visitors.json'

def load_visitors():
    if os.path.exists(VISITORS_FILE):
        with open(VISITORS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_visitors(visitors):
    with open(VISITORS_FILE, 'w') as f:
        json.dump(visitors, f)

@app.route('/')
def home():
    # Получаем IP адрес посетителя
    visitor_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    
    # Загружаем список уникальных посетителей
    visitors = load_visitors()
    
    # Если IP новый, добавляем его
    if visitor_ip not in visitors:
        visitors.append(visitor_ip)
        save_visitors(visitors)
    
    # Передаем количество уникальных посетителей в шаблон
    views_count = len(visitors)
    
    return render_template('index.html', views_count=views_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
