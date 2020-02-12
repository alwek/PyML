class Author:
    authorid: int
    name: str

    def __init__(self, name: str, authorid: int = None):
        self.authorid = authorid
        self.name = name