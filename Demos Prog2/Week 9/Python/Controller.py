class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Set initial message text for the view
        self.view.set_message_text(self.view.groupName, str(self.model.getGroupName()))
        self.view.set_message_text(self.view.groupPrice, str(self.model.getGroupPrice()))
        self.view.set_message_text(self.view.groupCapacity, str(self.model.getGroupCapacity()))
        self.view.set_message_text(self.view.groupSold, str(self.model.getGroupSold()))
        self.view.set_message_text(self.view.groupIncome, "{:.2f}".format(float(0)))
        self.view.set_message_text(self.view.groupLeft, str(self.model.getGroupLeft()))

    def sell(self, quantity):
        try:
            self.model.sell(int(quantity))
            self.view.set_message_text(self.view.groupSold, str(self.model.getGroupSold()))
            self.view.set_message_text(self.view.groupLeft, str(self.model.getGroupLeft()))
            self.view.set_message_text(self.view.groupIncome, "{:.2f}".format(float(self.model.getGroupIncome())))
            self.view.set_text(self.view.sellTf, "0")
        except:
            pass


