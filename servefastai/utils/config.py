"""Utilities to read, write and manage the system-wide configuration"""
from pathlib import Path
from getpass import getpass
import sqlite3
import json
import stat
import os

CONFIG_DIR = Path.home()/'.servefastai'
CONFIG_FNAME = 'config.json'
DB_FNAME = 'sqlite.db'


def create_config_dir():
    """Create the config directory if it doesn't exist"""
    if not CONFIG_DIR.exists():
        print(f'[servefastai] Creating configuration directory "{CONFIG_DIR}"')
        CONFIG_DIR.mkdir(exist_ok=True, parents=True)


def init_config_file(force=False):
    """Create (or clear) the config.json file"""
    path = CONFIG_DIR/CONFIG_FNAME
    if force or not path.exists():
        with open(path) as f:
            print(f'[servefastai] Creating configuration file "{path}"')
            json.dump({}, f)


def init_db(force=False):
    """Create (or clear) the local database"""
    path = CONFIG_DIR/DB_FNAME
    if force or not path.exists():
        print(f'[servefastai] Creating local database "{path}"')
        conn = sqlite3.connect(path)
        conn.close()
