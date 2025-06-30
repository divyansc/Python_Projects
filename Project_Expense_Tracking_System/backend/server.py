from fastapi import FastAPI, HTTPException, Body
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper

app = FastAPI()


class Expense(BaseModel): #pydantic classes
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    try:
        expenses = db_helper.fetch_expenses_for_date(expense_date)
        if expenses is None:
            raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database.")
        return expenses
    except Exception as e:
        print(f"Error fetching expenses: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching expenses.")


@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense] = Body(...)):
    try:
        db_helper.delete_expense_for_date(expense_date)
        for expense in expenses:
            db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
        return {"message": "Expenses updated successfully"}
    except Exception as e:
        print(f"Error inserting expenses: {e}")
        raise HTTPException(status_code=500, detail="Failed to insert expenses.")

@app.post("/analytics/")
def get_analytics(date_range:DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database")

    total = sum([row['total'] for row in data]) #grand total

    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total !=0 else 0
        breakdown[row['category']] = {
            "total":row['total'],
            "percentage": percentage
        }
    return breakdown

    #  {
    #     "Rent": {"total": 1234,"percentage":32.5},
    #     "Shopping":{"total":2345,"percentage":30}
    # }
    return data