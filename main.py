from DocumentParser import DocumentParser

dp = DocumentParser("/home/alwek/Projects/PyML/resources/example.txt", "txt", "r")
words = dp.getWords()
print(words)