#encoding:utf8
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
DBmanager = Manager()

@DBmanager.command
def init():
    print('数据库初始化完成')

@DBmanager.command
def migrate():
    print('数据库迁移成功')
    # migrate = Migrate(app, db)
