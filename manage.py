# encoding:utf8

from flask_script import Manager
from hello import app
from exts import db
from flask_migrate import Migrate, MigrateCommand
from models import Article, User

# from db_scripts import DBmanager
# manager.add_command('db', DBmanager)

manager = Manager(app)
# migrate 必须绑定app， db
migrate = Migrate(app, db)
# 把migrate命令传给flask——script
manager.add_command('db', MigrateCommand)

# 为什么要使用`migrate`，`app.create_all()`只负责映射表元素，如果数据库表新增字段或者修改字段，就必须先drop表，然后重新映射，但是drop表会清空数据，而migrate可以保证数据迁移的同时，修改或新增字段

# 使用命令
# 1：初始化使用，在当前目录下运行命令`python manage.py db init`
# 2: 迁移命令`python manage.py db migrate`
# 3: 更新数据库表 `python manage.py db upgrade`
# 注：若使用python3执行该任务报错`python3.5/dist-packages/MySQLdb/connections.py", line 36 raise errorclass, errorvalue`，原因是`python3`不再支持mysqldb驱动，可以使用mysqlclient替代，`sudo python3 -m pip install mysqlclient`

@manager.command
def runserver():
    print('服务器跑起来了')
    app.run(debug=True)

if __name__ == '__main__':
    manager.run()
