from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

datetime.utcnow()



db = SQLAlchemy()


class User(UserMixin, db.Model):
    """ User model """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    hashed_pswd = db.Column(db.String(), nullable=False)
    messages = db.relationship('ChatMessage', backref='user', lazy=True)
""" Chatroom model dortiz """


class ChatRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    messages = db.relationship('ChatMessage', backref='chat_room', lazy=True)
    
""" ChatMessage model dortiz """
class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    date_sent = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    chat_room_id = db.Column(db.Integer, db.ForeignKey('chat_room.id'), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)