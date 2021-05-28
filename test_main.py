import unittest
from user import User

class TestMain(unittest.TestCase):
  
  def test_saveUser(self):
    self.new_user = User("Samuel", "Maingi", "0796727706", "sm@gmail.com", "123456", '123456')
    self.new_user.savedata()
    self.assertEqual