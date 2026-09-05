from django.test import TestCase

from order.factories import OrderFactory
from product.factories import ProductFactory
from order.serializers.order_serializer import OrderSerializer


class OrderSerializerTestCase(TestCase):

    def test_order_serializer_fields(self):
        order = OrderFactory()

        serializer = OrderSerializer(order)

        self.assertEqual(
            set(serializer.data.keys()),
            {"product", "total", "user"}
        )

    def test_order_serializer_products_relationship(self):
        product = ProductFactory()
        order = OrderFactory()

        order.product.add(product)

        serializer = OrderSerializer(order)

        self.assertEqual(len(serializer.data["product"]), 1)

        self.assertEqual(
            serializer.data["product"][0]["title"],
            product.title
        )

    def test_order_serializer_total(self):
        product_1 = ProductFactory(price=100)
        product_2 = ProductFactory(price=50)

        order = OrderFactory()

        order.product.add(product_1, product_2)

        serializer = OrderSerializer(order)

        self.assertEqual(serializer.data["total"], 150)

    def test_order_serializer_multiple_products(self):
        product_1 = ProductFactory(price=100)
        product_2 = ProductFactory(price=200)
        product_3 = ProductFactory(price=50)

        order = OrderFactory()

        order.product.add(
            product_1,
            product_2,
            product_3
        )

        serializer = OrderSerializer(order)

        self.assertEqual(len(serializer.data["product"]), 3)
        self.assertEqual(serializer.data["total"], 350)