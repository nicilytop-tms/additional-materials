from flask import current_app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from les_17.flask_app_second.models.base import Base


def init_db(app):
    engine = create_engine(app.config['DB_URL'])
    app.config['engine'] = engine
    Base.metadata.create_all(engine)


def get_session():
    session = sessionmaker(current_app.config['engine'])
    return session()
