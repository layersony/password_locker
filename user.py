#! /usr/bin/python3
class User:

  userdetail = []
  """
    class for register user have to firstname, lastname, phonenumber, emaol, password, confirm password
  """
  def __init__(self, first_name, last_name, phone_number, email, password, con_pass):
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email
    self.password = password
    self.con_pass = con_pass

  # save user data
  def savedata(self):
    self.userdetail.append(self)

  @classmethod
  def displayUser(self):
    
    

  


new_contact = User("Samuel", "Maingi", "0796727706", "sm@gmail.com", "123456", '123456')
User.savedata(new_contact)

User.displayUser()