# -*- coding:gbk -*-
'''''示例7: 在示例4的基础上，让装饰器带参数，
和上一示例相比在外层多了一层包装。
装饰函数名实际上应更有意义些'''

def deco(arg):
    def _deco(func):
        def __deco(x):
            print("before %s called[%s]."%(func.__name__, arg))
            func(x)
            print("after %s called[%s]." %(func.__name__, arg))
        return __deco
    return _deco

#myfunc=deco("mymodule")(myfunc)
@deco("mymodule")
def myfunc(x):
    print("myfunc() called.%r" % x)

myfunc("aaaa")