def calc_prod(lst=[]):
    def func_mut():
        a = lst[0]
        for num in lst[1:]:
            a *= num
        return a
    return func_mut

f = calc_prod([1,2,3,4])
print(f())

from functools import reduce
def calc_prod2(lst=[]):
    def func_mut():
        return reduce((lambda x,y:x*y), lst)
    return func_mut
f = calc_prod2([5,4,3])
print(f())