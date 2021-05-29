class User:

  userdetail = ["layersony","Samuel", "Maingi", "0796727706", "sm@gmail.com", "123456", '123456']

  """
    class for register user have to firstname, lastname, phonenumber, email, password, confirm password
  """
  def __init__(self, username ,first_name, last_name, phone_number, email, password, con_pass):

    '''
      initialize the class user when called
    '''
    self.username = username
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email
    self.password = password
    self.con_pass = con_pass
  
  @classmethod
  def checkUserExist(cls, usrname, password):
    '''
      this method checks the username and password provided by user input if it exists  in the file or not
    '''
    with open("userlocker.txt", "r") as handle:
      data = handle.read()
      fulldata = data.split("|")    
    if usrname == fulldata[0] and password == fulldata[-1]:
      return True
    else:
      return False

  def saveUser(inputtype, mood):
    '''
      method to save data that is provide by user during registration
    '''
    with open("userlocker.txt", mood) as handle:
      handle.write(inputtype)

