# FASTAPI Template App

This is a basic template for a [FastAPI](https://fastapi.tiangolo.com/lo/) based app for deployment using the [Serverless](https://www.serverless.com/) framework.

## Libraries used

The goal of this template is to provide a sane starting point for larger projects using FastAPI. I make use of the following libraries here:

- [Serverless](https://www.serverless.com/) - for handling deployment of the project to AWS Lambda/API Gateway
  - [serverless-prune-plugin](https://www.serverless.com/plugins/serverless-prune-plugin) - to purge previous deployed versions of functions from AWS lambda
- [cross-env](https://www.npmjs.com/package/cross-env) - for running node scripts across platforms
- [Poetry](https://python-poetry.org/) - For python packaging and dependency management (an alternative to virtualenv + pip)
- [PostgreSQL](https://www.postgresql.org/) - relational database
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM for managing database
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) - For database migrations
- [Pytest](https://pytest.org) - For running unit tests

## Python version

This project uses Python version 3.9. I have not tested it with other versions of Python.

## Requirements

If you intend to deploy using the [Serverless](https://www.serverless.com/) framework, first install serverless globally using command:

```
npm install -g serverless
```

If you don't plan to use serverless to deploy your app, you can delete the package.json, package-lock.json and serverless.yml files.

You will also need Python 3.9 and PostgreSQL installed locally to run this project.

## Customizing

Throughout this project, I use the project name `my-fastapi-app`. You will want to find/replace this with your own project name.

# Getting started

1. Add an empty local database + test database (code below assumes you already have the postgres command line tools and a local server setup):

```
createdb my-fastapi-app
ceratedb my-fastapi-app-test
```

2. Run migrate (this doesn't actually modify your database just yet... it just generates a migration script that we will run in the next step)

Note: this will setup with the dummy Foo model... if you are just getting started, you should run these commands right away to make sure everything is working. After that, see steps in section "Resetting the database" to start with a fresh DB.

```
python manage.py db migrate
# This is for local. For DEV or Prod, run:
# env=Development python manage.py db migrate
# env=Production python manage.py db migrate
```

3. Upgrade database (this is the step where the actual DB tables get modified/created)

```
python manage.py db upgrade
# This is for local. For DEV or Prod, run:
# env=Development python manage.py db upgrade
# env=Production python manage.py db upgrade
```

4. Run unit tests

```
pytest
```

5. Start the server

```
python manage.py runserver
# env=Development python manage.py runserver
# env=Production python manage.py runserver
```

Once the server is running, go to http://127.0.0.1:5000 to see the swagger docs and play around.

## Resetting the database

The steps above create a table called Foo. I provided this as an example template, but you probably want to define your own tables. To reverse the steps above:

1. Run this command to downgrade your database

```
python manage.py db downgrade
```

2. Delete the python script that was generate inside of the alembic/versions folder

3. Create your own models/tabels and rerun the steps above!
