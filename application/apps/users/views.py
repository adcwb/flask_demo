from application import jsonrpc


@jsonrpc.method(name="Users.index")
def index(ret: str) -> str:
    """
        编写路由视图
        flask的路由是通过给视图添加装饰器的方式进行编写的。当然也可以分离到另一个文件中。
        flask的视图函数，flask中默认允许通过return返回html格式数据给客户端。
        路由和视图的名称必须全局唯一，不能出现重复，否则报错。
    :param ret:
    :return:
    """
    res = "hello" + ret
    return res
