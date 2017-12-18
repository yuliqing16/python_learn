import mylib.time

mylib.time.print_time()

@mylib.time.perfomence
def printlog():
    print("MyLog")

#printlog()

from functools import *
@mylib.time.perfomence
def factorial(n):
    return reduce(lambda x,y:x*y, range(1, n+1))

for i in range(1,2):
    print(factorial(i))

import os
print(os.listdir(r"./"))

import json

print(json.dumps({"yq":"tiancai"}))

print(2 ** 2)