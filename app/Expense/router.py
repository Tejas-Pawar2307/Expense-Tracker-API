from fastapi import APIRouter , Depends
from app.Expense import controller
from app.Expense.dtos import ExpenseCreateDTO
from app.utils.db import get_db
from app.utils.helpers import is_authenticated
from app.user.models import UserModel




data_route = APIRouter(prefix="/data")

@data_route.post("/create")
def create_expense(
    expense_data: ExpenseCreateDTO,
    db = Depends(get_db),
    user: UserModel = Depends(is_authenticated)
):
    return controller.create_expense(db, expense_data, user.id)

@data_route.get("/all_data")
def get_all_data(
    db = Depends(get_db),
    user: UserModel = Depends(is_authenticated)
):
    return controller.get_all_data(db, user.id)

@data_route.get("/get_one/{data_id}")
def get_one_data(
    data_id: int,
    db = Depends(get_db),
    user: UserModel = Depends(is_authenticated)
):
    return controller.get_one_data(data_id, db)



@data_route.put("/put_data/{data_id}")
def update_data(
    expense_data: ExpenseCreateDTO,
    data_id: int,
    db = Depends(get_db),
    user: UserModel = Depends(is_authenticated)
):
    return controller.update_data(expense_data, data_id, db)

@data_route.delete("/delete_data/{data_id}")
def delete_data(
    data_id: int,
    db = Depends(get_db),
    user: UserModel = Depends(is_authenticated)
):
    return controller.delete_data(data_id, db)