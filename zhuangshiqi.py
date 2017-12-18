
def mylog(func):
    def f(*argx):
        print("call ", func.__name__, ";")
        return func(*argx)
    return f

@mylog
def myadd(x):
    return x*x

print(myadd(5))

@mylog
def myadd2(x,y):
    return x+y
print(myadd2(3,4))


def print_log(s):
    print(s)

#-*- encoding=utf-8 -*-
from functools import wraps

def task_logging(taskname):
    def func_wrapper(func):
        @wraps(func)
        def return_wrapper(*args, **wkargs):
            # 函数通过装饰起参数给装饰器传送参数
            print('before task',taskname)
            # 装饰器传变量给函数
            taskid = 1
            summer, funcres = func(taskid, *args, **wkargs)
            print('after task', taskid, summer)
            return funcres
        return return_wrapper
    return func_wrapper

@task_logging("test")
def testd(taskid):
    print("testd runing",taskid)
    return "task summer success eg", []

print(testd())


def mylog2(a):
    def f(func):
        print("call ", func.__name__, ";", a)
        return func()
    return f

@mylog2(33)
def addd():
    return 33333

#print(addd())

def zsq(a):
  print('我是装饰器的参数', a)
  def nei(func):
    print('我在传入的函数执行之前做一些操作')
    func() # 执行函数
    print('我在目标函数执行后再做一些事情')
  return nei


@zsq('123')
def login():
  print('我进行了登录功能')