from . import InitConfig


class Config(InitConfig):
    """项目开发环境下的配置"""

    DEBUG = True

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/flask?charset=utf8mb4"
    SQLALCHEMY_ECHO = True

    # session存储配置
    SESSION_REDIS_HOST = "127.0.0.1"
    SESSION_REDIS_PORT = 6379
    SESSION_REDIS_DB = 1

    # 日志配置
    LOG_LEVEL = "DEBUG"  # 日志输出到文件中的最低等级
    LOG_DIR = "/logs/moving.log"  # 日志存储目录
    LOG_MAX_BYTES = 300 * 1024 * 1024  # 单个日志文件的存储上限[单位: b]
    LOG_BACKUP_COUNT = 20  # 日志文件的最大备份数量
    LOG_NAME = "moving"  # 日志器名称

    # 注册蓝图
    INSTALLED_APPS = [
        "application.apps.users",
    ]
