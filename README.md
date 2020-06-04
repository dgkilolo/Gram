## Gram
- Gram is a python web application that has been made with Django. It is meant to be a clone of the popular application Instagram.
- Users are first required to sign in to in order to use the application. The registration is carried out using Django registation that eliminates the possibility of having bugs. The user can then use the navbar to scroll through the various page in the application as well as logging out.

### Required Features
- Sign in to the application to start using.
- Upload my pictures to the application.
- See my profile with all my pictures.

### Additional Features
- Follow other users and see their pictures on my timeline.
- Like a picture and leave a comment on it.

## Bugs
- Users are able to see pictures that have been posted by other users on their profile.

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)
- [Flask](http://flask.pocoo.org/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)

## Technologies & Languages

- Django 3.0.6
- Python 3.6.9
- Html
- Css
- Bootstrap4

# Installation and Setup

Clone the repository below

```
git clone https://github.com/dgkilolo/Gram.git
```

### Create and activate a virtual environment

    virtualenv venv --python=python3.6

    source venv/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

### Copy environment variable

    cp env.sample .env

### Load/refresh .environment variables

    source .env

## Running the application

```
python manage.py server
```


## Endpoints Available

| Method | Endpoint                        | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| POST   |        /auth/signup             | sign up a user                        | users         |
| POST   |        /accounts/login          | log in  a user                        | users         |
| POST   |        /accounts/logout         | logout a user                         | users         |
| POST   |        /new/image               | add a new image                       | users         |

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
Copyright{ 2020 }