from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_db(app)
    Migrate(app, db)
    return app

app = create_app()

@app.route('/')
def hello_world():
    from model import User
    a = User.query.first()
    return jsonify({
        'id': a.id,
        'name': a.username
    })


if __name__ == '__main__':
    app.run()
