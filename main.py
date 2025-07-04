from flask import Flask, render_template, request # request теперь может быть и не нужен, если вы не используете IP-адрес для других целей

app = Flask(__name__)

@app.route('/')
def home():
    # Мы больше не считаем просмотры, поэтому переменная views_count не нужна.
    # Просто рендерим шаблон.
    return render_template('index.html')

if __name__ == '__main__':
    # Этот блок нужен только для локального запуска.
    # Vercel будет запускать ваше приложение через gunicorn, используя переменную `app`.
    app.run(host='0.0.0.0', port=5000, debug=True)
