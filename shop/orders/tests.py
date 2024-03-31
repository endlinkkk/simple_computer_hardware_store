from django.test import TestCase
from django.test import TestCase
from .models import Order, OrderItem, Product
from myshop.models import Category

class OrderModelTest(TestCase):
    def setUp(self):
        self.order = Order.objects.create(name='John Doe', email='johndoe@example.com', address='123 Main St', city='New York')

    def test_order_creation(self):
        self.assertEqual(self.order.name, 'John Doe')
        self.assertEqual(self.order.email, 'johndoe@example.com')
        self.assertEqual(self.order.address, '123 Main St')
        self.assertEqual(self.order.city, 'New York')
    
    def test_order_default_values(self):
        self.assertFalse(self.order.paid)

    def test_order_str_representation(self):
        self.assertEqual(str(self.order), f"Заказ {self.order.id}")

    def test_order_total_cost(self):
        category1 = Category.objects.create(name='Category 1')
        category2 = Category.objects.create(name='Category 2')
        product1 = Product.objects.create(name='Product 1', price=10.00, category=category1, count=10)
        product2 = Product.objects.create(name='Product 2', price=5.00, category=category2, count=10)
        order_item1 = OrderItem.objects.create(order=self.order, product=product1, price=10.00, quantity=2)
        order_item2 = OrderItem.objects.create(order=self.order, product=product2, price=5.00, quantity=1)

        expected_total_cost = 2 * 10.00 + 1 * 5.00
        self.assertEqual(self.order.get_total_cost(), expected_total_cost)

class OrderItemModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Category 1')
        self.product = Product.objects.create(name='Product 1', price=10.00, category=category, count=10)
        self.order = Order.objects.create(name='John Doe', email='johndoe@example.com', address='123 Main St', city='New York')
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, price=10.00, quantity=2)

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.price, 10.00)
        self.assertEqual(self.order_item.quantity, 2)

    def test_order_item_str_representation(self):
        self.assertEqual(str(self.order_item), str(self.order_item.id))

    def test_order_item_cost(self):
        expected_cost = 10.00 * 2
        self.assertEqual(self.order_item.get_cost(), expected_cost)

