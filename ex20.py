from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)

def prinf_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)
print("First all file content:")
print_all(current_file)

print("Let's rewind")
rewind(current_file)

print("3 lines:")

current_line = 1
prinf_a_line(current_line, current_file)

current_line += 1
prinf_a_line(current_line, current_file)

current_line += 1
prinf_a_line(current_line, current_file)

