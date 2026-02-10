# School Admin Dashboard  
**Django CRUD Activity – Lorraine**

A simple Django web application for managing Students, Courses, and Teachers with full Create, Read, Update, Delete (CRUD) functionality.  
Built using Django + Django REST Framework (DRF) as per the class activity.

## Features
- Clean admin-style dashboard (no login/register required)
- Responsive Bootstrap 5 design (mobile + desktop)
- Students: auto-generated sequential ID (1, 2, 3, …) – hidden from form
- Courses: one teacher per course (dropdown shows only available teachers)
- Teachers: list shows the specific assigned course(s)
- Dashboard with quick counts
- Poppins font for clean look

## Quick Start – How to Run After Downloading

### 1. Folder Setup
- Download the source code (ZIP from GitHub or wherever shared)
- Extract **all files** into a folder named exactly **`lorraine`**

Your folder should contain (among others):

lorraine/
├── manage.py
├── lorraine/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── school/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── ...
├── requirements.txt
└── README.md               ← this file






### 2. Open Terminal/Command Prompt in the "lorraine" folder
- Windows: Right-click inside the folder → "Open in Terminal" or "PowerShell here"
- Or open CMD/PowerShell and type:
  ```bash
  cd D:\path\to\lorraine



3. (Strongly recommended) Create & activate virtual environment
Bash
python -m venv venv


Activate it:

CMD:Bashvenv\Scripts\activate
PowerShell (if blocked):BashSet-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
venv\Scripts\activate

You’ll see (venv) appear in the prompt.




4. Install dependencies
Bashpip install -r requirements.txt
If the requirements.txt is missing or fails, run:
Bashpip install django==4.2.* djangorestframework==3.14.*
5. Apply database migrations
Bashpython manage.py makemigrations
python manage.py migrate
6. Run the server
Bashpython manage.py runserver
7. Open in browser
Visit:
http://127.0.0.1:8000/
or
http://localhost:8000/
You should see the dashboard immediately.
Navigation

Dashboard
Teachers
Courses
Students

Stopping the server
Press Ctrl + C in the terminal.







