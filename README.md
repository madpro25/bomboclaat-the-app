# bomboclaat-the-app

A Discord bot.

## Setting up

To set up, I would recommend creating a virtual environment.
To run the app, run the following commands:

```sh
git clone https://github.com/Colocasian/bomboclaat-the-app.git
cd bomboclaat-the-app

# Create a python venv
python -m venv venv
source ./venv/bin/activate

# Install the requirements
pip install -r ./requirements.txt

# For a dev setup, install dev requirements and setup pre-commit hooks
pip install -r ./requirements-dev.txt
pre-commit install
```
