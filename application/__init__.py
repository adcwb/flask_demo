import os

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_session import Session
from flask_migrate import Migrate, MigrateCommand
from flask_jsonrpc import JSONRPC

from application.utils import init_blueprint
from application.utils.config import load_config
from application.utils.session import init_session
from application.utils.logger import Log
from application.utils.commands import load_command

# 创建终端脚本管理对象
manager = Manager()

# 创建数据库链接对象
db = SQLAlchemy()

# redis链接对象
redis = FlaskRedis()

# Session存储对象
session_store = Session()

# 数据迁移实例对象
migrate = Migrate()

# 日志对象
log = Log()

# 初始化jsonrpc模块
jsonrpc = JSONRPC(service_url='/api')


def init_app(config_path):
    """
        全局初始化

        import_name      Flask程序所在的包(模块)，传 __name__ 就可以
                         其可以决定 Flask 在访问静态文件时查找的路径
        static_path      静态文件访问路径(不推荐使用，使用 static_url_path 代替)
        static_url_path  静态文件访问路径，可以不传，默认为：/ + static_folder
        static_folder    静态文件存储的文件夹，可以不传，默认为 static
        template_folder  模板文件存储的文件夹，可以不传，默认为 templates

    """
    # 创建app应用对象
    app = Flask(import_name=__name__)

    # 设置项目根目录
    app.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 加载配置
    # flask中支持多种配置方式，通过app.config来进行加载，我们会这里常用的是配置类
    Config = load_config(config_path)
    app.config.from_object(Config)

    # 数据库初始化
    db.init_app(app)
    redis.init_app(app)

    # session存储初始化
    init_session(app)
    session_store.init_app(app)

    # 数据迁移初始化
    migrate.init_app(app, db)

    # 添加数据迁移的命令到终端脚本工具中
    manager.add_command('db', MigrateCommand)

    # 日志初始化
    app.log = log.init_app(app)

    # 蓝图注册
    init_blueprint(app)

    # 初始化json-rpc
    jsonrpc.init_app(app)

    # 初始化终端脚本工具
    manager.app = app

    # 注册自定义命令
    load_command(manager)

    return manager
