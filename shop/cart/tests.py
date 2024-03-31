from decimal import Decimal
from django.test import TestCase, Client
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory
from django.shortcuts import reverse
from cart.forms import CartAddProductForm
from cart.cart import Cart
from myshop.models import Product, Category

class CartTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        # Add session data to request
        middleware = SessionMiddleware(lambda req: None)
        middleware.process_request(self.request)
        self.request.session.save()
        self.cart = Cart(self.request)
        self.product = Product.objects.create(
            category=Category.objects.create(name='Category 1'),
            name='Product 1',
            price=10.00,
            count=5
        )

    def test_add_product(self):
        form_data = {'quantity': 2, 'add': True}
        self.client.post(reverse('cart:cart-add', args=[self.product.id]), form_data)
        self.cart = self.client.session.get('cart', {})
        self.assertEqual(len(self.cart), 1)
        self.assertEqual(self.cart[str(self.product.id)]['quantity'], 2)

    def test_remove_product(self):
        self.cart.add(self.product, 2)
        self.client.post(reverse('cart:cart-remove', args=[self.product.id]))
        self.cart = self.client.session.get('cart', {})
        self.assertEqual(len(self.cart), 0)

    def test_get_total_price(self):
        self.cart.add(self.product, 2)
        self.client.session.save()
        total_price = self.product.price * 2
        response = self.cart.get_total_price()
        self.assertEqual(total_price, Decimal(total_price))

    def test_clear_cart(self):
        self.cart.add(self.product, 2)
        self.cart.clear()
        self.cart = self.client.session.get('cart', {})
        self.assertEqual(len(self.cart), 0)