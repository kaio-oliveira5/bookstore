from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.models import category
from product.serializers.product_serializer import ProductSerializer


class ProductSerializerTestCase(TestCase):

    def test_product_serializer_fields(self):
        product = ProductFactory()

        serializer = ProductSerializer(product)

        self.assertEqual(
            set(serializer.data.keys()),
            {"id", "title", "description", "price", "active", "category"},
        )

    def test_product_serializer_valid_data(self):
        category = CategoryFactory()

        data = {
            "title": "Livro Python",
            "description": "Livro sobre Python",
            "price": 100,
            "active": True,
            "categories_id": [category.id],
        }

        serializer = ProductSerializer(data=data)

        is_valid = serializer.is_valid()

        self.assertTrue(is_valid)

    def test_product_serializer_required_fields(self):
        data = {
            "description": "Livro sobre Python",
            "price": 100,
            "active": True,
            "category": [],
        }

        serializer = ProductSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

    def test_product_serializer_category_relationship(self):
        category = CategoryFactory()
        product = ProductFactory()

        product.category.add(category)

        serializer = ProductSerializer(product)

        self.assertEqual(len(serializer.data["category"]), 1)

        self.assertEqual(serializer.data["category"][0]["title"], category.title)

        self.assertEqual(serializer.data["category"][0]["slug"], category.slug)

    def test_product_serializer_invalid_price(self):
        data = {
            "title": "Livro Python",
            "description": "Livro sobre Python",
            "price": -100,
            "active": True,
            "category": [],
        }

        serializer = ProductSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("price", serializer.errors)
