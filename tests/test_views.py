from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
from datetime import datetime


class MenuViewTest(TestCase):
    """Test cases for Menu API views"""
    
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        self.menu_item_1 = Menu.objects.create(
            title="Grilled Fish",
            price=12.99,
            inventory=20
        )
        self.menu_item_2 = Menu.objects.create(
            title="Bruschetta",
            price=8.50,
            inventory=30
        )
        self.menu_item_3 = Menu.objects.create(
            title="Greek Salad",
            price=10.00,
            inventory=25
        )
    
    def test_getall(self):
        """Test retrieving all menu items"""
        response = self.client.get('/restaurant/menu/')
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(response.data), 3)
    
    def test_menu_list_endpoint_exists(self):
        """Test that menu list endpoint exists"""
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_single_menu_item(self):
        """Test retrieving a single menu item"""
        response = self.client.get(f'/restaurant/menu/{self.menu_item_1.id}/')
        serializer = MenuSerializer(self.menu_item_1)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_create_menu_item(self):
        """Test creating a new menu item"""
        data = {
            'title': 'Pasta Carbonara',
            'price': '14.99',
            'inventory': 15
        }
        response = self.client.post('/restaurant/menu/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 4)
        self.assertEqual(response.data['title'], 'Pasta Carbonara')
    
    def test_update_menu_item(self):
        """Test updating a menu item"""
        from decimal import Decimal
        data = {
            'title': 'Grilled Fish',
            'price': '14.99',
            'inventory': 25
        }
        response = self.client.put(
            f'/restaurant/menu/{self.menu_item_1.id}/',
            data,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_item = Menu.objects.get(id=self.menu_item_1.id)
        self.assertEqual(updated_item.price, Decimal('14.99'))
        self.assertEqual(updated_item.inventory, 25)
    
    def test_delete_menu_item(self):
        """Test deleting a menu item"""
        initial_count = Menu.objects.count()
        response = self.client.delete(f'/restaurant/menu/{self.menu_item_1.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), initial_count - 1)
        self.assertFalse(Menu.objects.filter(id=self.menu_item_1.id).exists())


class MenuItemFilterTest(TestCase):
    """Test filtering menu items"""
    
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        Menu.objects.create(title="Expensive Dish", price=99.99, inventory=5)
        Menu.objects.create(title="Cheap Dish", price=2.50, inventory=50)
    
    def test_menu_items_returned_with_correct_data(self):
        """Test that menu items are returned with correct data"""
        response = self.client.get('/restaurant/menu/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
        titles = [item['title'] for item in response.data]
        self.assertIn("Expensive Dish", titles)
        self.assertIn("Cheap Dish", titles)
