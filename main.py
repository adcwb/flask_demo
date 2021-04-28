from application import init_app

# 初始化项目配置文件
manage = init_app("application.settings.dev")


@manage.app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    manage.run()
