from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin


database = SQLAlchemy()


class User(UserMixin, database.Model):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(1000), nullable=False)
    
    def __init__(self, username, hashed_password):
        self.username = username
        self.hashed_password = hashed_password
    
    def __repr__(self):
        return f'{self.id}: {self.username}, {self.hashed_password}'
