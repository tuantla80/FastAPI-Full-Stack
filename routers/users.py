import sys
sys.path.append('..')

from starlette import status
from starlette.responses import RedirectResponse
from fastapi import Depends, APIRouter,Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic import BaseModel

import models
from database import engine, SessionLocal
from .auth import get_current_user, verify_password


router = APIRouter(
   prefix='/users',
   tags=['users'],
   responses={404: {'description': 'Not found'}}
)

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory='templates')

def get_db():
   try:
      db = SessionLocal()
      yield db
   finally:
      db.close()


class UserVarification(BaseModel):
   username: str
   password: str
   new_password: str


@router.get('/edit-password', responses_class=HTMLResponse)
async def edit_user_view(request: Request):
   pass
