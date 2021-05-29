# Password Locker

#### Created on 29th May 2021
#### By Samuel Maingi Mutunga

## Description 

A terminal based application that enable users to manage their individual passwords and also generate new passwords for them if they Want

What Can the Appication do:

* Create a password locker account with their details, a login username and password with authenication

* Can store credentials for already existing accounts

* Create new Account credentials in the Application

* Has an option for Custom Password for new account

* Can view saved accounts 

* Delete option for a specific Credential using login name(which is unique for all services)

* Auto Generate password for secure application 


---
## Design pattern

* Figma design pattern for project [Click_Me](https://www.figma.com/file/AyV5VBxbNb8cTHtmeSxAJj/password_locker?node-id=0%3A1)

## Run Application
Need an Terminal (Mac or Linux) or Command Prompt(Windows)

To run this project, please follow the following instructions.
* Get access to the internet.
* Clone the repository.

      $ git clone `https://github.com/layersony/password_locker.git`
      $ cd password_locker

* To run the application, in your terminal:

        $ chmod +x main.py
        $ ./main.py

## Testing the Application
* To run the tests for the application file:

        $ python3 test_main.py

---

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Welcomes user to the applicatin | **In terminal: $./main.py** | Welcome Message. Username & Password? |
| Register If new | **Would you like to register?** | Provide username, firstname, lastname, phone number, email, password, confirm password |
| Display menu Navigation | **What would you like to do?** | Use these codes : new - create a new credential, display - display credentials, delete - delete a credential, 00 - exit delete panel to main menu ,exit -exit the Application  |
| Prompt for creating new Credential | **Enter: new** | Enter the required form Account type, login name, email, site Url, password |
| Generate Password or input custom Password | **Want System Generated password** | gives option for either system generated password or custom password |
| Prompt for Diplay stored Credentials | **Enter: display** | list Available Credentials |
| Prompt for Deleting a Credential | **Enter: delete** | Credential deleted successfully |
| Exit | **Enter: exit** | Exit the Application |


---
## Technologies Used
Project is created with:
* Python 3.6 +

---

## Bugs

None at the moment, but would love to hear your feedback!

---

## Contact Details
For any inquiries, please reach out to

sammaingi5@gmail.com

@Maingi `Slack Moringa`

---

### License
This Project is under the [MIT](LICENSE) license