# Module for interacting with the static commands database.

from peewee import *
from playhouse.shortcuts import *


db = SqliteDatabase('../db/static_commands.db', pragmas={
        'journal_mode': 'wal',
        'cache_size': -1 * 64000,
        'foreign_keys': 1,
        'ignore_check_constraints': 0,
        'synchronous': 0})


class BaseModel(Model):
    class Meta:
        database = db


class Commands(BaseModel):
    name = CharField(unique=True)
    text = CharField()


def add_command(name, text):
    Commands.insert(name=name, text=text).execute()


def remove_command(name):
    Commands.delete().where(Commands.name == name).execute()


def edit_command(name, text):
    Commands.replace(name=name, text=text).execute()


def get_command(name):
    cmd = Commands.get_or_none(Commands.name == name)
    if cmd:
        return cmd.text


def get_command_list() -> {str: str}:
    return {c.name: c.text for c in Commands.select()}


def clear_commands():
    for cmd in Commands.select():
        cmd.delete_instance()


def create_table():
    db.create_tables([Commands])


def close_db():
    db.close()


if __name__ == '__main__':
    print(get_command_list())
