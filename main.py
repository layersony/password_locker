#! /usr/bin/python3
from user import User
from credential import Credential

def login():
  usrname = input("Username:\t")
  password = input("Password:\t")

  if User.checkUserExist(usrname, password):
    print("User exist")
  else:
    print("Username and password are Invalid")



if __name__ == '__main__':
  login()