# 定义任务
from .SXHGB_V4.find_peixun import find_peixun_url
from .SXHGB_V4.login import login
from .SXHGB_V4.peixun import peixun
from django_redis import get_redis_connection

from celery import Celery
app = Celery('my_web', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')
#在这里添加你的后台任务方法代码，并注解task
# from my_web.celery import app


@app.task
def sxhgb_study():

    """山西好干部在线学习的异步任务"""

    redis_conn = get_redis_connection('default')
    username = str(redis_conn.get('username'))
    password = str(redis_conn.get('password'))
    name = (redis_conn.get('name')).decode()
    print(username)

    login(username, password, name)
    find_peixun_url()
    peixun()
