word1 = input("Please enter the first word: ")
word2 = input("Please enter the second word: ")
word1_analysis = []
word2_analysis = []
for char in word1:
    word1_analysis.append(char)
for char in word2:
    word2_analysis.append(char)
for char in word1:
    if char in word2_analysis:
        word2_analysis.remove(char)
        word1_analysis.remove(char)
if len(word1_analysis) == len(word2_analysis) == 0:
    print("Annagrams")
else:
    print("Not anagrams")
