class List:
    def __init__(self, id, title, rev=0):
        self.id = id
        self.title = title
        self.revision = rev

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "revision": self.revision,
        }

    # def update_json_task(self):
    #     self.id = self.id
    #     self.title = self.title
    #     self.revision = self.revision + 1