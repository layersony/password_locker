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
    reg = input("WOuld you like to register? (y/n)").lower()
    if reg == "y":
      register()
    elif reg == "n":
      login()
    else:
      print("Didn't Catch what you saying")
      login()
      

def register():
  usrname = input("Username (for login)")
  User.saveUser(usrname + '|', "w")
  first_name = input("Firstname: ")
  User.saveUser( first_name +'|', "a" )
  last_name = input("Last_name: ")
  User.saveUser( last_name +'|', "a")
  phone_number = input("Phone Number: ")
  User.saveUser( phone_number +'|', "a")
  email = input("Email: ")
  User.saveUser( email +'|', "a")
  password = input("password: ")
  User.saveUser( password +'|', "a")
  conf_password = input("Confirm Password: ")
  User.saveUser( conf_password, "a")

def menu():
  usr = input("what would you like to do:")
  if usr == "new":
    pass
  elif  usr == "update":
    pass
  elif usr == "list":
    pass
  elif usr == "delete":
    pass
  else:
    print("didn't catch what you sayed")
    menu()

if __name__ == '__main__':
  login()
  menu()
