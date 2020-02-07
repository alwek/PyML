from DocumentParser import DocumentParser
from dbmanager import DbManager

dp = DocumentParser("resources/example.txt", "txt", "r")
words = dp.getWords()
print(words)

db = DbManager()
db.connect()
print(db.version())
# print("AuthorId: " + str(db.insert_author("Alican Bircan")))
# print("Success: " + str(db.insert_author_list([
#         ("Bircan Alican",),
#         ("Alibir Cancan",)
#     ])))
print(db.delete_author(4))
db.disconnect()