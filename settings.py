from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate


PG_DSN = 'postgresql://netology:pass@127.0.0.1:5432/flask'
app = Flask('test_app')
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=PG_DSN)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
