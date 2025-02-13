# Todo List Backend (Django REST Framework)

This is the backend API for a simple Todo List application, built using Django REST Framework. It provides RESTful endpoints for managing tasks, allowing for CRUD (Create, Read, Update, Delete) operations. This backend is designed to be used with a frontend application (like the Angular frontend provided separately).

## 🚀 Setup

Follow these steps to set up and run the backend API locally:

### ✅ Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python** (preferably 3.8 or higher) - Download from [python.org](https://www.python.org/).
- **pip** (Python Package Installer) - Usually bundled with Python.

### 📥 Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/will-developer/todo-backend-django
cd todo-backend-django
```

### 📌 Create a Virtual Environment (Recommended)

It's highly recommended to create a virtual environment to isolate project dependencies:

```bash
python -m venv venv  # Create virtual environment
```

### 📦 Install Dependencies

Install the required Python packages:

```bash
python.exe -m pip install --upgrade pip
```

### 📊 Database Migrations

Apply database migrations to set up the database schema:

```bash
python manage.py migrate
```

### 🔑 Create a Superuser (Optional but Recommended)

Create a superuser account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password.

### ▶️ Running the Backend API

To start the Django development server:

```bash
python manage.py runserver
```

The server will start running at: 
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://localhost:8000/](http://localhost:8000/)

## 🔗 Frontend Integration

🚀 **Easily integrate this backend with the Angular frontend!**

The **Todo List Frontend** is available at:
👉 [Todo List Frontend Repository](https://github.com/will-developer/todo-frontend)

To connect the backend with the frontend, ensure the backend server is running and configure the frontend to make API requests to `http://localhost:8000/api/tasks/`.

## 📌 API Endpoints

The backend API provides the following endpoints for managing tasks:

| Method | Endpoint | Description |
|--------|-------------------|----------------------------------|
| **GET** | `/api/tasks/` | Retrieve a list of all tasks |
| **POST** | `/api/tasks/` | Create a new task (JSON: `{title: string, completed: boolean (optional, defaults to false)}`) |
| **GET** | `/api/tasks/{id}/` | Retrieve a specific task by ID |
| **PUT** | `/api/tasks/{id}/` | Update an existing task by ID (JSON with updated fields) |
| **PATCH** | `/api/tasks/{id}/` | Partially update a task by ID |
| **DELETE** | `/api/tasks/{id}/` | Delete a task by ID |

🛠️ **Testing:** Use tools like **curl**, **Postman**, or **Insomnia** to test these API endpoints.

## 🌍 CORS Configuration

CORS is configured in `backend/settings.py` to allow requests from:
- `http://localhost:4200` (Angular frontend)

If your frontend runs on a different origin, update the `CORS_ALLOWED_ORIGINS` setting accordingly.

## ⚙️ Django Admin Panel

Access the Django admin panel at:
- [http://localhost:8000/admin/](http://localhost:8000/admin/)

Login with the superuser credentials to manage tasks via the web interface.

---
