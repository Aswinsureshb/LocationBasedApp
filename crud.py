from datetime import datetime
from sqlalchemy.orm import Session
import models
def get_user(db: Session, user_id:int):
    return db.query(models.User).filter(models.User.UserID==user_id).first()

def get_social_media_account(db: Session, user_id: int):
    return db.query(models.SocialMedia).filter(models.SocialMedia.UserID == user_id).first()


