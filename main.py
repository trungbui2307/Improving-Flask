from flask import Flask 
from config import Config, DevConfig 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users_table_name'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    
    def __init__(self, username):
        self.username = username 
        
    def __repr__(self):
        return '<User %r>' % self.username
    

@app.route('/')
def home():
    return '<h1>Home</h1>'

if __name__ == '__main__':
    app.run()
    
