class List:
    def __init__(self, id, title, rev):
        self.id = id
        self.title = title
        self.revision = rev

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "revision": self.revision,
        }