input_string = input("Please enter string: ")
words = input_string.lower().split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
unique_words = len(word_count)
for key in word_count:
    print("Word", str(key) + ": " + str(word_count[key]))
print("Unique words:", unique_words)
