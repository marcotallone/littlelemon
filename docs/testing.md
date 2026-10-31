# Testing Guide

<div align="center">
  <p>
    <a href="index.md">← Documentation Index</a> ·
    <a href="../README.md">← README</a>
  </p>
</div>

---

This guide covers two types of testing for the Little Lemon API:

1. **Automated unit tests**: run via Django's test runner (13 tests)
2. **Manual API testing**: using the Insomnia REST client

---

## Part 1: Automated Unit Tests

### Running the Tests

```bash
# From the littlelemon/ project root with venv active
source workspace/bin/activate
python manage.py test tests -v 2
```

### Expected Output

```
test_booking_creation (tests.test_models.BookingTest) ... ok
test_booking_str_representation (tests.test_models.BookingTest) ... ok
test_menu_creation (tests.test_models.MenuTest) ... ok
test_menu_deletion (tests.test_models.MenuTest) ... ok
test_menu_str_representation (tests.test_models.MenuTest) ... ok
test_menu_update (tests.test_models.MenuTest) ... ok
test_create_menu_item (tests.test_views.MenuViewTest) ... ok
test_delete_menu_item (tests.test_views.MenuViewTest) ... ok
test_get_single_menu_item (tests.test_views.MenuViewTest) ... ok
test_getall (tests.test_views.MenuViewTest) ... ok
test_menu_list_endpoint_exists (tests.test_views.MenuViewTest) ... ok
test_update_menu_item (tests.test_views.MenuViewTest) ... ok
test_menu_items_returned_with_correct_data (tests.test_views.MenuItemFilterTest) ... ok

----------------------------------------------------------------------
Ran 13 tests in ~0.05s

OK
```

> Tests run against a temporary test database (`test_LittleLemon`) that is created and destroyed automatically. Your production data is not affected.

### What the Tests Cover

#### Model Tests (`tests/test_models.py`)

| Test | Description |
|------|-------------|
| `test_menu_str_representation` | `str(menu)` returns `"Title : price"` |
| `test_menu_creation` | Menu item saved with correct field values |
| `test_menu_update` | Updated price persisted to database |
| `test_menu_deletion` | Deleted item no longer in database |
| `test_booking_creation` | Booking saved with correct field values |
| `test_booking_str_representation` | `str(booking)` returns guest name |

#### View Tests (`tests/test_views.py`)

| Test | Description |
|------|-------------|
| `test_getall` | `GET /restaurant/menu/` returns all items |
| `test_menu_list_endpoint_exists` | Endpoint returns `200 OK` |
| `test_get_single_menu_item` | `GET /restaurant/menu/{id}/` returns correct item |
| `test_create_menu_item` | `POST` creates item, returns `201 Created` |
| `test_update_menu_item` | `PUT` updates item, persists to database |
| `test_delete_menu_item` | `DELETE` removes item, returns `204 No Content` |
| `test_menu_items_returned_with_correct_data` | Response data matches expected titles |

---

## Part 2: Manual API Testing with Insomnia

### Setup

1. Download and install Insomnia from [insomnia.rest/download](https://insomnia.rest/download)
2. Start the Django development server:
   ```bash
   source workspace/bin/activate
   python manage.py runserver
   ```
3. Open Insomnia and create a new **Collection** called "Little Lemon API"

---

### Test 1: List Menu Items (Public GET)

| Field | Value |
|-------|-------|
| Method | `GET` |
| URL | `http://127.0.0.1:8000/restaurant/menu/` |
| Auth | None |

**Expected:** `200 OK` (JSON array of menu items)

---

### Test 2: Create a Menu Item (Public POST)

| Field | Value |
|-------|-------|
| Method | `POST` |
| URL | `http://127.0.0.1:8000/restaurant/menu/` |
| Auth | None |
| Body (JSON) | `{"title": "New Dish", "price": "12.99", "inventory": 20}` |

**Expected:** `201 Created` (the new item with its assigned `id`)

---

### Test 3: Retrieve a Single Menu Item

| Field | Value |
|-------|-------|
| Method | `GET` |
| URL | `http://127.0.0.1:8000/restaurant/menu/1/` |
| Auth | None |

**Expected:** `200 OK` (single menu item object)

---

### Test 4: Update a Menu Item (PUT)

| Field | Value |
|-------|-------|
| Method | `PUT` |
| URL | `http://127.0.0.1:8000/restaurant/menu/1/` |
| Auth | None |
| Body (JSON) | `{"title": "Bruschetta", "price": "9.99", "inventory": 25}` |

**Expected:** `200 OK` (updated menu item object)

---

### Test 5: Delete a Menu Item

| Field | Value |
|-------|-------|
| Method | `DELETE` |
| URL | `http://127.0.0.1:8000/restaurant/menu/1/` |
| Auth | None |

**Expected:** `204 No Content` (empty response body)

---

### Test 6: Register a New User

| Field | Value |
|-------|-------|
| Method | `POST` |
| URL | `http://127.0.0.1:8000/auth/users/` |
| Auth | None |
| Body (JSON) | `{"username": "testuser", "password": "testpass123"}` |

**Expected:** `201 Created`
```json
{"username": "testuser", "id": 2}
```

---

### Test 7: Obtain an Auth Token (Login)

| Field | Value |
|-------|-------|
| Method | `POST` |
| URL | `http://127.0.0.1:8000/auth/token/login/` |
| Auth | None |
| Body (JSON) | `{"username": "testuser", "password": "testpass123"}` |

**Expected:** `200 OK`
```json
{"auth_token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"}
```

> **Important:** Copy the `auth_token` value. You'll need it for the Booking API tests below.

---

### Test 8: Access Bookings Without Token (Should Fail)

| Field | Value |
|-------|-------|
| Method | `GET` |
| URL | `http://127.0.0.1:8000/restaurant/booking/tables/` |
| Auth | None |

**Expected:** `401 Unauthorized`
```json
{"detail": "Authentication credentials were not provided."}
```

This confirms the Booking API is protected.

---

### Test 9: Access Bookings With Token

| Field | Value |
|-------|-------|
| Method | `GET` |
| URL | `http://127.0.0.1:8000/restaurant/booking/tables/` |
| Auth | Header: `Authorization: Token <your-token>` |

In Insomnia, set the **Auth** tab to **Bearer Token** and paste your token there (Insomnia adds the `Token` prefix automatically), or use the **Header** tab:
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Expected:** `200 OK` (JSON array of bookings)

---

### Test 10: Create a Booking

| Field | Value |
|-------|-------|
| Method | `POST` |
| URL | `http://127.0.0.1:8000/restaurant/booking/tables/` |
| Auth | `Authorization: Token <your-token>` |
| Body (JSON) | `{"name": "Alice", "no_of_guests": 4, "booking_date": "2026-12-20T19:00:00Z"}` |

**Expected:** `201 Created` (the new booking with assigned `id`)

---

### Test 11: Log Out (Revoke Token)

| Field | Value |
|-------|-------|
| Method | `POST` |
| URL | `http://127.0.0.1:8000/auth/token/logout/` |
| Auth | `Authorization: Token <your-token>` |
| Body | None |

**Expected:** `204 No Content`

After logout, repeat **Test 9** with the same token. You should now receive `401 Unauthorized`.

---

### Insomnia Tips

- Set `Content-Type: application/json` on all POST/PUT requests (Insomnia does this automatically when you select **JSON** as the body type).
- Save requests to a collection so you can re-run them quickly.
- Use Insomnia's **Environment** feature to store the base URL and token as variables.
