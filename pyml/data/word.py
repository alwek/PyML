class Word:
    wordid: int
    workid: int
    value: str
    appearancecount: int
    popularityindex: float
    sentenceindex: float
    misspell: bool

    def __init__(self, workid: int, value: str, appearancecount: int, popularityindex: float, sentenceindex: float, misspell: bool, wordid: int = None):
        self.wordid = wordid
        self.workid = workid
        self.value = value
        self.appearancecount = appearancecount
        self.popularityindex = popularityindex
        self.sentenceindex = sentenceindex
        self.misspell = misspell