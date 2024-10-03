import decimal
from datetime import datetime
from pydantic import BaseModel

class LocationsBase(BaseModel):
    LocationID:int
    UserID: int
    Latitude: decimal
    Longitude: decimal
    Timestamp: datetime 
    
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
