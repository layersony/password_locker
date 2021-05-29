#! /usr/bin/python3
import unittest
from user import User
from credential import Credential

class Test_User(unittest.TestCase):

  def setUp(self):
    self.usrname = 'layersony'
    self.password = '12345'

  def tearDown(self):
    with open("userlocker.txt", "w") as handle:
      handle.write("")

  def test_checkUser(self):
    User.saveUser(self.usrname + '|', 'a')
    User.saveUser(self.password, 'a')

    with open("userlocker.txt", "r") as handle:
      data = handle.read()
      fulldata = data.split("|")

      self.assertEqual(self.usrname, fulldata[0])
      self.assertEqual(self.password, fulldata[-1])

  

class Test_Credential(unittest.TestCase):
  pass


if __name__ == '__main__':
  unittest.main()