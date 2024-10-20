from Group import Group

class Stadium:
    def __init__(self):
        self.group = Group("front", 300, 400.0)

    def getGroup(self):
        return self.group