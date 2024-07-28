import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(initial_balance=100)
        self.target_account = Account(initial_balance=50)
    
    def test_withdraw_success(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)
    
    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_deposit_success(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    
    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)
    
    def test_transfer_success(self):
        self.account.transfer(50, self.target_account)
        self.assertEqual(self.account.balance, 50)
        self.assertEqual(self.target_account.balance, 100)
    
    def test_transfer_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.transfer(150, self.target_account)
    
    def test_transfer_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.transfer(-10, self.target_account)

if __name__ == '__main__':
    unittest.main()