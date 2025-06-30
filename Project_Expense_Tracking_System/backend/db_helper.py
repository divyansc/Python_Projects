from contextlib import contextmanager
import mysql.connector
from logging_setup import logger_setup


logger = logger_setup("db_helper")


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    try:
        with get_db_cursor() as cursor:
            cursor.execute("SELECT amount, category, notes FROM expenses WHERE expense_date = %s", (expense_date,))
            return cursor.fetchall()
    except Exception as e:
        print(f"DB fetch error: {e}")
        return None


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expenses called with expense: {expense_date} amount: {amount} category: {category} notes: {notes}")
    try:
        print(f"Inserting expense: {expense_date}, {amount}, {category}, {notes}")
        with get_db_cursor(commit=True) as cursor:
            cursor.execute(
                "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
                (expense_date, amount, category, notes)
            )
    except Exception as e:
        print(f"DB insert error: {e}")
        raise

def delete_expense_for_date(expense_date):
    logger.info(f"delete_expense_for_date called with {expense_date}")
    try:
        with get_db_cursor(commit=True) as cursor:
            cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))
    except Exception as e:
        print(f"DB delete error: {e}")
        raise

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary_for_date called with start: {start_date} end: {end_date} ")
    try:
        with get_db_cursor() as cursor:
            cursor.execute(
                '''
                SELECT category, SUM(amount) as total
                FROM expenses
                WHERE expense_date BETWEEN %s AND %s
                GROUP BY category
                ''',
                (start_date, end_date)
            )
            return cursor.fetchall()
    except Exception as e:
        print(f"DB summary error: {e}")
        return []

if __name__ == '__main__':
    expenses = fetch_expenses_for_date("2024-08-01")
    print(expenses)
    # insert_expense("2024-08-31",200,"accessories","bought a sunglass")
    summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    for record in summary:
        print(record)

