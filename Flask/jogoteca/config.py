import os

SECRET_KEY = '1234'

# config. para banco de dados
SGBD = 'mysql+mysqlconnector'
usuario = 'ENZODEV'
senha = 1234
servidor = 'localhost'
database = 'jogoteca'


# conexão sqlalchemy (orm) com banco de dados mysql PONTE!!!
SQLALCHEMY_DATABASE_URI = \
  f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'

# __file__ referencia o proprio arquivo, no caso config.py
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'