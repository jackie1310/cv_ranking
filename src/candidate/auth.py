# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from fastapi import Depends, HTTPException, status, APIRouter
# from pydantic import BaseModel
# from typing import Optional
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from mongo_db import connectUser

# SECRET_KEY = "nguyenan13102004521462"  # Change this to a secure random key
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 5

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# users_collection = connectUser()

# router = APIRouter()

# class User(BaseModel):
#     username: str

# class UserInDB(User):
#     hashed_password: str

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     username: str

# class UserCreate(BaseModel):
#     email: str
#     username: str
#     password: str

# class UserLogin(BaseModel):
#     email: str
#     password: str

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_user(db, user_email:str):
#     user = db.find_one({"user_email": user_email})
#     if user:
#         return UserInDB(username=user['user_email'], hashed_password=user['hashed_password'])
#     return None

# def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now() + expires_delta
#     else:
#         expire = datetime.now() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# def create_user(user: UserCreate):
#     hashed_password = pwd_context.hash(user.password)
#     users_collection.insert_one({
#         "username": user.username,
#         "user_email": user.email,
#         "hashed_password": hashed_password
#     })
    

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#         # return username
#     except JWTError:
#         raise credentials_exception
#     return token_data

# def authenticate_user(user_email: str, password: str):
#     user = get_user(users_collection, user_email)
#     if user and verify_password(password, user.hashed_password):
#         return user
#     return None
    
# @router.post("/login", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}

# @router.post("/signup", response_model=User)
# async def signup(user: UserCreate):
#     if users_collection.find_one({"user_email": user.email}):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Username already registered"
#         )
#     create_user(user)
#     return User(username=user.email)

# @router.get("/users/me", response_model=User)
# async def read_users_me(current_user: TokenData = Depends(get_current_user)):
#     return current_user