def read_file(filename):
    """Define a function to read files"""
    try:
        with open(filename) as fo:
            contents = fo.read()
            print(contents)
    except FileNotFoundError:
        pass

filenames = 'cats.txt', 'dogs.txt'
for filename in filenames:
    read_file(filename)
