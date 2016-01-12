def word_frequency(file_name):
    """return a dictionary that counts frequency of words in a file"""

    data_file = open(file_name)

    dict_word = {}

    punctuations_to_remove = [',', '.', '!', '?', '-', '--', 
                              '/', '\\', ':', '"', ';', '_']

    for line in data_file:


        line = line.rstrip()
        words = line.split(" ")

        cleaned_words = []

        for word in words:
            for symbol in punctuations_to_remove:
                word = word.strip(symbol)
            cleaned_words.append(word)
        
        lower_words = [word.lower() for word in cleaned_words]

        # lower_words = []
        # for word in words:
        #     lower_words.append(word.lower())


        for word in lower_words:
            dict_word[word] = dict_word.get(word, 0) + 1


    for key, value in dict_word.iteritems():
        print key, value

    return dict_word

    data_file.close()

word_frequency("test.txt")
word_frequency("twain.txt")


