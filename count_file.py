def count_file(word):
    """Count special words in file"""
    with open(filename) as f:
        contents = f.read()
        number = contents.count(word)
        lower_word = contents.lower().count(word)
        print(number)
        print(lower_word)

filename = 'alice.txt'
count_file('the')
