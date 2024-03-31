from django.test import TestCase
from myshop.models import Category, Product

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Category 1')

    def test_category_name(self):
        self.assertEqual(self.category.name, 'Category 1')

    def test_category_str_representation(self):
        self.assertEqual(str(self.category), 'Category 1')

    def test_category_absolute_url(self):
        expected_url = f'/{self.category.id}/'
        self.assertEqual(self.category.get_absolute_url(), expected_url)

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Category 1')
        self.product = Product.objects.create(
            category=self.category,
            name='Product 1',
            price=10.00,
            count=5
        )

    def test_product_category(self):
        self.assertEqual(self.product.category, self.category)

    def test_product_name(self):
        self.assertEqual(self.product.name, 'Product 1')

    def test_product_price(self):
        self.assertEqual(self.product.price, 10.00)

    def test_product_count(self):
        self.assertEqual(self.product.count, 5)

    def test_product_str_representation(self):
        self.assertEqual(str(self.product), 'Product 1')

    def test_product_absolute_url(self):
        expected_url = f'/product/{self.product.id}'
        self.assertEqual(self.product.get_absolute_url(), expected_url)