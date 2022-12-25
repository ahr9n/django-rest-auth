# Django Rest Registration

This is a Django Rest Framework project that implements registration and authentication APIs using django-rest-knox.

## Features

1. Registration and authentication endpoints for Django Rest Framework.
2. Token-based authentication using django-rest-knox.
3. Proper form validation for all fields.

## Installation

Before you start, consider that I implemented the project with [poetry@1.2.2](https://github.com/ahr9n/common-scripts/blob/main/python-poetry.sh), so if you need any troubleshooting; address the problem and [start an issue on this repository](https://github.com/ahr9n/bulletin-board-system/issues/new). Here we go!

1. Clone the repository to your local machine and head to the project:

```sh
git clone https://github.com/ah9rn/django-rest-auth.git
cd django-rest-auth
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

You can test the project using [Postman](https://www.postman.com/) or follow the following `curl` commands. The project includes the following endpoints:

## Sign up (POST /auth/registration/)

This endpoint allows users to create a new account by providing their name, email, password, and date of birth. Proper form validation is implemented, including checks for required fields, valid email addresses, strong passwords, and correct date of birth format.

To sign up, you can use the following `curl` command:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"name": "Test User", "email": "test@example.com", "password1": "password123", "password2": "password123", "date_of_birth": "1995-12-01"}' http://localhost:8000/auth/registration/
```

## Sign in (POST /auth/login/)

This endpoint allows users to sign in using their email and password. Token-based authentication is implemented using django-rest-knox, and the endpoint returns the token and a representation of the user in JSON format.

To sign in, you can use the following `curl` command:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"email": "test@example.com", "password": "password123"}' http://localhost:8000/auth/login/
```

## Sign out (POST /auth/logout/)

This endpoint allows users to sign out by invalidating the token provided. To sign out, you will need to include the token received from the sign in endpoint in the headers of your request. You can use the following `curl` command:

```sh
curl -X POST -H "Authorization: Token <token>" http://localhost:8000/auth/logout/
```

Don't forget to replace `<token>` with the actual token received from the sign in endpoint.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ahr9n/django-rest-auth/blob/main/LICENSE) file for more details.
