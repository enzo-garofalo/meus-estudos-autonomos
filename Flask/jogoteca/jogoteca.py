from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Faz o app rodar
app = Flask(__name__)
app.config.from_pyfile('config.py')

# INSTANCIA
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
  app.run(debug=True)