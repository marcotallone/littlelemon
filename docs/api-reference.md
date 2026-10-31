# API Reference

<div align="center">
  <p>
    <a href="index.md">← Documentation Index</a> ·
    <a href="../README.md">← README</a>
  </p>
</div>

---

The Little Lemon API exposes three groups of endpoints: the static homepage, the Menu API (public), and the Table Booking API (token-protected), plus Djoser-managed authentication routes.

**Base URL:** `http://127.0.0.1:8000`

---

## Authentication

The Booking API requires a **token authentication header** on every request:

```
Authorization: Token <your-token-here>
```

Tokens are generated at login. The Menu and homepage endpoints are fully public.

---

## Homepage

### `GET /restaurant/`

Serves the static HTML homepage.

**Response:** `200 OK` (HTML page)

---

## Menu API

All Menu endpoints are **public**: no authentication required.

---

### `GET /restaurant/menu/`

List all menu items.

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "title": "Bruschetta",
    "price": "7.99",
    "inventory": 30
  },
  {
    "id": 2,
    "title": "Greek Salad",
    "price": "10.99",
    "inventory": 25
  }
]
```

---

### `POST /restaurant/menu/`

Create a new menu item.

**Request body:**
```json
{
  "title": "Pasta Carbonara",
  "price": "14.99",
  "inventory": 20
}
```

**Response:** `201 Created`
```json
{
  "id": 6,
  "title": "Pasta Carbonara",
  "price": "14.99",
  "inventory": 20
}
```

**Validation errors:** `400 Bad Request` if required fields are missing or invalid.

---

### `GET /restaurant/menu/{id}/`

Retrieve a single menu item by ID.

**Response:** `200 OK`
```json
{
  "id": 1,
  "title": "Bruschetta",
  "price": "7.99",
  "inventory": 30
}
```

**Not found:** `404 Not Found` if the ID does not exist.

---

### `PUT /restaurant/menu/{id}/`

Fully update a menu item. All fields are required.

**Request body:**
```json
{
  "title": "Bruschetta",
  "price": "9.99",
  "inventory": 25
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "title": "Bruschetta",
  "price": "9.99",
  "inventory": 25
}
```

---

### `PATCH /restaurant/menu/{id}/`

Partially update a menu item. Only include the fields to change.

**Request body:**
```json
{
  "price": "11.50"
}
```

**Response:** `200 OK`

---

### `DELETE /restaurant/menu/{id}/`

Delete a menu item.

**Response:** `204 No Content`

---

## Authentication Endpoints

Provided by [Djoser](https://djoser.readthedocs.io/).

---

### `POST /auth/users/`

Register a new user account.

**Request body:**
```json
{
  "username": "testuser",
  "password": "securepassword123"
}
```

**Response:** `201 Created`
```json
{
  "username": "testuser",
  "id": 2
}
```

---

### `POST /auth/token/login/`

Obtain an authentication token.

**Request body:**
```json
{
  "username": "testuser",
  "password": "securepassword123"
}
```

**Response:** `200 OK`
```json
{
  "auth_token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

> Copy this token. You'll use it as the `Authorization` header value for all Booking API requests.

---

### `POST /auth/token/logout/`

Revoke the current authentication token.

**Request header:**
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response:** `204 No Content`

After logout, the token is deleted from the database and cannot be reused.

---

## Booking API

All Booking endpoints **require authentication**. Add the `Authorization: Token <token>` header to every request.

Unauthenticated requests return `401 Unauthorized`.

---

### `GET /restaurant/booking/tables/`

List all table bookings.

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "Alice",
    "no_of_guests": 2,
    "booking_date": "2026-12-01T19:00:00Z"
  }
]
```

---

### `POST /restaurant/booking/tables/`

Create a new table booking.

**Request body:**
```json
{
  "name": "Bob",
  "no_of_guests": 4,
  "booking_date": "2026-12-15T20:00:00Z"
}
```

**Response:** `201 Created`
```json
{
  "id": 3,
  "name": "Bob",
  "no_of_guests": 4,
  "booking_date": "2026-12-15T20:00:00Z"
}
```

**Date format:** ISO 8601: `YYYY-MM-DDTHH:MM:SSZ`

---

### `GET /restaurant/booking/tables/{id}/`

Retrieve a single booking.

**Response:** `200 OK` (booking object)

---

### `PUT /restaurant/booking/tables/{id}/`

Fully update a booking. All fields required.

**Response:** `200 OK` (updated booking object)

---

### `PATCH /restaurant/booking/tables/{id}/`

Partially update a booking.

**Response:** `200 OK`

---

### `DELETE /restaurant/booking/tables/{id}/`

Delete a booking.

**Response:** `204 No Content`

---

## HTTP Status Code Reference

| Code | Meaning | When it occurs |
|------|---------|----------------|
| `200 OK` | Success | GET or PUT request succeeded |
| `201 Created` | Created | POST request created a new resource |
| `204 No Content` | Deleted / Logged out | DELETE or logout succeeded |
| `400 Bad Request` | Invalid input | Missing or invalid request fields |
| `401 Unauthorized` | Auth required | Booking endpoint accessed without token |
| `404 Not Found` | Not found | Requested resource ID does not exist |

---

## Data Models

### Menu

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Auto-generated primary key |
| `title` | String (max 255) | Name of the dish |
| `price` | Decimal (10,2) | Price in dollars |
| `inventory` | Integer | Number of items available |

### Booking

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Auto-generated primary key |
| `name` | String (max 255) | Guest name for the reservation |
| `no_of_guests` | Integer | Number of guests |
| `booking_date` | DateTime | Date and time of the reservation |
