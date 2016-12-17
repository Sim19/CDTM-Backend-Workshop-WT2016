class Task:
    NORMAL = 'normal'
    COMPLETED = 'completed'

    def __init__(self,  title, list, id=0, due='', status=NORMAL, descrip="", rev="1"):
        self.id = id
        self.title = title
        self.list = list
        self.status = status
        self.description = descrip
        self.due = due
        self.rev = rev

    def serialize(self):

        return{
            "id": self.id,
            "title": self.title,
            "list": self.list,
            "status": self.status,
            "description": self.description,
            "due": self.due,
            "revision": self.rev,
        }