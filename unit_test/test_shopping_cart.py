import unittest
from shopping_cart import Product, ShoppingCart, NotExistsProductError

API_VERSION = 17

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.bed = Product("Bed", 25.2)
        self.juice = Product("Orange", 23.3)
        self.shopping_cart = ShoppingCart() #before test
        self.shopping_cart.add_product(self.bed)

    def tearDown(self):
        pass    #after test

    def test_five_plus_five_iqual_ten(self):
        assert 5 + 5 == 10

    def test_product_name_iqual_bed(self):
        self.assertEqual(self.bed.name, "Bed") # ==

    def test_product_name_diferent_apple(self):
        self.assertNotEqual(self.juice.name, "Apple")

    def test_contains_products(self):
        self.assertTrue(self.shopping_cart.contains_products())

    def test_not_contains_products(self):
        self.shopping_cart.remove_products(self.bed)
        self.assertFalse(self.shopping_cart.contains_products())

    def test_obteins_product_bed(self):
        product = self.shopping_cart.get_product(self.bed)
        self.assertIs(product, self.bed) #is
        self.assertIsNot(product, self.juice)

    def test_execption_obtain_juice(self):
        with self.assertRaises(NotExistsProductError):
            self.shopping_cart.get_product(self.juice)
            
    def test_total_with_one_product(self):
        total = self.shopping_cart.total()
        self.assertGreater(total, 0)
        self.assertLess(total, self.bed.price + 1.0)
        self.assertEqual(total, self.bed.price)

    def test_code_bed(self):
        self.assertRegex(self.bed.code(), self.bed.name)

    def test_fail(self):
        if 2 > 3:
            self.fail("Two is not greater than three!")

    #@unittest.skip("Motives")
    #@unittest.skipIf(API_VERSION < 18, "Motives")
    @unittest.skipUnless(3 > 5, "Motives")
    def test_skip(self):
        pass



if __name__ == "__main__":
    unittest.main()