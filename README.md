# Dqbug Django Project #
## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages dqbug-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages dqbug-env
cd dqbug-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> dqbug
```

### Install requirements ###
```bash
cd dqbug
pip install -r requirements.txt
```

### Configure project ###
```bash
cp dqbug/__local_settings.py dqbug/local_settings.py
vi dqbug/local_settings.py
```

### Sync database ###
```bash
python manage.py syncdb
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000
