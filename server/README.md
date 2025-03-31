# PersonalAIs: Generative AI Agent for Personalized Music Recommendations

Backend for PersonalAIs.
How to run it.

## Install Poetry:

Poetry is used to manage the dependencies of the project. You can install poetry by running the following command or you can visit the [official documentation](https://python-poetry.org/docs/#installation) for more information.

For the purpose of making sure that the project runs smoothly (the commands below run as expected), use Poetry (version 1.8.4), that's what I have used to develop the project.

```bash
pipx install poetry==1.8.4
```

## Activate the Shell:
    
```bash
poetry shell
```

## Install the dependencies:

```bash
poetry install
```

## Running in development mode:

```bash
poe dev
```

## Running in production mode:

```bash
poe start
```

# How to see the api documentation:
- First run the server in development mode as shown above. [here](#running-in-development-mode)
- Then head over to the following link, and a swagger documentation will be available for you to see the api documentation.
```bash
http://localhost:8000/docs
```


