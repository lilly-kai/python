import sys
#one command-line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
#check for python file
filename = sys.argv[1]
if not filename.endswith(".py"):
    sys.exit("Not a Python file")
#start counting lines(except empty and # lines)
count = 0
try:
    with open(filename) as file:
        for line in file:
            stripped = line.lstrip()
            if stripped != "" and not stripped.startswith("#"):
                count += 1
        print(count)
except FileNotFoundError:
    sys.exit("File does not exist")
