def deco(func):
    print("before myfunc() called.")
    func()
    print("Aafter myfunc() called.")
    return func

#equal:myfunc=deco(myfunc)
@deco
def myfunc():
    print("myfunc() called.")

myfunc()