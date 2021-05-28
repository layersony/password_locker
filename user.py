
class User:
  
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
    with open("userdetail.txt", "w") as handle:
      handle.write(self)
  