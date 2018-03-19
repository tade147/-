def read_file(filename):
    """Define a function to read files"""
    try:
        with open(filename) as fo:
            contents = fo.read()
            print(contents)
    except FileNotFoundError:
        print("Sorry, this file " + filename + " does not exsit!")

filenames = 'cats.txt', 'dogs.txt'
for filename in filenames:
    read_file(filename)
