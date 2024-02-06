# Galactic Atlas

The Galactic Atlas is an ORM written in vanilla python that can be interacted with via a CLI. It allows the user to input, update, delete, and retrieve information on stars, planets, civilizations, and species both real and fictional.

## Installation

### SQLite

To run this project, you will need SQLite installed on your system. Run the following command to check:

```bash
$ which sqlite3
/usr/bin/sqlite3
```

If you see the output above, you have a working version of sqlite3 already installed on your system. Otherwise, run the following command if you are on OSX:

```bash
brew install sqlite
```

For WSL, [Here are directions from Microsoft](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database#install-sqlite)

### Virtual Environment

Install and run the virtual environment with the following commands:

```bash
pipenv install
pipenv shell
```

## Usage

To initialize and seed the database, run `python lib/seed_db.py`.
To interact with the database, run `python lib/atlas.py`.
