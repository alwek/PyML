from DocumentParser import DocumentParser

dp = DocumentParser("resources/example.txt", "txt", "r")
words = dp.getWords()
print(words)