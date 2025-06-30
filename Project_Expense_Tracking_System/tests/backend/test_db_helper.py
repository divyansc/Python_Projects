from backend import db_helper


def test_fetch__expenses_for_date():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expenses)==1 #since we only have one record in db
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]['notes'] == "Bought potatoes"

def test_fetch__expenses_for_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9929-08-20")

    assert len(expenses) == 0

def test_fetch_expense_summary_invalid_range():
    summary = db_helper.fetch_expense_summary("9992-08-01","2999-08-05")

    assert len(summary) ==0



