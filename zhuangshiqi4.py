# -*- coding:gbk -*-
'''''ʾ��4: ʹ����Ƕ��װ������ȷ��ÿ���º����������ã�
��Ƕ��װ�������βκͷ���ֵ��ԭ������ͬ��װ�κ���������Ƕ��װ��������'''

def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("after myfunc() called.")
    return _deco

#myfunc=deco(myfunc)
@deco
def myfunc():
    print("myfunc() called")
    return 'ok'

myfunc()
myfunc()