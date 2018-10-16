import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False

    POSTGRES_URL = os.getenv("POSTGRES_URL")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PW = os.getenv("POSTGRES_PW")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = DB_URL

    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://tijfaqdwktvysr:ca612cfb6b6e135efe0509e585a343b6fa5bc28fe0cf3b1714ce0306f1c607fe@ec2-46-137-75-170.eu-west-1.compute.amazonaws.com:5432/d50tcej9hcois8'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://tijfaqdwktvysr:ca612cfb6b6e135efe0509e585a343b6fa5bc28fe0cf3b1714ce0306f1c607fe@ec2-46-137-75-170.eu-west-1.compute.amazonaws.com:5432/d50tcej9hcois8'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
