# -*- coding:gbk -*-
'''''示例6: 对参数数量不确定的函数进行装饰，
参数用(*args, **kwargs)，自动适应变参和命名参数'''

def deco(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("after %r called,result :%r" %(func.__name__, ret))
        return ret
    return _deco

@deco
def myfunc(a,b):
    print("myfunc(%r,%r) called." %(a,b))
    return a+b

@deco
def myfunc2(a,b,c):
    print("myfunc(%r,%r,%r) called." %(a,b,c))
    return a+b+c

myfunc(1,3)
myfunc2(4,3,1)