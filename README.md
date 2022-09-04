# Template for Vue-Flask CRUD Web application
This is a template to build web application with Vue.js for Frontend, Python Flask for backend, and Gunicorn as WSGI.

## What is good about this template?
### Flask part
As a whole, you can avoid thousands of lines in any files with reasonable directory structures,<br>
even if you try to increase the number of behaviours against GET, POST, PUT, and DELETE request<br>
and database tables, etc. For more details, it does the follow.
* Uses blueprint to manage auth, app, api and others separately for larger application by default
* Database tables can be increased in a scalable way, but can be used across blueprints
root<br>
   ├──server<br>
   │    ├──flask_app.py    <- Create Flask instance and provide create_app() func used by gunicorn<br>
   │    ├──gunicorn.py   <- Call gunicorn from python, after loading env vars<br>
   │    ├──config.py   <- Config used when creating Flask<br>
   │    ├──requirements.txt   <- pip freeze results at initial state<br>
   │    ├──main   <- Implement main contents, starting from route('/')<br>
   │    │    ├──__init__.py<br>
   │    │    ├──views.py    <- You can split this file for large scala application<br>
   │    │    ├──...<br>
   │    │<br>
   │    ├──app    <- Majorly implement anything starting from route('/app')<br>
   │    │    ├──__init__.py<br>
   │    │    ├──views.py<br>
   │    │    ├──...<br>
   │    │<br>
   │    ├──api<br>
   │    │    ├──__init__.py<br>
   │    │    ├──sample.py<br>
   │    │    ├──...<br>
   │    │<br>
   │    ├──auth<br>
   │    │    ├──__init__.py<br> 
   │    │    ├──views.py<br>
   │    │    ├──...<br>
   │    │<br>
   │    └── models<br>
   │         ├──__init__.py<br> 
   │         ├──db.py<br>
   │         ├──user.py<br>
   │         ├──...<br>
   ├──...<br>

## Requisites
In order to use this template, you'll need to have the follows.
* Python3
* npm
* node (required for npm)

For setting up python3, use of virtualenv is recommended.<br>
[Here](https://github.com/daichi-yoshikawa/python-boilerplate) is one of instructions for virtualenv(See (Option2) Create virtualenv).

As for npm (and node), [here](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/) is a great instruction.

## Get Started

Firstly, do the follows with one terminal. This is to bundle/compile client scripts(html, css, js, vue). The resulting files will be generated in client/dist/dev dir.
```
$ git clone https://github.com/daichi-yoshikawa/vue-flask-boilerplate
$ cd <path-to-vue-flask-boilerplate>
$ cd client
$ npm install
$ npm
```

And then, do the follows with another terminal.
```
$ cd <path-to-vue-flask-boilerplate>
$ cd server
```
If you use pyenv and pyenv-virtualenv, do the follows to set python virtualenv to the directory.
```
$ pyenv install <version of python(Eg. 3.7.6)>
$ pyenv virtualenv <version of python(Eg. 3.7.6)> <venv name(Eg. py376-webapp)>
$ cd <path-to-vue-flask-boilerplate>/server
$ pyenv local <venv name(Eg. py376-webapp)>
```
And run python file under server dir.
```
$ python gunicorn.py
```

Now you can check if everything is going well by opening browser and input "localhost:5000" in URL bar. You'll see like below.<br>

![Image of sample page](https://raw.githubusercontent.com/daichi-yoshikawa/personal-assets/master/vue-flask-boilerplate/sample_page_screenshot.png)

Also, uncomment the lines in server/flask_app.py to activate api, try "localhost:5000/api/sample" then you'll get JSON format response {"Hello": "RESTful API world"}.
```
from api import api_blueprint
flask_app.register_blueprint(api_blueprint, url_prefix='/api')
```

## How to extend code
### Backend (Flask)
#### Add more routes
Regarding routes, especially for GET method, implement in server/app/views.py.

#### Add more RESTful APIs
To implement RESTful APIs, create new python file to implement API in server/api. And then implement API with Resource class provided by flask-RESTful package as sample.py is implemented. Once you implemented API, edit server/api/\_\_init\_\_.py like below.
```
from flask import Blueprint
from flask_restful import Api

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

from .your_api import YourAPI

api.add_resource(YourAPI, '/your_api')
```

#### Add more DB tables
server/models directory is the place to add more DB tables. You create python file to implement DB table with SQLAlchemy. Here is an example of implementation.
```
from datetime import datetime

from .db import db


class User(db.Model):
  name = 'users'
  __tablename__ = 'users'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(255), nullable=False, unique=True)
  created_at = db.Column(db.DateTime(), default=datetime.utcnow)
  updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
```

And then, add new module you created to server/models/\_\_init\_\_.py like below.
```
from .user import User # Add this line.
```

Once you defined models, you do the follows. Note that flask db init is only needed when you don't have migrations dir in server dir.
```
$ cd <path to server dir>
$ export FLASK_APP=flask_app:create_app
$ flask db init
$ flask db migrate -m "Initial migration."
$ flask db upgrade
```

### Frontend (Vue.js)
#### Add more 3rd party js files
#### Add more your own js files
#### Add more Vue components
#### Add more Vue routes
