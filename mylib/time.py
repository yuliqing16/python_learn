import time
def print_time():
    print("Print Time Function")

def perfomence(func):
    def _per(*args, **kwargs):
        before = time.time()
        ret = func(*args, **kwargs)
        print("Perfomnce:%r" % (time.time() - before))
        return ret
    return _per