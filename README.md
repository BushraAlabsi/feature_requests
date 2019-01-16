# Feature Requests

#### The app is live at:

http://ec2-3-86-248-156.compute-1.amazonaws.com/ 


## Stack
1. **Python 2.7.15** 
2. **Flask** - Python micro framework.
4. **SQLAlchemy** - Database ORM
5. **MySQL** .
6. **Boostrap V4 and Jquery** 
7. **KnockoutJS** - Javascript library used for dynamic UI.


## Infrastructure
1. **AWS EC2:** The app is running on an AWS EC2 instance.
2. **Ubuntu 18.04 LTS:** The OS used is the Ubuntu 16.04 provided by AWS.
3. **Database**: The MySQL production instance is running on the same machine.
4. **Static Files**: No service like AWS S3 or CDN is being used.

## Setting Up Environment

1. SECRET KEY: the secret key is used by the system to protect from csrf attacks, and it is required to the forms, any string could work as a secret key but generating a random hex would be more secure


2. SQLALCHEMY_DATABASE_URI: This is the uri for the database that you're using, sqlalchemy 	supports many database systems, you can use the database system that you are comfortable with, here are the two options; sqlite3 and mysql that were used in this project:

sqlite:///request.db  (for developement)
mysql+pymysql://yourusername:yourpassword@yourserver/request (for deployment)  

to set these variable in the system on Ubuntu:

open your bash_profile file:
```nano ~/.bash_profile```

add these two line and then save the file:

``` export SECRET_KEY='YOUR_SECRET_KEY' `
``  export SQLALCHEMY_DATABASE_URI='YOUR_DATABASE_URI' ```


**if you chose mysql, you need to create the database first, ony way of doing that is from your terminal:**
``` sudo mysql -u username -p ``` Note: sudo is optional unless you are using mysql version 5.7 or higher, and using the root user.

``` CREATE DATABASE request ```

## Running Locally
make sure to go through setting up enviroment before continuing on tis section

I. clone this repository, or download it 
```git clone ```

II. create a virtual environment (this step is optional you can download the dependencies globally on your machine)
	
	1.install virtualenv:
	
	```pip install virtualenv ```
	
	2. create a virtual environment by navigating to the path you want to add it to:
	
	``` virtualenv name ```
	
	3.activate the virtual machine that you have created:
	
	``` source name/bin/activate```

III. navigate into this repository in your terminal and install dependecies:
``` pip install -r requirements.txt```

IV. create tables and insert clients and product area:
```python create_database.py ```

V. run the app:
```python run.py ```

now the application is running on localhost:5000

## Running Tests
make sure to go through setting up enviroment before continuing on tis section

To run the test, from within the root directory:

`` python manage.py test ``


