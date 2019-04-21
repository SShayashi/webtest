from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify
from flask import request
from sqlalchemy import exc

db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, unique=True)
    password = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(80), nullable=True)
    comment = db.Column(db.String(100), default='')

    def __repr__(self):
        return '<User %r>' % self.user_id

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
app.app_context().push()
db.create_all()

@app.route('/')
def hello_world():
    return 'ok'


def validation(json_data):
    pass
@app.route('/signup', methods=["POST"])
def signup():
    data = request.get_json()
    #validaiton
    user_id = data['user_id']
    password = data['password']
    u = User(user_id=user_id, password=password)
    try:
        db.session.add(u)
        db.session.commit()
        return jsonify({
            "message": "Account successfully created",
            "user": data
        }, 200)
    except Exception as e:
        return jsonify(
            {"message": "Account creation failed",
             "cause": str(e)
             }, 400)


@app.route('/users/<string:user_id>')
def users(user_id):
    user = User.query.filter_by(user_id=user_id).first()

    return 'users'


@app.route('/close')
def close():
    return 'close'

if __name__ == '__main__':
    app.run()
