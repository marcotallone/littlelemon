from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime


class MenuTest(TestCase):
    """Test cases for Menu model"""
    
    def setUp(self):
        """Set up test data"""
        self.menu_item = Menu.objects.create(
            title="IceCream",
            price=8.0,
            inventory=100
        )
    
    def test_menu_str_representation(self):
        """Test the string representation of Menu model"""
        expected_str = "IceCream : 8.0"
        self.assertEqual(str(self.menu_item), expected_str)
    
    def test_menu_creation(self):
        """Test creating a menu item"""
        item = Menu.objects.create(
            title="Pizza",
            price=12.50,
            inventory=50
        )
        self.assertTrue(Menu.objects.filter(title="Pizza").exists())
        self.assertEqual(item.price, 12.50)
        self.assertEqual(item.inventory, 50)
    
    def test_menu_update(self):
        """Test updating a menu item"""
        self.menu_item.price = 10.0
        self.menu_item.save()
        updated_item = Menu.objects.get(id=self.menu_item.id)
        self.assertEqual(updated_item.price, 10.0)
    
    def test_menu_deletion(self):
        """Test deleting a menu item"""
        item_id = self.menu_item.id
        self.menu_item.delete()
        self.assertFalse(Menu.objects.filter(id=item_id).exists())


class BookingTest(TestCase):
    """Test cases for Booking model"""
    
    def setUp(self):
        """Set up test data"""
        self.booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=datetime(2026, 11, 15, 19, 0, 0)
        )
    
    def test_booking_creation(self):
        """Test creating a booking"""
        booking = Booking.objects.create(
            name="Jane Smith",
            no_of_guests=2,
            booking_date=datetime(2026, 11, 16, 20, 30, 0)
        )
        self.assertTrue(Booking.objects.filter(name="Jane Smith").exists())
        self.assertEqual(booking.no_of_guests, 2)
    
    def test_booking_str_representation(self):
        """Test the string representation of Booking model"""
        self.assertEqual(str(self.booking), "John Doe")
