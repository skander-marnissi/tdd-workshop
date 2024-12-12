from app.models.product import Product
from app.repositories.product_repository import ProductRepository

class TestProductRepository:
    def test_add_product_with_valid_data(self):
        #Given
        product_repository = ProductRepository()
        product = Product('id_0','sword',250)

        #When
        product_repository.add_product(product)

        #Then
        assert len(product_repository.products) == 1
        assert product_repository.products[0] == product

    def test_get_products_with_valid_data(self):
        pass