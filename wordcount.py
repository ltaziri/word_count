def word_frequency(file_name):
    """return a dictionary that counts frequency of words in a file"""

    data_file = open(file_name)

    dict_word = {}

    for line in data_file:
        line = line.rstrip()
        words = line.split(" ")
        for word in words:
            dict_word[word] = dict_word.get(word, 0) + 1

    print dict_word
    return dict_word

    data_file.close()

word_frequency("test.txt")

