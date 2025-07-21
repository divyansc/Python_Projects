💰 Expense Tracking System
A full-stack application for tracking personal expenses with a clean interface, category-based analytics, and persistent storage.

🔧 Tech Stack
🎯 Backend: FastAPI (Python)
📊 Frontend: Streamlit
🗄️ Database: MySQL
🛠️ Other: Logging, Modular Structure
📁 Project Structure
Project_expense_tracking_system/ ├── backend/ # FastAPI server logic & database interaction │ ├── server.py │ ├── db_helper.py │ └── logging_setup.py ├── database/ │ └── expense_db_creation.sql # MySQL schema ├── frontend/ │ └── app.py # Streamlit interface ├── requirements.txt └── README.md

✨ Features
🧾 Add/Update Tab
Add new expense entries with:
📅 Date
💸 Amount
🏷️ Category
📝 Notes
Edit existing entries
Store data in MySQL
📈 Analytics Tab
Select Start Date and End Date
Visualize:
Total spending by category
Interactive bar chart with Streamlit
⚙️ Setup Instructions
✅ Requirements
Python 3.8+
MySQL Server
🧪 Installation
Clone the repository
git clone https://github.com/yourusername/expense-management-system.git
cd Project_Expense_Tracking_System
Install Dependencies
pip install -r requirements.txt
Set up MySQL database
-- In MySQL:
CREATE DATABASE expense_db;
USE expense_db;

-- Run the SQL file:
source database/expense_db_creation.sql;
Run FastAPI backend
uvicorn backend.server:app --reload
Launch Streamlit frontend
streamlit run frontend/app.py
📸 Screenshots
Add/update tab

img.png

Analytics tab

img_1.png

🧪 Tests
Test cases are located in the tests/ folder.

👩‍💻 Author
Divyanshi Chaurasia

🔗 www.linkedin.com/in/divyanshi-chaurasia 📫 dchaurasia.1011@gmail.com
