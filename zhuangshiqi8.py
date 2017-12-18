# -*- coding:gbk -*-
'''''ʾ��8: װ�����������'''

class locler:
    def __init__(self):
        print("locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        print("locker.acquire() called.")

    @staticmethod
    def release():
        print("locker.release() called.")

def deco(cls):
    '''''cls ����ʵ��acquire��release��̬����'''
    def _deco(func):
        def __deco():
            print("before %s called[%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco

@deco(locler)
def myfunc():
    print("myfunc() called.")

myfunc()