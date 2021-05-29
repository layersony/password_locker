#! /usr/bin/python3
from user import User
from credential import Credential

def login():
  print('\n')
  print('*****If New here input dummy username and password to access register portal*****')
  print('\n')
  usrname = input("Username:\t")
  password = input("Password:\t")

  if User.checkUserExist(usrname, password):
    print("*"*50)
    print('\t\tWelcome to the System')
  else:
    print("\n")
    print("Username and password are Invalid")
    reg = input("Would you like to register? (y/n)").lower()
    if reg == "y":
      register()
      print("\n")
    elif reg == "n":
      login()
    else:
      print("Didn't Catch what you saying")
      login() 

def register():
  usrname = input("Username (for login):  ")
  User.saveUser(usrname + '|', "w")
  first_name = input("Firstname:  ")
  User.saveUser( first_name +'|', "a" )
  last_name = input("Last_name:  ")
  User.saveUser( last_name +'|', "a")
  phone_number = input("Phone Number:  ")
  User.saveUser( phone_number +'|', "a")
  email = input("Email:  ")
  User.saveUser( email +'|', "a")
  password = input("password:  ")
  User.saveUser( password +'|', "a")
  conf_password = input("Confirm Password:  ")
  User.saveUser( conf_password, "a")
  login()

def passcode():
  passcus = input("Want a system Generated password (y/n): ").lower()

  if passcus == "n":
    usrpass = input("Custom password: ")
    Credential.saveUser( usrpass +'\n')
  elif passcus == 'y':
    password = Credential.gen_pass()
    Credential.saveUser(password)
    Credential.saveUser('\n')
  else:
    print('Didnt catch what you wrote Pardon :)')
    passcode()

def add_cred():
  
  actype = input("Account type (eg. Instagram): ")
  Credential.saveUser(actype + '|')

  login = input("Login Name: ")
  Credential.saveUser( login +'|')

  email = input("Email: ")
  Credential.saveUser( email +'|')

  url = input("App Url: ")
  Credential.saveUser( url +'|')

  passcode()

  print(f'    {login} for Account {actype} Added')

def displaycred():
  data = Credential.displayCred()
  count = 1
  for i in data:
    afspl = i.split('|')
    print('*'*40)
    print('Account--' + str(count))
    print('\n')
    print("Account type: " + afspl[0])
    print("Login Name: " + afspl[1])
    print("Email: " + afspl[2])
    print("url: " + afspl[3])
    print("Password: " + afspl[4])
    print('*'*40)
    print('\n')
    count += 1

def delete():
  todele = input("Delete which Account (login name)? ")

  if todele == "00":
    pass
  elif todele == todele :
    data = Credential.findCred(todele)
    Credential.deleteCred(data)
    print('\n')
    print('Credential deleted successfully')
    print('\n')
    displaycred()
  else:
    print("Didn't catch you")
    delete()

def welcome():
  print('''

             Welcome to Password Locker
    A Easy and Simple Application for Storing you 
             Password  Locally Via Terminal

  ''')

if __name__ == '__main__':
  end = True
  welcome()
  login()
  while end:
    print('-'*50)
    print('''
        new == create a new Credential
        display == Display saved Credentials
        delete == Delete Credential
        00 == Go back (In delete) 
        exit == Stop Application
    ''')
    print('-'*50)
    usr = input("What would you like to do: ").lower()
    print('\n')
    if usr == "new":  
      add_cred()
    elif usr == "display": 
      displaycred()
    elif usr == "delete": 
      delete()
    elif usr == 'exit': 
      print("Thank you see you again later")
      end = False
    else:
      print("didn't catch what you typed :}\n")
      continue