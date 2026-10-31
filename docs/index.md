# Little Lemon API Documentation

<div align="center">
  <p>
    <a href="../README.md">← Back to README</a>
  </p>
</div>

---

Welcome to the full documentation for the **Little Lemon Restaurant API**. Use the table below to navigate to the section you need.

## Contents

<table>
  <tr>
    <td>
      <h3><a href="installation.md">⚙️ Installation Guide</a></h3>
      <p>Full prerequisites, step-by-step MySQL setup, Django configuration, migrations, and superuser creation. Start here if you're setting up the project for the first time.</p>
    </td>
    <td>
      <h3><a href="api-reference.md">🔌 API Reference</a></h3>
      <p>Complete documentation for every API endpoint: request formats, response bodies, status codes, and authentication details.</p>
    </td>
  </tr>
  <tr>
    <td>
      <h3><a href="testing.md">🧪 Testing Guide</a></h3>
      <p>Instructions for running the 13 automated unit tests, plus a step-by-step walkthrough for manual API testing with the Insomnia REST client.</p>
    </td>
    <td>
      <h3><a href="../README.md">🏠 Main README</a></h3>
      <p>Project overview, feature summary, tech stack, quick-start setup, and API quick reference table.</p>
    </td>
  </tr>
</table>

---

## Project Overview

The Little Lemon Restaurant API is a Django REST Framework backend that provides:

| Component | Description |
|-----------|-------------|
| **Static homepage** | Django template served at `/restaurant/` |
| **Menu API** | Public CRUD endpoints for managing menu items |
| **Booking API** | Token-protected CRUD endpoints for table reservations |
| **Auth system** | Registration, login, and logout via Djoser |
| **Admin panel** | Django admin at `/admin/` |
| **Unit tests** | 13 automated tests across models and views |

## Technology Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Language | Python | 3.14 |
| Web framework | Django | 6.1.2 |
| REST API layer | Django REST Framework | 3.18.3 |
| Authentication | Djoser | 2.3.5 |
| Database driver | mysqlclient | 2.3.0 |
| Database | MySQL | 9.7 |

## Project Structure

```
littlelemon/
├── LittleLemon/             # Django project package
│   ├── settings.py          # App config, database, auth
│   └── urls.py              # Root URL routing
├── restaurant/              # Main app
│   ├── models.py            # Menu and Booking models
│   ├── views.py             # API view classes
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # App-level URL routes
│   └── admin.py             # Admin registration
├── templates/
│   └── index.html           # Static homepage template
├── tests/
│   ├── test_models.py       # Model unit tests
│   └── test_views.py        # View/API unit tests
├── docs/                    # This documentation folder
├── README.md
└── manage.py
```
