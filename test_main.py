#! /usr/bin/python3
import unittest
from user import User
from credential import Credential

class Test_User(unittest.TestCase):

  def setUp(self):
    self.usrname = 'layersony'
    self.password = '12345'
    self.full = self.usrname + '|' + self.password

  def tearDown(self):
    pass

  def test_checkUser(self):
    User.saveUser(self.usrname + '|', 'a')
    User.saveUser(self.password, 'a')

    with open("userlocker.txt", "r") as handle:
      data = handle.read()
      fulldata = data.split("|")

      self.assertEqual(self.usrname, fulldata[0])
      self.assertEqual(self.password, fulldata[-1])

    with open("userlocker.txt", "w") as handle:
      handle.write("")
  
  def test_save(self):
    User.saveUser(self.usrname + '|', 'a')
    User.saveUser(self.password, 'a')

    with open("userlocker.txt", "r") as handle:
      data = handle.read()
      self.assertEqual(data, self.full)


class Test_Credential(unittest.TestCase):
  def setUp(self):
    self.appType = 'twitter'
    self.appLogin = 'maingi'
    self.appUrl = 'twitter.com'
    self.email = 'sm@gmail.com'
    self.appPassword = '12345'

    self.full = 'twitter|maingi|twitter.com|sm@gmail.com|12345'

  def tearDown(self):
    with open("credlocker.txt", "w") as handle:
      handle.write("")

  def test_save(self):
    Credential.saveUser(self.appType + '|')
    Credential.saveUser(self.appLogin + '|')
    Credential.saveUser(self.appUrl + '|')
    Credential.saveUser(self.email + '|')
    Credential.saveUser(self.appPassword)

    
    with open("credlocker.txt", "r") as handle:
      data = handle.read()
      self.assertEqual(data, self.full)
      

if __name__ == '__main__':
  unittest.main()