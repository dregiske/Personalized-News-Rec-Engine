from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime

# 1) Create the Base class — all ORM classes will inherit from this
Base = declarative_base()

# 2) Define your tables as Python classes:
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String(512), nullable=False)
    content = Column(Text)
    source = Column(String(255))
    publish_date = Column(DateTime)
    keywords = Column(String(512))

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    event_type = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
