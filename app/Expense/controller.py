from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.Expense.models import ExpenseModel
from app.Expense.dtos import ExpenseCreateDTO


def create_expense(db: Session, expense_data: ExpenseCreateDTO, user_id: int):
    new_expense = ExpenseModel(
        user_id=user_id,
        title=expense_data.title,
        amount=expense_data.amount,
        category=expense_data.category
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


def get_all_data(db: Session, user_id: int):
    return db.query(ExpenseModel).filter(ExpenseModel.user_id == user_id).all()


def get_one_data(data_id: int, db: Session):
    one_data = db.query(ExpenseModel).filter(ExpenseModel.id == data_id).first()
    if not one_data:
        raise HTTPException(status_code=404, detail="Data id is incorrect")
    return one_data


def update_data(expense_data: ExpenseCreateDTO, data_id: int, db: Session):
    one_data = db.query(ExpenseModel).filter(ExpenseModel.id == data_id).first()
    if not one_data:
        raise HTTPException(status_code=404, detail="Data id is incorrect")

    one_data.title = expense_data.title
    one_data.amount = expense_data.amount
    one_data.category = expense_data.category

    db.commit()
    db.refresh(one_data)
    return one_data


def delete_data(data_id: int, db: Session):
    one_data = db.query(ExpenseModel).filter(ExpenseModel.id == data_id).first()
    if not one_data:
        raise HTTPException(status_code=404, detail="Data id is incorrect")

    db.delete(one_data)
    db.commit()
    return {"message": "Deleted successfully"}