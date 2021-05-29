class User:

  userdetail = ["layersony","Samuel", "Maingi", "0796727706", "sm@gmail.com", "123456", '123456']

  """
    class for register user have to firstname, lastname, phonenumber, emaol, password, confirm password
  """
  def __init__(self, username ,first_name, last_name, phone_number, email, password, con_pass):
    self.username = username
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email
    self.password = password
    self.con_pass = con_pass
  
  @classmethod
  def checkUserExist(cls, usrname, password):
    with open("userlocker.txt", "r") as handle:
      data = handle.read()
      fulldata = data.split("|")    
    if usrname == fulldata[0] and password == fulldata[-1]:
      return True
    else:
      return False

  def saveUser(inputtype, mood):
    with open("userlocker.txt", mood) as handle:
      handle.write(inputtype)

