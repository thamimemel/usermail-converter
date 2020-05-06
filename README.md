# UserMail Converter

A simple GUI tool made with python and PyQt5, used to convert between emails and usernames.

## Key Features
- [x] Import or Export accounts
- [x] Convert Emails to Usernames and the other way around
- [x] Support lists with passwords (separated by ":" only)
- [x] Simple Interface
- [x] It works and it's not a virus ;D
	### Todo
	i don't know ! but feel free to suggest anything you want to be included.
## Requirements
Python >= 3.5  
PyQt5 >= 5.14.2  
PyAutoGUI >= 0.9.50  

## Installation

### Windows Executables
Binaries for windows are available under [releases](https://github.com/ThamiMemel/UserMail_Converter/releases)  
***Notice** : Zip version is prefered over portable veriosn since the portable one has a slow startup.*
### Linux Executables
***Notice** : Pypi or running from source are prefered for Linux.*
Binaries for Linux  are available under [releases](https://github.com/ThamiMemel/UserMail_Converter/releases)
### Pypi
	$ pip install -U usermail-converter
to launch the app after installation use the command 
    $ usermail-converter


### Running from source
**Note** : Python 3.5 or higher is required, consider using a virtual environment to avoid packages conflict.

	# clone or download this git repository and enter it
	$ git clone https://github.com/ThamiMemel/usermail-converter.git && cd usermail-converter
	
	# install requirements
	$ pip install -r requirements.txt

	# To run this program
	$ python -m usermail_converter
	
	

# Modes
#### Email to Username 
	user@domaine.com > user
#### Email:Password to Username:Password
	user@domaine.com:pass > user:pass
#### Username to Email
	user > user@domain.com
#### Username:Password to Email:Password
	user:pass > user@domain.com:pass
## Disclaimer
By using this software, you agree that you are responsible for your actions when using it.


