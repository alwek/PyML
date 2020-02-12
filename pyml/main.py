import os
from pyml.data.author import Author
from pyml.data.work import Work
from pyml.data.word import Word
from pyml.utlities.documentparser import DocumentParser
from pyml.database.dbmanager import DbManager

def run():
    dirpath = os.path.dirname(os.path.realpath(__file__))

    dp = DocumentParser(dirpath + "/resources/loremipsum.txt", "txt", "r")
    words = dp.getWords()
    print(words)

    db = DbManager()
    db.connect()
    print(db.version())
    db.disconnect()
