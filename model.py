from api_server import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, unique=True)
    nickname = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(20), nullable=False)
    comment = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_id