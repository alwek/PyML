import re
from PyPDF2 import PdfFileReader

class DocumentParser:
    def __init__(self, docFile, filetype, mode):
        self.docFile = docFile
        self.filetype = filetype
        self.mode = mode

    def getWords(self):
        if self.filetype == "txt":
            return self.getWordsFromText()
        elif self.filetype == "pdf":
            return self.getWordsFromPDF()
        else:
            return 'Unknown filetype of file.'

    def getWordsFromText(self):
        textFile = open(self.docFile, self.mode)
        lines = textFile.readlines()
        array = []
        regex = re.compile('[^a-zA-Z]')

        for line in lines:
            words = line.split()
            for word in words:
                array.append(regex.sub("", word))

        textFile.close()
        return array

    def getWordsFromPDF(self):
        pdfFileObj = open(self.docFile, self.mode)
        pdfReader = PdfFileReader(pdfFileObj)
        print(pdfReader.numPages)
        pageObj = pdfReader.getPage(0)
        print(pageObj.extractText())
        pdfFileObj.close()
        