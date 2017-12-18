tabby_cat = "\tI'amtabbed in"
persian_cat = "I'am split \non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_Cat="""
I'll do a list:
\t* Cat food
\t* Fishies
\f* New File
\v12333
\t* Catnip\n\t* Grass
\u1234
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_Cat)

print("12345", end="\r")
print("abc", end="\r")
import time

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        time.sleep(0.1)
        print("%s\r" % i, end="")
