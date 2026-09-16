from django.test import TestCase

from product.factories import CategoryFactory
from product.serializers.category_serializer import CategorySerializer


class CategorySerializerTestCase(TestCase):

    def test_category_serializer_fields(self):
        category = CategoryFactory()

        serializer = CategorySerializer(category)

        self.assertEqual(
            set(serializer.data.keys()), {"title", "slug", "description", "active"}
        )

    def test_category_serializer_valid_data(self):
        data = {
            "title": "Livros",
            "slug": "livros",
            "description": "Categoria de livros",
            "active": True,
        }

        serializer = CategorySerializer(data=data)

        self.assertTrue(serializer.is_valid())

    def test_category_serializer_required_fields(self):
        data = {
            "description": "Categoria de livros",
            "active": True,
        }

        serializer = CategorySerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

    def test_category_serializer_invalid_slug(self):
        data = {
            "title": "Livros",
            "slug": "slug inválido!",
            "description": "Categoria de livros",
            "active": True,
        }

        serializer = CategorySerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("slug", serializer.errors)
