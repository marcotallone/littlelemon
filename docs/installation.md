# Installation Guide

<div align="center">
  <p>
    <a href="index.md">← Documentation Index</a> ·
    <a href="../README.md">← README</a>
  </p>
</div>

---

## Prerequisites

Before setting up this project, ensure you have the following installed:

| Requirement | Version | Notes |
|-------------|---------|-------|
| **Python** | 3.10+ | [python.org](https://www.python.org/downloads/) |
| **MySQL** | 8.0+ | [mysql.com](https://dev.mysql.com/downloads/mysql/) |
| **pip** | Latest | Comes with Python |
| **Git** | Any | For cloning the repo |

Verify your installations:

```bash
python3 --version
mysql --version
git --version
```

---

## Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd littlelemon
```

---

## Step 2: Create a Virtual Environment

```bash
python3 -m venv workspace
source workspace/bin/activate        # macOS / Linux
# workspace\Scripts\activate         # Windows
```

Your prompt should now show `(workspace)`.

---

## Step 3: Install Python Dependencies

Install all required packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Alternatively, install packages individually:

```bash
pip install django djangorestframework djoser mysqlclient
```

> **macOS note:** If `mysqlclient` fails to install, you may need Homebrew's MySQL development headers:
> ```bash
> brew install mysql
> pip install -r requirements.txt
> ```

### What's in requirements.txt

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 6.1.2 | Web framework |
| djangorestframework | 3.18.3 | REST API toolkit |
| djoser | 2.3.5 | User authentication endpoints |
| mysqlclient | 2.3.0 | MySQL database driver |
| python-dotenv | 1.0.1 | Environment variable management |

---

## Step 4: Create the MySQL Database

Start the MySQL shell and create the database:

```bash
mysql -u root -p
```

```sql
CREATE DATABASE LittleLemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

---

## Step 5: Configure Database Credentials

Open `LittleLemon/settings.py` and update the `DATABASES` section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',
        'USER': 'your_mysql_user',       # e.g. 'root'
        'PASSWORD': 'your_password',     # your MySQL password
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

### Environment Variables (recommended)

For production or shared repositories, avoid storing credentials in `settings.py`. Use a `.env` file instead:

1. Install `python-dotenv`:
   ```bash
   pip install python-dotenv
   ```

2. Create a `.env` file at the project root (it is already gitignored):
   ```
   DB_USER=root
   DB_PASSWORD=your_password
   DJANGO_SECRET_KEY=your-secret-key
   ```

3. Load in `settings.py`:
   ```python
   from dotenv import load_dotenv
   import os
   load_dotenv()

   SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
   DATABASES['default']['USER'] = os.environ.get('DB_USER')
   DATABASES['default']['PASSWORD'] = os.environ.get('DB_PASSWORD')
   ```

---

## Step 6: Run Migrations

```bash
python manage.py migrate
```

This creates all required tables in the `LittleLemon` database, including:
- Django auth tables (`auth_user`, `auth_token`, etc.)
- `restaurant_menu`
- `restaurant_booking`

---

## Step 7: Create a Superuser

A superuser account is needed for the Django admin panel and for generating auth tokens during testing:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

---

## Step 8: Start the Development Server

```bash
python manage.py runserver
```

Open your browser and verify:

| URL | Expected Result |
|-----|-----------------|
| `http://127.0.0.1:8000/restaurant/` | Little Lemon homepage |
| `http://127.0.0.1:8000/admin/` | Django admin login |
| `http://127.0.0.1:8000/restaurant/menu/` | Menu API (JSON response) |

---

## Optional: Load Sample Data

To populate the database with sample records for testing:

```bash
python manage.py shell
```

```python
from restaurant.models import Menu, Booking
from datetime import datetime

Menu.objects.bulk_create([
    Menu(title="Bruschetta", price=7.99, inventory=30),
    Menu(title="Greek Salad", price=10.99, inventory=25),
    Menu(title="Grilled Fish", price=18.99, inventory=15),
    Menu(title="Pasta Carbonara", price=14.99, inventory=20),
    Menu(title="Lemon Dessert", price=6.99, inventory=40),
])

Booking.objects.create(name="Alice", no_of_guests=2, booking_date=datetime(2026, 12, 1, 19, 0))
Booking.objects.create(name="Bob",   no_of_guests=4, booking_date=datetime(2026, 12, 2, 20, 0))
exit()
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `django.db.OperationalError: (2002, ...)` | MySQL is not running. Start it with `brew services start mysql` or `sudo service mysql start` |
| `mysqlclient` install fails | Install MySQL dev headers: `brew install mysql` (macOS) or `sudo apt install libmysqlclient-dev` (Debian/Ubuntu) |
| `django.core.exceptions.ImproperlyConfigured` on migrate | Check database name, user, and password in `settings.py` |
| Port 8000 already in use | Use `python manage.py runserver 8001` |
