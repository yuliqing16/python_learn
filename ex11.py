print("How old are you", end="")
age = input()
print("Hoe tall are you?", end="")
height= input()
print("How much do you weight?", end="")
weight= input()

print("So, you're %d old, %r tall, %r heavy." % (
    int(age), height,weight
))