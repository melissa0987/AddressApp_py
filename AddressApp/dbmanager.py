import click
from .db import Database
from flask import g, current_app
import os

from .db import Database

def get_db():
    if 'db' not in g:
        g.db = Database()
    return g.db

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    db.run_file(os.path.join(current_app.root_path, 'schema.sql'))

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initializing the database...')
