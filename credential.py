import random
import string


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
  def displayCred():
    with open("credlocker.txt", "r") as handle:
      data = handle.readlines()
      return data 

  def gen_pass():

    passwd = ''
    symbols = ['*', '%', '£']

    for _ in range(5):
      passwd += random.choice(string.ascii_lowercase)
      passwd += random.choice(string.ascii_uppercase)
      passwd += random.choice(string.digits)
      passwd += random.choice(symbols)
    return passwd
    
  #search by app name4
  # delete selected
  # update data selected