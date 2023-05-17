# LWTech Capstone Project

Welcome to the LWTech capstone project! The idea of this project is to create a game world that players can interact with programmatically to improve their programming ability while having fun. 

This project is in it's early stages so keep an eye out for future improvements!

## Setup

### Dependencies
Running the following commands will install the dependencies for the project.
```
python -m pip install flask pymongo[srv]
``` 

### Configuration
#### db.config
You need a `db.config` file containing a MongoDB connection string in the top level of the project so the app can load the database.

If you are getting an error like "File db.config" does not exist this is why.

## Running The Server
Use these commands to start the Flask server. Running the server in development mode like shown here will reload the server when changes are made.


### Flask 2.2.0
If you just installed flask this is the option to choose.
```bash
python -m flask --debug run
```

### Flask 2.0.0
If you're using an older version of flask you have to set some environment variables first.
### Windows CMD
```cmd
set FLASK_APP=app.py
set FLASK_ENV=development
python -m flask run
```

### Windows PowerShell
```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development
python -m flask run
```

### Bash
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
python -m flask run
```
