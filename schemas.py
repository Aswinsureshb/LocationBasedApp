from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Float

class LocationsBase(BaseModel):
    LocationID:int
    UserID: int
    Latitude: Decimal
    Longitude: Decimal
    Timestamp: datetime 
    
    class Config:  # Config to allow arbitrary types
        arbitrary_types_allowed = True
    
class Locations(LocationsBase):
    pass
    
class PrivacyBase(BaseModel):
    SettingID: int
    UserID: int
    ShareLocation: bool
    NotifyOnNearbyFriends: bool
    
class Privacy(PrivacyBase):
    pass

class SocialMediaBase(BaseModel):
    AccountID: int
    UserID: int
    Platform: str
    AccountLink: str
    
class SocialMedia(SocialMediaBase):
    pass  

class UsersBase(BaseModel):
    UserID: int
    UserName: str
    Email: str
    PasswordHash: str
    PhoneNumber: str
    LocationPermission: bool
    CreatedAt: datetime
    
class Users(UsersBase):
    pass 
