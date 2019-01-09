# Blog

A blog application that allows an author to write and publish articles for the public readers.

# Key Application Features

1. Creating, reading, updating and deleting articles by an admin user.
2. Viewing and reading articles by public users.

# Dependecies

- [Django 2.x](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)

# Setup Development

- Check that python 3 is installed

  ```
  python --v
  >> Python 3.6.5
  ```

- Install virtualenv

  ```
  pip install virtualenv
  ```

- Create a virtual environment

  ```
  virtualenv env
  source env\bin\activate
  ```

- Install python requirements

  ```
  pip install -r requirements.txt
  ```

- Make a copy of `.env.sample` file and rename it to `.env` and replace the variables with your postgres database credentials i.e

  ```
      DB_USER=your-database-user
      DB_PASSWORD=your-database-user-password
      DB_NAME=your-database-name
      DB_HOST=your-host
      PORT=5432
  ```

  then run `source .env`

- Run the migrations

  ```
  python ./manage.py migrate
  ```

- Run the application

  ```
  python ./manage.py runserver
  ```
