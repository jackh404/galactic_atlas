# Galactic Atlas

The Galactic Atlas is an ORM written in vanilla python that can be interacted with via a Command Line Interface. It allows the user to input, update, delete, and retrieve information on stars, planets, civilizations, and species both real and fictional using an SQLite database.

## Using the Atlas

Fork and clone this repository.

### To Run

**MacOS**: `mac/atlas`

**Linux**: `linux/atlas`

## Modifying the Atlas

### **Installation**

### SQLite

To install and modify this project, you will need SQLite installed on your system. Run the following command to check:

```bash
$ which sqlite3
/usr/bin/sqlite3
```

If you see the output above, you have a working version of sqlite3 already installed on your system. Otherwise, run the following command if you are on OSX:

```bash
brew install sqlite
```

For WSL, [Here are directions from Microsoft](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database#install-sqlite)

### Virtual Environment and pyinstaller

Install and run a python virtual environment of your choice and install dependencies. For example, use pipenv:

```bash
pipenv install
pipenv shell
```

## Usage

To run the app and interact with the database, use `python lib/atlas.py`.

### Structure

**lib**:

- app.py contains the main loop for the app and the upper level menus.
- helpers.py contains the functions and lower level menus called upon by app.py.
- seed.py contains the data to seed the database with. It is called by app.py if the database is empty or needs to be created.
- debug.py contains the simplest possible implementation of [ipdb](https://hasil-sharma.github.io/2017-05-13-python-ipdb/) for tracing and debugging. Run it with `python debug.py`

**lib/models**:

- **init**.py imports and initializes SQLite
- model.py contains the parent class for all models, and therefore much of the database logic
  - body.py contains the parent class for stars and planets
    - star.py contains the Star class corresponding to the stars table in the database
    - planet.py contains the Planet class corresponding to the planets table in the database
  - civilization.py contains the Civilization class corresponding to the civilizations table in the database
  - species.py contains the Species class corresponding to the species table in the database

### Build your project

Once you have made changes you are happy with, you can use [pyinstaller](https://pyinstaller.org/en/stable/usage.html) build your project and make an executable script. To do so, run the following command from the root directory:

```bash
pyinstaller --distpath <your platform> -F lib/atlas.py
```
