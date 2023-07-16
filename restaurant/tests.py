from django.test import TestCase
from restaurant.models import Menu,Booking
import datetime
from unittest import mock
from django.test.utils import setup_test_environment
from django.test import Client
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from .views import MenuItemsView
import json

class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(title='Foo',price=6.50,inventory=5)
        
    def test_menus(self):
        menu = Menu.objects.get(title="Foo")
        self.assertEqual(menu.price,6.50)
        self.assertEqual(menu.inventory,5)
        
    def test_get_item(self):
        menu = Menu.objects.get(title="Foo")
        self.assertEqual(menu.get_item(), "Foo : 6.50")
        
class BookingTestCase(TestCase):
    def setUp(self):
        Booking.objects.create(name='Foo',no_of_guests=5,booking_date=datetime.datetime(2022,7,13,6,30))
    
    def test_bookings(self):
        booking = Booking.objects.get(name='Foo')
        self.assertTrue(booking.no_of_guests,5)
        self.assertTrue(booking.booking_date,datetime.datetime(2022,7,13,6,30))
        

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Foo',price=6.50,inventory=5)
        Menu.objects.create(title='Foo2',price=7.50,inventory=6)

    def test_menu_view(self):
        factory = APIRequestFactory()
        user = User.objects.create_user('tester','foo@bar.com','blablah12')
        request=factory.get('/restaurant/menu',format='json')
        force_authenticate(request,user)
        view=MenuItemsView.as_view()
        response=view(request)
        self.assertEqual(len(response.data),2)
        titles=[x['title'] for x in response.data]
        self.assertEqual(titles,['Foo','Foo2'])