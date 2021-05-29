#! /usr/bin/python3
import unittest
from user import User
from credential import Credential

class Test_User(unittest.TestCase):
  '''
    tests below test the functionality of the class behaivours

    Args:
      unittest.TestCase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases in the test User Class
    '''
    self.usrname = 'smaingi'
    self.first_name = 'samuel'
    self.last_name = 'maingi'
    self.phone_number = '072345678'
    self.email = 'sm@gmail.com'
    self.password = '12345'
    self.con_pass = '12345'
    self.full = self.usrname + '|' + self.password

  def test_init(self):
    '''
    test init test case if the object is initialized correctly
    '''
    self.assertEqual(self.usrname, "smaingi")
    self.assertEqual(self.first_name, 'samuel')
    self.assertEqual(self.last_name, 'maingi')
    self.assertEqual(self.phone_number, '072345678')
    self.assertEqual(self.email, 'sm@gmail.com')
    self.assertEqual(self.con_pass, '12345')
    self.assertEqual(self.password, "12345")

  def test_checkUser(self):
    '''
      test checkuser is for authentication to see if the user exists or not
    '''
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
    '''
      test save to check it save function in user is working correctly
    '''
    User.saveUser(self.usrname + '|', 'a')
    User.saveUser(self.password, 'a')

    with open("userlocker.txt", "r") as handle:
      data = handle.read()
      self.assertEqual(data, self.full)


class Test_Credential(unittest.TestCase):
  '''
    tests below test the functionality of the class behaivours

    Args:
      unittest.TestCase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
      Set up method to run before each test cases.
    '''
    self.appType = 'twitter'
    self.appLogin = 'maingi'
    self.appUrl = 'twitter.com'
    self.email = 'sm@gmail.com'
    self.appPassword = '12345'

    self.full = 'twitter|maingi|twitter.com|sm@gmail.com|12345'

  def tearDown(self):
    '''
      tear down method to run after each test cases.
    '''
    with open("credlocker.txt", "w") as handle:
      handle.write("")

  def test_save(self):
    '''
      test save to check it save function in credential is working correctly
    '''
    Credential.saveUser(self.appType + '|')
    Credential.saveUser(self.appLogin + '|')
    Credential.saveUser(self.appUrl + '|')
    Credential.saveUser(self.email + '|')
    Credential.saveUser(self.appPassword)

    
    with open("credlocker.txt", "r") as handle:
      data = handle.read()
      self.assertEqual(data, self.full)

  def test_gen_pass(self):
    '''
      method that tests if passwords are being generated and lenght is 20
    '''
    self.assertEqual(len(Credential.gen_pass()), 20)

  def test_find(self):
    '''
      method that tests if data saved from test unit is the same as the one found when 
      run from the credential.py
    '''
    Credential.saveUser(self.full)
    data = Credential.displayCred()
    found = Credential.findCred('maingi')
    found2 = ['|'.join(found[0:])]
    self.assertEqual(data, found2)

  def test_display(self):
    '''
      method that tests if the same data that will be displayed in for the user will be the same as one produced here
    '''
    Credential.saveUser(self.full)
    data = Credential.displayCred()
    self.assertEqual(data, Credential.displayCred())
    
  def test_delete(self):
    '''
      method that tests the number of items saved when the one is deleted
    '''

    full = 'twitter|maingi|twitter.com|sm@gmail.com|12345\n'
    full2 = 'instagram|mutunga|instagram.com|tyu@gmail.com|87648976\n'
    full3 = 'facebook|layersony|facebook.com|unb@gmail.com|34786855\n'
    Credential.saveUser(full)
    Credential.saveUser(full2)
    Credential.saveUser(full3)
    data = Credential.findCred("mutunga")
    Credential.deleteCred(data)
    with open("credlocker.txt", "r") as handle:
      info = handle.readlines()
      self.assertEqual(len(info), 2)

if __name__ == '__main__':
  unittest.main()
