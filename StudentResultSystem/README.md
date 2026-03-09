# Student Result Management System

The Student Result Management System is a web-based application built using Flask that allows administrators to manage and analyze student academic results efficiently. The system enables the admin to add student marks, automatically calculate total marks, percentage, and grades, and visualize student performance through graphs.

## Features

- Admin Login Authentication
- Add Student Marks
- Automatic Total & Percentage Calculation
- Automatic Grade Assignment (A/B/C/F)
- Student Result Dashboard
- Performance Graph using Chart.js
- Responsive UI using Bootstrap

## Technologies Used

- Python (Flask)
- SQLite Database
- HTML5
- CSS3
- Bootstrap
- Chart.js
- JavaScript

## How to Run the Project

1. Install Flask

pip install flask

2. Create the database

python create_db.py

3. Run the application

python app.py

4. Open in browser

http://127.0.0.1:5000

## Project Structure

StudentResultSystem/
│
├── app.py  
├── create_db.py  
├── students.db  
│
└── templates  
    ├── login.html  
    ├── dashboard.html  
    ├── result.html  
    └── index.html
