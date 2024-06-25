import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/product_allocation_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
