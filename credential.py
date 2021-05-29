import random
class Credential:

  mycred = []

  def __init__(self, appType, appName, appUrl, appLogin, appPassword):
    self.appType = appType
    self.appName = appName
    self.appUrl = appUrl
    self.appLogin = appLogin
    self.appPassword

  #save
  def saveUser(inputtype):
    with open("credlocker.txt", "a") as handle:
      handle.write(inputtype)
  
  #display one or many
  @classmethod
  def displayCred(cls):
    return cls.mycred

  def gen_pass(self):
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYXabcdefghijklmnopqrstuvwxyx1234567890"
    passwd = ''

    for i in range(10):
      passwd = random.choice(char)
    return passwd
  #search by app name4
  # delete selected
  # update data selected