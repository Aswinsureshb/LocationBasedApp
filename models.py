
from datetime import datetime
from database import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String,ForeignKey
from decimal import Decimal


class Locations(Base):
    __tablename__ = "Locations"
    LocationID = Column(Integer, primary_key=True,index=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    Latitude = Column(Numeric(9, 6))  # Use Numeric instead of Decimal
    Longitude = Column(Numeric(9, 6))  # Use Numeric instead of Decimal
    Timestamp = Column(DateTime, default=datetime.utcnow) 

class Privacy(Base):
    __tablename__ = "PrivacySettings"
    SettingID = Column(Integer, primary_key=True,index=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    ShareLocation = Column(Boolean)
    NotifyOnNearbyFriends = Column(Boolean)
    
class SocialMedia(Base):
    __tablename__ = "SocialMediaAccounts"
    AccountID = Column(Integer, primary_key=True,index=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    Platform = Column(String(50))
    AccountLink = Column(String(255))
    
class User(Base):
    __tablename__ = "Users"
    UserID = Column(Integer,primary_key=True,index=True)
    UserName = Column(String(100))
    Email = Column(String(100))
    PasswordHash = Column(String(255))
    PhoneNumber = Column(String(15))
    LocationPermission = Column(Boolean)
    CreatedAt = Column(DateTime, default=datetime.utcnow)