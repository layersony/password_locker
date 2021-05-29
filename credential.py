import random
import string
import os


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

  # gen_password
  def gen_pass():

    passwd = ''
    symbols = ['*', '%', '£']

    for _ in range(5):
      passwd += random.choice(string.ascii_lowercase)
      passwd += random.choice(string.ascii_uppercase)
      passwd += random.choice(string.digits)
      passwd += random.choice(symbols)
    return passwd
  
  # delete selected
  def deleteCred(info):
    file = open("credlocker.txt", "r")
    temp = open("temp.txt", 'w+')

    data = file.readlines()
    for i in data:
      tdata = i.split("|")
      if tdata != info:
        temp.write(i)

    file.close()
    temp.close()

    os.remove('credlocker.txt')
    os.replace('temp.txt', "credlocker.txt")

  #find by name
  @classmethod
  def findCred(cls, name):
    data = cls.displayCred()
    for i in data:
      afspl = i.split('|')
      if afspl[1] == name:
        return afspl


  #search by app name4
  # update data selected