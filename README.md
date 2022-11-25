# REST REGISTERATION

## Getting Started

After cloning the repository, refer to the project folder and:

```sh
$ poetry install
$ poetry shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

For testing, head to 
* http://localhost:8000/auth/register
* http://localhost:8000/auth/login
* http://localhost:8000/auth/logout

For logout make sure to open settings.py to change `DEBUG` and `ALLOWED_HOSTS` as in comments there.

1. You can use postman to send the token in the headers using knox token
2. Or via the command
```sh
$ curl -X POST -H "Authorization: Token <token>" http://localhost:8000/auth/logout/
```

_Notice the last slash for testing logging out!_