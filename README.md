# Sample project for unit testing using pytests

This project focuses on unit testing using pytests.

## Setting up the project 
Please install virtualenv from [here](https://pypi.python.org/pypi/virtualenv), if you don't have it
 
## Getting to know the sample services

* Open the project directory
* Create a virtual environment using ```virtualenv python-unit-tests```
* Change directory to python-unit-tests ```cd python-unit-tests```
* Activate virtualenv ```source bin/activate```
* Install flask using: ```pip install flask```
* Install requests module using: ```pip install requests```
* Run the provider application: ```./provider_app.py```
* Run the consumer application: ```./consumer_app.py```
* To run tests: ```pytest provider_app_test.py```
* Check the REST the endpoints and understand what has been implemented for the provider application (http://127.0.0.1:5000/)
* Check the REST the endpoints and understand what has been implemented for the consumer application (http://127.0.0.1:5001/)

## License
[MIT](https://choosealicense.com/licenses/mit/)



