class User:

  userdetail = ["Samuel", "Maingi", "0796727706", "sm@gmail.com", "123456", '123456']

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
  def saveUser(self): # if new
    User.userdetail.append(self)

  
  def displayUser(self): # display user information from registration
    return User.userdetail
  
  @classmethod
  def checkUserExist(cls, usrname, password):
    if usrname == cls.userdetail[0] and password == cls.userdetail[5]:
      return True
    else:
      return False