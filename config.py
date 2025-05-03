import os

class Config:
    SECRET_KEY = os.urandom(24)  # for session management
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # using SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
