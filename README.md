# HospitalRecordSystem
Prototype for a Desktop app to manage patient records

##Requirements
1. Python 2.7 or higher - https://www.python.org/downloads/
2. MySQL - https://dev.mysql.com/downloads/installer/
3. PyQt4
4. Peewee
(dependencies are not included)

##Installation
1. Clone the project
2. copy the `env_example.py` file as `env.py`
3. Replace the file contents with valid credentials.
4. Run the following command from inside the `databases/` directory - <br/>
  `python Hospital_Database.py`.
5. To run the app, type the following command - <br/>
  `python main.py`.
6. If the app is run on Windows, then start the SQL server and serve it on localhost (preferably via [WAMP](http://www.wampserver.com/en/))
