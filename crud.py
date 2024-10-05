from datetime import datetime
from sqlalchemy.orm import Session
import models
import schemas
def get_user(db: Session, user_id:int):
    return db.query(models.User).filter(models.User.UserID==user_id).first()

def get_social_media_account(db: Session, user_id: int):
    return db.query(models.SocialMedia).filter(models.SocialMedia.UserID == user_id).first()


def create_user(db: Session, user_data: schemas.Users):
    # Create a new user instance using the data from the frontend
    db_user = models.User(
        UserName=user_data.UserName,
        Email=user_data.Email,
        PasswordHash=user_data.PasswordHash,
        PhoneNumber=user_data.PhoneNumber,
        LocationPermission=user_data.LocationPermission,
        CreatedAt=datetime.utcnow(),
    )
    
    # Add and commit the new user to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Refresh to get the latest data from the DB
    
    return db_user