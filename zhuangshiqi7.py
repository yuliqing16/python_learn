# -*- coding:gbk -*-
'''''ʾ��7: ��ʾ��4�Ļ����ϣ���װ������������
����һʾ�������������һ���װ��
װ�κ�����ʵ����Ӧ��������Щ'''

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