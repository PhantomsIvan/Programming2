from Stadium import Stadium

class Model:
    def __init__(self):
        self.stadium = Stadium()
        self.group = self.stadium.getGroup()

    def sell(self, quantity):
        if self.group.canSell(quantity):
            self.group.sell(quantity)

    def getGroupName(self):
        return str(self.group.getName())

    def getGroupCapacity(self):
        return str(self.group.getCapacity())

    def getGroupPrice(self):
        return str(self.group.getPrice())

    def getGroupSold(self):
        return str(self.group.getSold())

    def getGroupIncome(self):
        return str(self.group.getIncome())

    def getGroupLeft(self):
        return str(self.group.getLeft())

