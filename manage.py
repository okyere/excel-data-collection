#!env/Scripts/python

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

from app import theapp, db
theapp.config.from_object('config')

migrate = Migrate(theapp, db)
manager = Manager(theapp)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
