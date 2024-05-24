from flask import Flask
from routes import ad_bp

app = Flask(__name__)

# Регистрируем blueprint объявлений
app.register_blueprint(ad_bp)

if __name__ == '__main__':
    app.run(debug=True)