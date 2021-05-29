#! /usr/bin/python3
from user import User
from credential import Credential

def login():
  usrname = input("Username:\t")
  password = input("Password:\t")

  if User.checkUserExist(usrname, password):
    print("*"*20)
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
  login()

# def menu():
#   usr = input("what would you like to do: ")
#   if usr == "new": # done
#     add_cred()
#   elif usr == "display": # done
#     displaycred()
#   elif usr == "delete": # done
#     delete()
#   elif usr == 'exit':
#     end = False
#   else:
#     print("didn't catch what you sayed")
#     menu()

def passcode():
  passcus = input("Want a system Gen password: ").lower()

  if passcus == "n":
    usrpass = input("Custom password: ")
    Credential.saveUser( usrpass +'\n')
  elif passcus == 'y':
    password = Credential.gen_pass()
    Credential.saveUser(password)
    Credential.saveUser('\n')
  else:
    print('Didnt catch you write Pardon')
    passcode()

def add_cred():
  
  actype = input("Account type: ")
  Credential.saveUser(actype + '|')

  login = input("Login Name: ")
  Credential.saveUser( login +'|')

  email = input("Email: ")
  Credential.saveUser( email +'|')

  passcode()

def displaycred():
  data = Credential.displayCred()
  for i in data:
    afspl = i.split('|')
    print('*'*40)
    print("Account type: " + afspl[0])
    
    print("Login Name: " + afspl[1])
    
    print("Email: " + afspl[2])
    
    print("Password: " + afspl[3])
    print('*'*40)

def delete():
  todele = input("What do you want to delete? ")

  if todele == "1":
    data = Credential.findCred("maingi")
    Credential.deleteCred(data)
    displaycred()
  else:
    print('Didnt catch you')


if __name__ == '__main__':
  end = True
  login()

  while end:
    usr = input("what would you like to do: ")
    if usr == "new": # done
      add_cred()
    elif usr == "display": # done
      displaycred()
    elif usr == "delete": # done
      delete()
    elif usr == 'exit':
      print("Thank you see you again")
      end = False
    else:
      print("didn't catch what you sayed")
      continue