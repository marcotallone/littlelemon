<div align="center">
  <img src="restaurant/static/restaurant/littlelemon.png" alt="Little Lemon Logo" width="180"/>
  <h1>Little Lemon Restaurant API</h1>
  <p><em>Django REST Framework backend for the Little Lemon restaurant management system</em></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/Django-6.1.2-092E20?logo=django&logoColor=white" alt="Django"/>
    <img src="https://img.shields.io/badge/DRF-3.18-A30000" alt="DRF"/>
    <img src="https://img.shields.io/badge/MySQL-9.7-4479A1?logo=mysql&logoColor=white" alt="MySQL"/>
    <img src="https://img.shields.io/badge/Tests-13%20passing-brightgreen" alt="Tests"/>
    <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License"/>
  </p>

  <p>
    <a href="docs/index.md"><strong>📖 Full Docs</strong></a> &nbsp;&nbsp;&nbsp;
    <a href="docs/api-reference.md"><strong>🔌 API Reference</strong></a> &nbsp;&nbsp;&nbsp;
    <a href="docs/testing.md"><strong>🧪 Testing Guide</strong></a> &nbsp;&nbsp;&nbsp;
    <a href="docs/installation.md"><strong>⚙️ Installation</strong></a>
  </p>
</div>

---

## About

A complete Django REST API backend for the **Little Lemon** restaurant, built with Django REST Framework.

The application handles menu management and table bookings, featuring token-based authentication, a MySQL database, and a static HTML homepage, all powered by Django REST Framework.

## Features

- 🌐 **Static homepage** served by Django templates
- 🍽️ **Menu API**: fully public CRUD for restaurant menu items
- 📅 **Table Booking API**: authenticated CRUD, token-protected
- 🔐 **User authentication**: registration, login & token logout via Djoser
- 🗄️ **MySQL** database backend
- ✅ **13 unit tests** covering models and views
- 🛠️ **Django Admin** interface for data management

## Tech Stack

| Layer          | Technology                          |
| -------------- | ----------------------------------- |
| Language       | Python 3.14                         |
| Framework      | Django 6.1.2                        |
| REST API       | Django REST Framework 3.18          |
| Authentication | Djoser 2.3.5 + Token Authentication |
| Database       | MySQL 9.7                           |
| Testing        | Django TestCase + DRF APIClient     |

---

## Getting Started

> See the [full installation guide](docs/installation.md) for a detailed walkthrough.

### Prerequisites

- Python 3.10+
- MySQL 8.0+ running locally
- `mysqlclient` Python package

### Quick Setup

```bash
# 1. Clone the repository
git clone https://github.com/marcotallone/littlelemon.git
cd littlelemon

# 2. Create and activate a virtual environment
python3 -m venv workspace
source workspace/bin/activate        # macOS/Linux
# workspace\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create the MySQL database
mysql -u root -p -e "CREATE DATABASE LittleLemon;"

# 5. Update database credentials in LittleLemon/settings.py (see below)

# 6. Run migrations
python manage.py migrate

# 7. Create a superuser (for admin and testing)
python manage.py createsuperuser

# 8. Start the development server
python manage.py runserver
```

The application will be available at <http://127.0.0.1:8000/restaurant/>. See the [API Quick Reference](#api-quick-reference) for available endpoints.

### Database Configuration

Open `LittleLemon/settings.py` and update the `DATABASES` section with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

> ⚠️ For production use, move credentials to environment variables. See the [installation guide](docs/installation.md#environment-variables).

---

## API Quick Reference

### Public Endpoints (no authentication required)

| Method   | Endpoint                 | Description                 |
| -------- | ------------------------ | --------------------------- |
| `GET`    | `/restaurant/`           | Static homepage             |
| `GET`    | `/restaurant/menu/`      | List all menu items         |
| `POST`   | `/restaurant/menu/`      | Create a new menu item      |
| `GET`    | `/restaurant/menu/{id}/` | Retrieve a single menu item |
| `PUT`    | `/restaurant/menu/{id}/` | Update a menu item          |
| `DELETE` | `/restaurant/menu/{id}/` | Delete a menu item          |

### Authentication Endpoints

| Method | Endpoint              | Description              |
| ------ | --------------------- | ------------------------ |
| `POST` | `/auth/users/`        | Register a new user      |
| `POST` | `/auth/token/login/`  | Obtain an auth token     |
| `POST` | `/auth/token/logout/` | Revoke the current token |

### Protected Endpoints (auth token required)

| Method   | Endpoint                           | Description          |
| -------- | ---------------------------------- | -------------------- |
| `GET`    | `/restaurant/booking/tables/`      | List all bookings    |
| `POST`   | `/restaurant/booking/tables/`      | Create a new booking |
| `GET`    | `/restaurant/booking/tables/{id}/` | Retrieve a booking   |
| `PUT`    | `/restaurant/booking/tables/{id}/` | Update a booking     |
| `DELETE` | `/restaurant/booking/tables/{id}/` | Delete a booking     |

**Add this header to all protected requests:**

```
Authorization: Token <your-token-here>
```

See the [full API reference](docs/api-reference.md) for request/response body examples.

---

## Running Tests

```bash
source workspace/bin/activate
python manage.py test tests -v 2
```

Expected output:

```
Ran 13 tests in ~0.05s
OK
```

Covers: Menu model CRUD, Booking model creation, Menu API (GET/POST/PUT/DELETE), and endpoint availability.
See the [testing guide](docs/testing.md) for Insomnia-based API testing.

---

## Documentation

<table>
  <tr>
    <td align="center">
      <a href="docs/index.md">
        <strong>📋 Documentation Index</strong><br/>
        <sub>Overview and navigation</sub>
      </a>
    </td>
    <td align="center">
      <a href="docs/installation.md">
        <strong>⚙️ Installation Guide</strong><br/>
        <sub>Full setup and configuration</sub>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="docs/api-reference.md">
        <strong>🔌 API Reference</strong><br/>
        <sub>All endpoints with examples</sub>
      </a>
    </td>
    <td align="center">
      <a href="docs/testing.md">
        <strong>🧪 Testing Guide</strong><br/>
        <sub>Unit tests and Insomnia testing</sub>
      </a>
    </td>
  </tr>
</table>

---

## License

This project is licensed under the [MIT License](LICENSE).
