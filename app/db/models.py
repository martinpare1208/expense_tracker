from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

database = SQLAlchemy()


class User(database.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)




