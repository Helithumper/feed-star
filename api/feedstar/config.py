"""Default configuration

Use env var to override
"""
import os

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

VERSION = "0.0.1"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME") or 'admin'
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD") or 'admin'
