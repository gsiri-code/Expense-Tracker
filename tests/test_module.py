import unittest
from unittest.mock import patch
from helper_class.expense import ExpenseRegistry

class TestExpenseRegistry(unittest.TestCase):

    def setUp(self):
        # Create a fresh instance of ExpenseRegistry for each test
        self.registry = ExpenseRegistry()

    def test_add_expense(self):
        with patch('builtins.input', side_effect=['100', 'food', 'dinner']):
            self.assertTrue(self.registry.add_expense())
            self.assertEqual(self.registry.get_total(), 100)

    def test_delete_expense(self):
        # Add an expense first
        with patch('builtins.input', side_effect=['100', 'food', 'dinner']):
            self.registry.add_expense()
        # Now, test deleting it
        with patch('builtins.input', return_value='1'):
            self.assertTrue(self.registry.delete_expense())
            self.assertFalse(self.registry.delete_expense())  # Deleting again should return False

    # ... similarly, you can add tests for other methods ...

    def test_save(self):
        with patch('builtins.input', side_effect=['100', 'food', 'dinner']):
            self.registry.add_expense()
        # Save to a temporary file (for the sake of the example, we're using 'test.csv')
        self.assertTrue(self.registry.save('test.csv'))
        # You can also add assertions to check the contents of the file

    # ... and so on ...

if __name__ == '__main__':
    unittest.main()
