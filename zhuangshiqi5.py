# -*- coding:gbk -*-
'''''ʾ��5: �Դ������ĺ�������װ�Σ�
��Ƕ��װ�������βκͷ���ֵ��ԭ������ͬ��װ�κ���������Ƕ��װ��������'''

def deco(func):
    def _deco(a,b):
        print("before myfunc() called.")
        ret = func(a,b)
        print("after myfunc called. result:%s" % ret)
        return ret
    return _deco

#myfunc=deco(myfunc)
@deco
def myfunc(a,b):
    print("myfunc(%r,%r) called" % (a,b))
    return a+b

myfunc(4,5)