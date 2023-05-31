from sqlalchemy import Column, Text, Integer, ForeignKey
from les_17.flask_app_second.models.base import Base


class Comment(Base):
    __tablename__ = 'comment'

    id = Column('id', Integer, primary_key=True)
    message = Column('message', Text(), nullable=False)
    article_id = Column('article_id', ForeignKey('article.id'), nullable=False)
