import unittest
from main_module import process_orders



class Test_Soft(unittest.TestCase):
   def test_check_product(self):
      inventory = {"apple": 10}
      orders = [{"product": "cherry", "quantity": 2}]
      with self.assertRaises(ValueError):
        process_orders(orders, inventory)
      print(f"{orders} not found")


   def test_product_stock(self):
      inventory = {"apple": 5}
      orders = [{"product": "apple", "quantity": 10}]
      with self.assertRaises(ValueError):
        process_orders(orders, inventory)
      print(f"{orders} not enough quantity in invertory, Today's quantity is {inventory}")

   def test_order(self):
       inventory = {"apple": 10}
       orders = [{"product": "apple", "quantity": 3}]
       result = process_orders(orders, inventory)
       self.assertEqual(result, orders)
       self.assertEqual(inventory["apple"], 7)



if __name__=="__main__":
    unittest.main()