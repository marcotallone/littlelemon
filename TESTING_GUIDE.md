# Testing Guide for Little Lemon Restaurant API

## Unit Testing - COMPLETED ✅

### Summary

I have created comprehensive unit tests for your Django application:

**Test Files Created:**

- `tests/test_models.py` - 6 test cases for Menu and Booking models
- `tests/test_views.py` - 7 test cases for Menu API views

**Total Tests: 13 - ALL PASSING ✅**

### Running Unit Tests

#### Run all tests:

```bash
cd /Users/marco/Projects/coursera/meta_backend/06_FInalProject/littlelemon
source workspace/bin/activate
python manage.py test tests -v 2
```

#### Run only model tests:

```bash
python manage.py test tests.test_models -v 2
```

#### Run only view tests:

```bash
python manage.py test tests.test_views -v 2
```

#### Run a specific test:

```bash
python manage.py test tests.test_models.MenuTest.test_menu_creation
```

### Test Coverage

**Model Tests (test_models.py):**

- ✅ Menu string representation
- ✅ Menu creation
- ✅ Menu update
- ✅ Menu deletion
- ✅ Booking creation
- ✅ Booking string representation

**View Tests (test_views.py):**

- ✅ Retrieve all menu items (GET /restaurant/menu/)
- ✅ Retrieve single menu item (GET /restaurant/menu/<id>/)
- ✅ Create menu item (POST /restaurant/menu/)
- ✅ Update menu item (PUT /restaurant/menu/<id>/)
- ✅ Delete menu item (DELETE /restaurant/menu/<id>/)
- ✅ Menu API endpoint exists
- ✅ Menu items returned with correct data

---

## Manual Testing with Insomnia - YOU NEED TO DO THIS ⚠️

### Step 1: Download and Install Insomnia

Visit: https://insomnia.rest/download

Download the Insomnia REST client for your operating system (macOS, Linux, or Windows).

### Step 2: Start the Django Server

```bash
cd /Users/marco/Projects/coursera/meta_backend/06_FInalProject/littlelemon
source workspace/bin/activate
python manage.py runserver 8000
```

### Step 3: Open Insomnia App

Launch the Insomnia application you just installed.

### Step 4: Create New Request - Test GET (Menu List)

1. Click "Create Request"
2. Enter URL: `http://127.0.0.1:8000/restaurant/menu/`
3. Select method: **GET**
4. Click "Send"
5. Verify you get a list of all menu items in the response panel

### Step 5: Test POST (Create Menu Item)

1. Create a new request
2. Enter URL: `http://127.0.0.1:8000/restaurant/menu/`
3. Select method: **POST**
4. Go to "Body" tab → Select "JSON" format
5. Enter JSON data:

```json
{
  "title": "New Dish",
  "price": "12.99",
  "inventory": 20
}
```

6. Click "Send"
7. Verify you get a 201 Created response with the new item ID

### Step 6: Test PUT (Update Menu Item)

1. Create a new request
2. Enter URL: `http://127.0.0.1:8000/restaurant/menu/1/`
3. Select method: **PUT**
4. Go to "Body" tab → Select "JSON" format
5. Enter updated data:

```json
{
  "title": "Updated Grilled Fish",
  "price": "15.99",
  "inventory": 30
}
```

6. Click "Send"
7. Verify you get a 200 OK response with updated data

### Step 7: Test DELETE (Delete Menu Item)

1. Create a new request
2. Enter URL: `http://127.0.0.1:8000/restaurant/menu/6/` (or any item ID you created)
3. Select method: **DELETE**
4. Click "Send"
5. Verify you get a 204 No Content response
6. Confirm deletion by running GET request to verify the item is gone

---

## Testing User Authentication - YOU NEED TO DO THIS ⚠️

### Step 1: Register a New User (via Insomnia)

1. Create a new request
2. Enter URL: `http://127.0.0.1:8000/auth/users/`
3. Select method: **POST**
4. Go to "Body" tab → Select "JSON" format
5. Enter:

```json
{
  "username": "testuser",
  "password": "SecurePassword123!"
}
```

6. Click "Send"
7. Verify you get 201 Created response

### Step 2: Get Authentication Token

1. Create a new request
2. Enter URL: `http://127.0.0.1:8000/auth/token/login/`
3. Select method: **POST**
4. Body JSON:

```json
{
  "username": "testuser",
  "password": "SecurePassword123!"
}
```

5. Click "Send"
6. **Copy the auth_token from the response** - you'll need this for protected endpoints

### Step 3: Test Protected Booking API

1. Create a new request
2. Enter URL: `http://127.0.0.1:8000/restaurant/booking/tables/`
3. Select method: **GET**
4. Go to "Auth" tab
5. Select "Bearer Token" from dropdown
6. Paste your auth_token
7. Click "Send"
8. Verify you can now access the protected endpoint and see all bookings

### Step 4: Create a Booking (Protected)

1. Create a new request
2. Enter URL: `http://127.0.0.1:8000/restaurant/booking/tables/`
3. Select method: **POST**
4. Add Auth token (same as Step 3)
5. Go to "Body" tab → JSON format
6. Enter:

```json
{
  "name": "Test Customer",
  "no_of_guests": 5,
  "booking_date": "2026-11-20T19:00:00Z"
}
```

7. Click "Send"
8. Verify you get 201 Created with new booking ID

### Step 5: Test Logout

1. Create a new request
2. Enter URL: `http://127.0.0.1:8000/auth/token/logout/`
3. Select method: **POST**
4. Add your auth_token in Auth tab
5. Click "Send"
6. Try accessing booking API again with same token
7. Verify you get 401 Unauthorized error

---

## Browsable API - Manual Testing Alternative

If you prefer not to use Insomnia, you can use the Django Browsable API:

1. Start server: `python manage.py runserver 8000`
2. Visit: http://127.0.0.1:8000/restaurant/menu/
3. You can use the built-in form to:
   - View all items (GET)
   - Create items (POST)
   - View single items (GET)
   - Update items (PUT)
   - Delete items (DELETE)

For protected endpoints, use the "Login" button in top right corner of the browsable API.

---

## Summary of Testing

### ✅ Automated (Completed)

- Unit tests for models (CRUD operations)
- Unit tests for API views (GET, POST, PUT, DELETE)
- All 13 tests passing

### ⚠️ Manual Testing (YOU DO)

1. Download and install Insomnia
2. Test Menu API (GET, POST, PUT, DELETE)
3. Test user registration and login
4. Test protected Booking API with token authentication
5. Test logout and token invalidation

---

## Expected Test Results

**Unit Tests:**

```
Ran 13 tests in 0.048s
OK
```

**Manual Testing Checklist:**

- [ ] Menu GET returns all items
- [ ] Menu POST creates new item
- [ ] Menu GET single returns correct item
- [ ] Menu PUT updates item
- [ ] Menu DELETE removes item
- [ ] User registration works
- [ ] Token login generates auth token
- [ ] Booking API requires token
- [ ] Booking API with token returns data
- [ ] Create booking with token succeeds
- [ ] Logout invalidates token
