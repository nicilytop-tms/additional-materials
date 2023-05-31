from sqlalchemy import Column, Text, String, Integer
from les_17.flask_app_second.models.base import Base


class Article(Base):
    __tablename__ = 'article'

    id = Column('id', Integer, primary_key=True)
    header = Column('header', String(100), nullable=False)
    content = Column('content', Text(), nullable=False)
