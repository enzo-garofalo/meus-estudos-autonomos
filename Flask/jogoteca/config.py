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