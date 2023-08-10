## Requirements
* Brew
  * For installation see: https://docs.brew.sh/Installation
* Python
  *  v3.10.0 (exact version) using [Pyenv](https://github.com/pyenv/pyenv)
      * `brew install pyenv`
      * `pyenv install 3.10.0`
      * `pyenv versions` to confirm that **3.10.0** is in the list of Python versions
  * Inside the project directory
      * `rm -rf .venv` to remove old environment
      * `pyenv local 3.10.0` to set specific Python version at project level (not OS level)
      * `python --version` to check if it's **3.10.0**. If not, then
          * `echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc` or `~/.bash_profile`
          * `echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc` or `~/.bash_profile`
          * `echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc` or `~/.bash_profile`
      * Re-open shell and `python --version` to check if it's **3.10.0** at project level
* Poetry
  * `pip install poetry`
  * Inside the project directory
      * `poetry shell` to activate poetry virtual environment
      * `python --version` to confirm that **3.10.0** inside the environment as well

## Setup the development environment
* Confirm you have all system requirements above
* Clone the repository to your local machine
* Download & install dependencies by running `poetry install`


## Working with requirements/dependencies
 - For adding a requirement, you can run: `poetry add {requirement}`
 - For adding a dev requirement, you can run: `poetry add {requirement} --dev`
 - For updating a requirement, you can run: `poetry update {requirement}`
 - For removal of a requirement, you can run: `poetry remove {requirement}`

-------------------------------------------------
## Run the server
- `uvicorn IoTDashboard.app:app --host 0.0.0.0 --port 80 --reload`

## Run lint & format
- `isort .` - sort package imports
- `black .` - format the code

## Testing
- `pytest` - test all directories
- `pytest {path to specific test file}`

-------------------------------------------------
## Run the stack using docker
- `docker compose up`
- If you change the project dependencies make sure to include the **--build** to rebuild the image with the right dependencies.

## Generate new migrations
- `docker compose run app alembic revision --autogenerate -m "Your migration message"` - **app** is the docker compose service

## Run migrations
- `docker compose run app alembic upgrade head` - to apply migrations
- `docker compose run app alembic downgrade {revision}` - to revert migrations to specific revision state

## Testing
- `docker compose run app pytest`
- `docker compose run app pytest {path to specific test file}`

---------------------------------------------


