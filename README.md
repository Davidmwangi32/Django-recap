# Django_recap
# Django User Registration App

This is a simple Django-based project that allows users to register using a form. It saves user data (name, email, age, and bio) into a database and provides admin management through Django’s built-in admin panel.

## 🔧 Features

- User registration form
- Save user data (name, email, age, bio)
- Admin panel to manage users
- Clean and simple frontend

## 🛠️ Tech Stack

- Python 3
- Django
- SQLite (default Django database)

## 📁 Project Structure

myproject/
├── users/ # App with models, views, forms, templates
├── myproject/ # Main project settings and URLs
├── templates/ # HTML templates
├── db.sqlite3 # Default database
├── manage.py # Django CLI entry point

## 🚀 Setup Instructions

### 1. Clone the repository
git clone https://github.com/Davidmwangi32/Django-recap.git
cd django-registration-app

### 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Apply migrations and run server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

🧑‍💼 Admin Access
To access the Django admin panel:
python manage.py createsuperuser

🙏 Acknowledgements
This project was built as part of a Django hands-on assignment to practice backend development.
