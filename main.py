'''
Step 1: Access to virtual environment "venv"
   C:\Python\fastapi\FastAPI-Full-Stack> venv\Scripts\activate
   --> (venv) PS C:\Python\fastapi\FastAPI-Full-Stack>
Step 2: Goto other folder if needed
Step 3: run uvicorn
   (venv) C:\Python\fastapi\FastAPI-Full-Stack> uvicorn main:app --reload
Step 4: Access to
   http://127.0.0.1:8000/ or
   http://127.0.0.1:8000/docs
'''

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

import models
from database import engine
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# To import static directory
app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(auth.router)
app.include_router(todos.router)
