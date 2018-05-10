from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # pylint: disable=E1101
    username = db.Column(db.String(80), unique=True, nullable=False) # pylint: disable=E1101
    email = db.Column(db.String(120), unique=True, nullable=False) # pylint: disable=E1101
    company = db.Column(db.String(120), unique=True, nullable=False) # pylint: disable=E1101
    password = db.Column(db.String(120), unique=True, nullable=False) # pylint: disable=E1101

    def __repr__(self):
        return '<User %r>' % self.username

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True) # pylint: disable=E1101
    username = db.Column(db.String(80), unique=True, nullable=False) # pylint: disable=E1101
    company = db.Column(db.String(120), unique=True, nullable=False) # pylint: disable=E1101
    password = db.Column(db.String(120), unique=True, nullable=False) # pylint: disable=E1101

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()