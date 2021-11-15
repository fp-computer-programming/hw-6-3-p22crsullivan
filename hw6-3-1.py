# Author: CRS 11/15/21
word1 = list(input("Please enter a word."))
word2 = list(input("Please enter another word."))
word1.sort()
word2.sort()
if word1 == word2:
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
