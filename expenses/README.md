# 💰 Expense Tracker Backend

Backend API for the Expense Tracker application built using Django and Django REST Framework.  
Handles authentication, expense management, and AI-powered expense insights.

## 🚀 Features

- JWT Authentication
- Expense CRUD APIs
- AI-generated expense overview
- RESTful API architecture
- Secure backend configuration
- CORS enabled for frontend integration

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Simple JWT
- Google Gemini API

## 📂 Project Setup

### Clone the Repository

```bash
git clone https://github.com/nishana-codes/expense-tracker-backend.git

cd expense-tracker-backend
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
⚙️ Environment Variables

Create a .env file in the project root:

SECRET_KEY=your_secret_key

DEBUG=True

GEMINI_API_KEY=your_gemini_api_key
▶️ Run the Server
python manage.py migrate

python manage.py runserver

Server runs at:

http://127.0.0.1:8000/
🔗 API Endpoints
Endpoint	Description
/api/token/	Login API
/api/token/refresh/	Refresh JWT token
/api/expense/list/	Get expenses
/api/expense/create/	Create expense
/api/expense/ai-overview/	AI expense summary
🌐 Frontend Repository

Frontend:
https://github.com/nishana-codes/expense-tracker-frontend

👨‍💻 Author

Developed by Nishana