from database import Base, engine,get_db
from fastapi import FastAPI,Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import schemas,crud
#setup the database
Base.metadata.create_all(bind = engine)

#setup fastapi

app= FastAPI()

# CORS Configuration
origins = ["*"]  # Modify this list according to your requirements
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/user/{user_id}", response_model=schemas.Users)
async def read_user(user_id:int, db:Session=Depends(get_db)):
    db_user = crud.get_user(db=db, user_id = user_id)
    return db_user

@app.get("/user/social_media/{user_id}", response_model=schemas.SocialMedia)
async def read_social_media(user_id: int, db: Session = Depends(get_db)):
    db_social_media = crud.get_social_media_account(db=db, user_id=user_id)
    
    # You might want to handle the case when the user has no social media account
    if db_social_media is None:
        raise HTTPException(status_code=404, detail="Social media account not found")
    
    return db_social_media


@app.post("/users/create", response_model=schemas.Users)
async def create_user_endpoint(user_data: schemas.Users, db: Session = Depends(get_db)):
    # Only allow 0 or 1 for LocationPermission
    if user_data.LocationPermission not in [0, 1]:
        raise HTTPException(status_code=400, detail="LocationPermission must be either 0 or 1.")
    
    # Call the CRUD function to create the user
    created_user = crud.create_user(db=db, user_data=user_data)
    
    return created_user