from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.sql.operators import exists
from app.forms import UserLoginForm, UserCreateForm
from app.models import connect_db, User
from app.utils import get_password_hash
from starlette import status


router = APIRouter()


@router.post('/login', name='user:login')
def login(user_form: UserLoginForm = Body(..., embed=True),  database=Depends(connect_db)):
    user = database.query(User).filter(User.email ==  user_form.email).one_or_none()
    if not user or get_password_hash(user_form.password) != user.password:
        return {'error': 'Email/password invalid'}
    
    
    database.commit()
    return {'status' : 'ok'}




@router.post('/user', name='user:create')
def create_user(user: UserCreateForm = Body(..., embed=True),  database=Depends(connect_db)):
    exists_user = database.query(User.id).filter(User.email == user.email).one_or_none()
    if exists_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already exists')
    
    new_user = User(
        email=user.email,
        password=get_password_hash(user.password),
        first_name=user.first_name
    )
    database.add(new_user)
    database.commit()
    return {'user_id' : new_user.id}