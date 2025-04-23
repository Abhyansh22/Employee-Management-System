👨‍💼 Employee Management System (Python + MySQL)
A console-based Employee Management System built with Python and MySQL that allows employee registration, performance tracking, data updates, and more through an interactive terminal menu.

📋 Features
🔐 User registration and login system

👤 Employee record management (CRUD operations)

📈 Performance and work experience tracking

📊 View and update employee details

🧠 Interactive command-line interface

🗃️ MySQL backend for persistent data storage

🛠️ Technologies Used
Python 3

MySQL (via mysql-connector-python)

📂 Project Structure
employee-management-system/
<br>
├── loginproj.py           # Handles login/registration and database setup
<br>
├── comproject.py     # Main menu and core features (employee management)
<br>
├── README.md         # Project documentation

⚙️ Setup Instructions
Prerequisites
Python installed on your machine (version 3.6+ recommended)

MySQL server running locally

Install required Python module:
pip install mysql-connector-python

🚀 How to Run the Project
Start your MySQL Server and ensure it's running on localhost.

Open main.py to initiate the database, tables, and user login/register system:

python loginproj.py
Once logged in, the system imports and runs comproject.py, providing a menu-driven interface for managing employees.

🔐 Login & Registration
Upon running loginproj.py, you will be prompted to register or login.

Credentials are stored in the login table.

On successful login, users access the full employee management features.

📋 Menu Options (in comproject.py)

Option	Description
1	Register new employee
2	View all employee details
3	Update employee info (name, department, salary, age)
4	Display list of employees (alphabetical order)
5	Add work experience and performance details
6	View employee performance & experience
7	Exit program

🧾 Sample Employee Table Schema

Employee_Docs
Employee_Id        BIGINT (Primary Key)
Employee_Name      VARCHAR(255)
Employee_Department VARCHAR(255)
Employee_Salary    INT
Employee_Age       INT

Employee_Stats
Employee_Id         BIGINT (Primary Key)
Employee_Name       VARCHAR(255)
Employee_Department VARCHAR(255)
Employee_Performance VARCHAR(255)
em_Work            VARCHAR(255)

⚠️ Important Notes
Ensure the MySQL server is running and credentials in the code (user='root', passwd='@dmin123') match your local setup.

✅ Future Improvements
Implement better security (e.g., password hashing)

Use parameterized queries to prevent SQL injection

Add GUI (Tkinter or Flask/Django)

Add admin and user role separation.
