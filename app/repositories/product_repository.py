from typing import List

from app.models.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product):
        self.products.append(product)
