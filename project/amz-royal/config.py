import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # You can change this to a real database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
