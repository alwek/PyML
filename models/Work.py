class Work:
    workid: int
    authorid: int
    name: str
    language: str
    totalwords: int

    def __init__(self, authorid: int, name: str, language: str, totalwords: int, workid: int = None):
        self.workid = workid
        self.authorid = authorid
        self.name = name
        self.language = language
        self.totalwords = totalwords

