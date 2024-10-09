from flask import Flask
from routes.client_routes import client_bp
from init_db import create_tables

app = Flask(__name__)

create_tables()

app.register_blueprint(client_bp)

@app.route('/')
def index():
    return "Api iniciada com sucesso."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')