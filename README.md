# Django Rest To Do

This is a Django Rest Framework project that implements a simple to-do list app with proper authentication and authorization.

## Features

1. To-do list endpoints for Django Rest Framework
2. Registration and authentication endpoints for Django Rest Framework.
3. Token-based authentication using django-rest-knox.
4. Proper form validation for all fields.
5. Custom paginator for pagination of to-do list.

## Installation

Before you start, consider that I implemented the project with [poetry@1.2.2](https://github.com/ahr9n/common-scripts/blob/main/python-poetry.sh), so if you need any troubleshooting; address the problem and [start an issue on this repository](https://github.com/ahr9n/django-rest-auth/issues/new). Here we go!

1. Clone the repository to your local machine, head to the project and convert to the `todos` branch:

```sh
git clone https://github.com/ah9rn/django-rest-auth.git
cd django-rest-auth
git checkout todos
git fetch
git pull
```

2. Set up the required environment variables by creating a `.env` file and filling in the values. You can use `.env.example` as a reference.

```sh
cp .env.example .env
```

3. Install all the required dependanies:

```sh
poetry install
poetry shell
```

4. Create and apply the Django migrations:

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

5. Run the development server:

```sh
python3 manage.py runserver
```

The project should now be running at http://localhost:8000/ and for testing, head to:

1. http://localhost:8000/auth/register
2. http://localhost:8000/auth/login
3. http://localhost:8000/auth/logout


## Getting Started

You can test the project using [Postman](https://www.postman.com/) or follow the following `curl` commands. This branch has more endpoints than [the Rest Registration endpoints](https://github.com/ahr9n/django-rest-auth/blob/main/README.md).

## For testing, use the following curl commands

1. Get to-dos:

```sh
curl -X GET -H "Authorization: Token <token>" http://localhost:8000/todos/
```

2. Get one to-do:

```sh
curl -X GET -H "Authorization: Token <token>" http://localhost:8000/todos/<id>
```

3. Create a new to-do:

```sh
curl -X POST -H "Authorization: Token <token>" -H "Content-Type: application/json" -d '{"title": "Test To Do", "description": "Test to-do description", "due": "2022-01-01", "completed": false}' http://localhost:8000/todos/
```

4. Update a to-do:

```sh
curl -X PUT -H "Authorization: Token <token>" -H "Content-Type: application/json" -d '{"title": "Test To Do", "description": "Test to-do description", "due": "2022-01-01", "completed": true}' http://localhost:8000/todos/<id>
```

5. Partially update a to-do:

```sh
curl -X PATCH -H "Authorization: Token <token>" -H "Content-Type: application/json" -d '{"title": "Updated To Do"}' http://localhost:8000/todos/<id>
```

6. Delete a to-do:

```sh
curl -X DELETE -H "Authorization: Token <token>" http://localhost:8000/todos/<id>
```

Don't forget to replace `<token>` and `<id>` with the actual token received from the [sign in endpoint](https://github.com/ahr9n/django-rest-auth/blob/main/README.md#sign-in-post-authlogin) and the to-do ID respectively.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ahr9n/django-rest-auth/blob/main/LICENSE) file for more details.
