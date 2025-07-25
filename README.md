# ☕ Coffee Shop - Django Web Application

A modern, multilingual coffee shop application built with Django. This project features robust product management, secure user authentication, order processing, and is ready for production deployment.

## ⭐ Key Features

-   **Product Management**: Add, view, and edit products. The edit functionality is restricted to administrators.
-   **Secure Authentication**: User registration and login/logout system.
-   **Order Management**: "Add to Cart" functionality for authenticated users.
-   **Multilingual Support (i18n)**: Interface available in Spanish, English, and French, with a language switcher.
-   **Static File Serving with WhiteNoise**: Optimized configuration for serving static assets in production.
-   **Enhanced Security**:
    -   HTTPS enforced in production environments.
    -   Secure cookies and security headers (CSRF, XSS, etc.).
    -   Backend-level protection for edit views, accessible only by superusers.

## 🛠️ Tech Stack

-   **Backend**: Django, Django REST Framework
-   **Frontend**: HTML, Tailwind CSS
-   **Database**: PostgreSQL (production), SQLite (development)
-   **Static File Server**: WhiteNoise
-   **Deployment**: Gunicorn
-   **Forms**: Crispy Forms with Tailwind CSS

## 🚀 Local Development Setup

### Prerequisites

-   Python 3.8 or higher
-   Git

### 1. Clone the Repository

```bash
git clone https://github.com/Moepulido/coffe_shop.git
cd coffe_shop
```

### 2. Create and Activate Virtual Environment

Using a virtual environment is crucial for managing project dependencies.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root (`coffe_shop/.env`) and add the following configuration.

```env
# A strong, unique secret key for Django
SECRET_KEY='django-insecure-your-own-secret-key-here'

# For development with SQLite (recommended to start)
DJANGO_DB_URL='sqlite:///db.sqlite3'

# If you prefer to use PostgreSQL locally
# DJANGO_DB_URL='postgres://USER:PASSWORD@HOST:PORT/NAME'

# Set to False for local development
IS_AWS_ENV=False
```

### 5. Set Up the Database

Run the migrations to create the database schema.

```bash
python manage.py migrate
```

### 6. Create a Superuser

This user will have access to the Django admin panel and will be able to edit products.

```bash
python manage.py createsuperuser
```

### 7. Run the Application

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

## 📦 Dependencies

This project relies on several key packages:

-   **Django**: The core web framework.
-   **psycopg2-binary**: PostgreSQL adapter for Python.
-   **gunicorn**: WSGI HTTP Server for UNIX.
-   **whitenoise**: Simplified static file serving for Django.
-   **django-crispy-forms**: Advanced form rendering.
-   **crispy-tailwind**: Tailwind CSS template pack for Crispy Forms.
-   **djangorestframework**: Powerful framework for building Web APIs.
-   **django-environ**: Helps manage environment variables.

For a complete list, see the `requirements.txt` file.

## 🛡️ Security Considerations

-   **DEBUG Mode**: The `DEBUG` setting is automatically disabled in production environments by checking the `IS_AWS_ENV` variable.
-   **HTTPS**: The application is configured to enforce HTTPS, secure cookies, and security headers in production.
-   **Protected Views**: Critical views, such as product editing, are protected to ensure they are only accessible to superusers.

Thank you for checking out the project!

## 📜 License

This project is licensed under the MIT License.
