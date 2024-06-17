from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# Faz o app rodar
app = Flask(__name__)
app.config.from_pyfile('config.py')

# INSTANCIA
db = SQLAlchemy(app)
csrf = CSRFProtect(app)


from views_games import *
from views_user import *

if __name__ == '__main__':
  app.run(debug=True)