# Cookiecutter_Django_REST-API_Template
A Cookiecutter Template that sets up a Django development environment and supports REST APIs.

Deploy Virtual Environment
```
python -m venv project_env
project_env\Scripts\activate.bat
```

Install Requirements
```
pip install -r requirements.txt
```

Download Cookiecutter Template
```
cookiecutter https://github.com/gem-tanvipenumudy/Cookiecutter_Django_REST-API_Template.git
```

Goto Directory
```
cd {{cookiecutter.project_name}}
```

Migrate & Run Server
```
python ./manage.py migrate
python ./manage.py showmigrations
python ./manage.py runserver
```

Check Functionality
```
curl -X GET http://127.0.0.1:port/{{cookiecutter.url}}/
curl -X POST -F "hello=world" http://127.0.0.1:port/{{cookiecutter.url}}/
```
