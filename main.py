from models.Author import Author
from models.Work import Work
from models.Word import Word
from DocumentParser import DocumentParser
from dbmanager import DbManager


dp = DocumentParser("resources/loremipsum.txt", "txt", "r")
words = dp.getWords()
print(words)
print("Word count: " + str(len(words)))

authorToInsert = Author("Alican Bircan", None)
workToInsert = Work(authorToInsert.authorid, "A Novella", "English", 100, None)
wordToInsert = Word(workToInsert.workid, "Pickles", 1, 1, 1, False, None)

db = DbManager()
db.connect()
print(db.version())
# print("AuthorId: " + str(db.insert_author("Alican Bircan")))
# print("Success: " + str(db.insert_author_list([
#         ("Bircan Alican",),
#         ("Alibir Cancan",)
#     ])))
# print(db.delete_author(2))
db.disconnect()