# Little Lemon Restaurant API Reference

## Overview

This is a complete REST API for managing menu items and table bookings with user authentication.

## Base URL

```
http://localhost:8000
```

---

## Authentication

### Register a New User

**Endpoint:** `POST /auth/users/`

**Request:**

```json
{
  "username": "newuser",
  "password": "securepassword123"
}
```

**Response (201 Created):**

```json
{
  "email": "",
  "username": "newuser"
}
```

### Login & Get Token

**Endpoint:** `POST /auth/token/login/`

**Request:**

```json
{
  "username": "newuser",
  "password": "securepassword123"
}
```

**Response (200 OK):**

```json
{
  "auth_token": "24cafce3a155741819cd826acfa4950271867d22"
}
```

### Logout

**Endpoint:** `POST /auth/token/logout/`

**Headers:**

```
Authorization: Token <your_auth_token>
```

**Response (204 No Content)**

---

## Menu API (Public - No Authentication Required)

### List All Menu Items

**Endpoint:** `GET /restaurant/menu/`

**Response (200 OK):**

```json
[
  {
    "id": 1,
    "title": "Grilled Fish",
    "price": "14.99",
    "inventory": 25
  },
  {
    "id": 2,
    "title": "Bruschetta",
    "price": "8.50",
    "inventory": 30
  }
]
```

### Create Menu Item

**Endpoint:** `POST /restaurant/menu/`

**Request:**

```json
{
  "title": "New Dish",
  "price": "12.99",
  "inventory": 20
}
```

**Response (201 Created):**

```json
{
  "id": 7,
  "title": "New Dish",
  "price": "12.99",
  "inventory": 20
}
```

### Get Single Menu Item

**Endpoint:** `GET /restaurant/menu/<id>/`

**Response (200 OK):**

```json
{
  "id": 1,
  "title": "Grilled Fish",
  "price": "14.99",
  "inventory": 25
}
```

### Update Menu Item

**Endpoint:** `PUT /restaurant/menu/<id>/`

**Request:**

```json
{
  "title": "Grilled Fish",
  "price": "15.99",
  "inventory": 30
}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "title": "Grilled Fish",
  "price": "15.99",
  "inventory": 30
}
```

### Delete Menu Item

**Endpoint:** `DELETE /restaurant/menu/<id>/`

**Response (204 No Content)**

---

## Table Booking API (Protected - Requires Authentication)

### List All Bookings

**Endpoint:** `GET /restaurant/booking/tables/`

**Headers:**

```
Authorization: Token <your_auth_token>
```

**Response (200 OK):**

```json
[
  {
    "id": 1,
    "name": "John Smith",
    "no_of_guests": 4,
    "booking_date": "2026-11-07T19:00:00Z"
  },
  {
    "id": 2,
    "name": "Maria Garcia",
    "no_of_guests": 2,
    "booking_date": "2026-11-08T20:30:00Z"
  }
]
```

### Create Booking

**Endpoint:** `POST /restaurant/booking/tables/`

**Headers:**

```
Authorization: Token <your_auth_token>
Content-Type: application/json
```

**Request:**

```json
{
  "name": "Alice Brown",
  "no_of_guests": 5,
  "booking_date": "2026-11-15T19:00:00Z"
}
```

**Response (201 Created):**

```json
{
  "id": 6,
  "name": "Alice Brown",
  "no_of_guests": 5,
  "booking_date": "2026-11-15T19:00:00Z"
}
```

### Get Single Booking

**Endpoint:** `GET /restaurant/booking/tables/<id>/`

**Headers:**

```
Authorization: Token <your_auth_token>
```

**Response (200 OK):**

```json
{
  "id": 1,
  "name": "John Smith",
  "no_of_guests": 4,
  "booking_date": "2026-11-07T19:00:00Z"
}
```

### Update Booking

**Endpoint:** `PUT /restaurant/booking/tables/<id>/`

**Headers:**

```
Authorization: Token <your_auth_token>
Content-Type: application/json
```

**Request:**

```json
{
  "name": "John Smith",
  "no_of_guests": 6,
  "booking_date": "2026-11-07T19:00:00Z"
}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "name": "John Smith",
  "no_of_guests": 6,
  "booking_date": "2026-11-07T19:00:00Z"
}
```

### Delete Booking

**Endpoint:** `DELETE /restaurant/booking/tables/<id>/`

**Headers:**

```
Authorization: Token <your_auth_token>
```

**Response (204 No Content)**

---

## Error Responses

### 401 Unauthorized (Missing Token)

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 401 Unauthorized (Invalid Token)

```json
{
  "detail": "Invalid token."
}
```

### 404 Not Found

```json
{
  "detail": "Not found."
}
```

---

## Testing with cURL

### Register User

```bash
curl -X POST http://localhost:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

### Login

```bash
curl -X POST http://localhost:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

### Get Bookings (with token)

```bash
curl -H "Authorization: Token YOUR_TOKEN" \
  http://localhost:8000/restaurant/booking/tables/
```

### Create Booking

```bash
curl -X POST http://localhost:8000/restaurant/booking/tables/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{"name":"Test User","no_of_guests":4,"booking_date":"2026-11-15T19:00:00Z"}'
```

---

## Technologies Used

- **Django** - Web framework
- **Django REST Framework** - API toolkit
- **Djoser** - Authentication and user management
- **Token Authentication** - Secure API access
- **MySQL** - Database

---

## Security Features

✅ User registration and authentication
✅ Token-based API security
✅ Protected booking endpoints
✅ Public menu endpoints for browsing
✅ Session and token authentication support
