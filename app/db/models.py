from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, REAL, DateTime, Boolean
from flask_login import UserMixin
from datetime import datetime


database = SQLAlchemy()


class User(UserMixin, database.Model):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(1000), nullable=False)
    
    def __init__(self, username: str, hashed_password: str):
        self.username = username
        self.hashed_password = hashed_password
    
    def __repr__(self):
        return f'{self.id}: {self.username}, {self.hashed_password}'
    
    
    
class Expense(database.Model):
    __tablename__ = "Expense"
    
    e_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('User.id'))
    amount: Mapped[float] = mapped_column(REAL, nullable=False)
    created_date: Mapped[datetime] = mapped_column(DateTime)
    modified_date: Mapped[datetime] = mapped_column(DateTime)
    payment_type: Mapped[str] = mapped_column(String(1000))
    description: Mapped[str] = mapped_column(String(5000))
    location: Mapped[str] = mapped_column(String(1000))
    
    
    def __init__(self, amount: float, payment_type: str, description: str, location: str):
        self.amount = amount
        self.payment_type = payment_type
        self.description = description
        self.location = location

    # Implement later
    def __repr__(self):
        return 
    
    
class CurrencyType:
    __tablename__ = "CurrencyType"
    
    currency_code: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    currency_name: Mapped[str] = mapped_column(String(100), nullable=False)
    country: Mapped[str] = mapped_column(String(1000))
    currency_label: Mapped[str] = mapped_column(String(100))
    
    def __init__(self, currency_code: str, currency_name: str, country: str, currency_label: str):
        
        self.currency_code = currency_code
        self.currency_name = currency_name
        self.country = country
        self.currency_label = currency_label
        
    # Implement later    
    def __repr__(self):
        return 
    
    
class UserSettings:
    __tablename__ =  "UserSettings"
    
    user_id: Mapped[int] = mapped_column(ForeignKey('User.id'))
    isDarkMode: Mapped[bool] = mapped_column(Boolean)
    currency_code: Mapped[str] = mapped_column(ForeignKey('CurrencyType.currency_code'))
    currency_name: Mapped[str] = mapped_column(ForeignKey('CurrencyType.currency_name'))
    
    def __init__(self, user_id: int, isDarkMode: bool, currency_code: str, currency_name: str):
        self.user_id = user_id
        self.isDarkMode = isDarkMode
        self.currency_code = currency_code
        self.currency_name = currency_name
        
    # Implement later
    def __repr__(self):
        return

class ExpenseCategory:
    __tablename__ = "ExpenseCategory"
    
    category_code: Mapped[str] = mapped_column(String(100))
    category_name: Mapped[str] = mapped_column(String(100))
    category_desc: Mapped[str] = mapped_column(String(1000))
    
    def __init__(self, category_code: str, category_name: str, category_desc: str):
        self.category_code = category_code
        self.category_name = category_name
        self.category_desc = category_desc
        
    # Implement later
    def __repr__(self):
        return