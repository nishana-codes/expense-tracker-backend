# 💰 Expense Tracker Backend

Backend API for the Expense Tracker application built using Django and Django REST Framework.

## 🚀 Features

- JWT Authentication
- Expense CRUD APIs
- AI-powered expense overview
- REST API architecture
- CORS enabled
- Secure backend setup

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Simple JWT
- Google Gemini API

## 📂 Clone Repository

```bash
git clone https://github.com/nishana-codes/expense-tracker-backend.git

cd expense-tracker-backend
⚙️ Create Virtual Environment
Windows
python -m venv venv

venv\Scripts\activate
Linux / Mac
python3 -m venv venv

source venv/bin/activate
📦 Install Dependencies
pip install -r requirements.txt
🌐 Environment Variables

Create a .env file in the root directory:

SECRET_KEY=your_secret_key

DEBUG=True

GEMINI_API_KEY=your_gemini_api_key
▶️ Run Server
python manage.py migrate

python manage.py runserver

Server URL:

http://127.0.0.1:8000/
🔗 API Endpoints
Endpoint	Method	Description
/api/token/	POST	User login
/api/token/refresh/	POST	Refresh token
/api/expense/list/	GET	Get all expenses
/api/expense/create/	POST	Create expense
/api/expense/ai-overview/	GET	AI expense analysis
🌐 Frontend Repository

Frontend GitHub Repo:

https://github.com/nishana-codes/expense-tracker-frontend

👨‍💻 Author

Developed by Nishana
