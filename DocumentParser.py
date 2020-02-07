from PyPDF2 import PdfFileReader
import re

class DocumentParser:
    def __init__(self, docFile, type, mode):
        self.docFile = docFile
        self.type = type
        self.mode = mode
    
    def getWords(self):
        if self.type == "txt":
            return self.getWordsFromText()
        elif self.type == "pdf":
            return self.getWordsFromPDF()
        else:
            return 'Unknown type of file.'

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
        # creating a pdf file object 
        pdfFileObj = open(self.docFile, self.mode) 
        # creating a pdf reader object 
        pdfReader = PdfFileReader(pdfFileObj)
        # printing number of pages in pdf file 
        print(pdfReader.numPages) 
        # creating a page object 
        pageObj = pdfReader.getPage(0) 
        # extracting text from page 
        print(pageObj.extractText()) 
        # closing the pdf file object 
        pdfFileObj.close()
        