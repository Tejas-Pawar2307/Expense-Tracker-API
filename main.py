from fastapi import FastAPI
from app.utils.db import Base , engine
from fastapi import APIRouter
from app.Expense.router import data_route
from app.user.router import user_routes

app = FastAPI()

app.include_router(data_route)
app.include_router(user_routes) 

Base.metadata.create_all(engine)