def deco(func):
    print("Before myfunc() called")
    func()
    print("After myfunc called.")
    return func

def myfunc():
    print("myfunc() called")

myfunc = deco(myfunc)

myfunc()
myfunc()