import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://fqtkemerxaamnr:a50ea567ed6f24f9bfba2bd6071729d195df57a82c3bcc0ffcf07a176916d2d7@ec2-54-217-249-103.eu-west-1.compute.amazonaws.com:5432/d83g723rkf2r2o'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://fqtkemerxaamnr:a50ea567ed6f24f9bfba2bd6071729d195df57a82c3bcc0ffcf07a176916d2d7@ec2-54-217-249-103.eu-west-1.compute.amazonaws.com:5432/d83g723rkf2r2o'


class DevelopmentConfig(Config):

    POSTGRES_URL = os.getenv("POSTGRES_URL")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PW = os.getenv("POSTGRES_PW")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = DB_URL

    DEVELOPMENT = True
    DEBUG = True
