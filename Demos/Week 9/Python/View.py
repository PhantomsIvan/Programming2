import tkinter as tk

class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create labels
        self.groupLabel = tk.Label(self, text="Seat Group:")
        self.groupLabel.grid(row=0, column=0, sticky=tk.W)

        self.capacityLabel = tk.Label(self, text="Capacity:")
        self.capacityLabel.grid(row=1, column=0, sticky=tk.W)

        self.priceLabel = tk.Label(self, text="Price ($):")
        self.priceLabel.grid(row=2, column=0, sticky=tk.W)

        self.soldLabel = tk.Label(self, text="Sold:")
        self.soldLabel.grid(row=3, column=0, sticky=tk.W)

        self.leftLabel = tk.Label(self, text="Left:")
        self.leftLabel.grid(row=4, column=0, sticky=tk.W)

        self.incomeLabel = tk.Label(self, text="Income ($):")
        self.incomeLabel.grid(row=5, column=0, sticky=tk.W)

        self.sellLabel = tk.Label(self, text="Sell:")
        self.sellLabel.grid(row=6, column=0, sticky=tk.W)

        # Create message fields
        self.groupName = tk.Message(self, justify=tk.LEFT, text="", width=300)
        self.groupName.grid(row=0, column=1, sticky=tk.W)

        self.groupCapacity = tk.Message(self, justify=tk.LEFT, text="", width=300)
        self.groupCapacity.grid(row=1, column=1, sticky=tk.W)

        self.groupPrice = tk.Message(self, justify=tk.LEFT, text="", width=300)
        self.groupPrice.grid(row=2, column=1, sticky=tk.W)

        self.groupSold = tk.Message(self, justify=tk.LEFT, text="", width=300)
        self.groupSold.grid(row=3, column=1, sticky=tk.W)

        self.groupLeft = tk.Message(self, justify=tk.LEFT, text="", width=300)
        self.groupLeft.grid(row=4, column=1, sticky=tk.W)

        self.groupIncome = tk.Message(self, justify=tk.LEFT, text="", width=300)
        self.groupIncome.grid(row=5, column=1, sticky=tk.W)

        # Entry fields
        self.sellTf = tk.Entry(self)
        self.sellTf.grid(row=6, column=1, sticky=tk.W)

        # Set default value for sellTf
        self.set_text(self.sellTf, "0")

        # Button
        self.sellBtn = tk.Button(self, text="Sell", command=self.sell_button_clicked)
        self.sellBtn.grid(row=7, column=1, sticky=tk.E)

        # Set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def sell_button_clicked(self):
        if self.controller:
            try:
                # Attempt to call the sell method in the controller
                self.controller.sell(self.sellTf.get())
            except Exception as e:
                print(f"An error occurred: {e}")
                pass

    def set_message_text(self, mf, text):
        mf.configure(text=text)

    def set_text(self, tf, text):
        tf.delete(0, tk.END)
        tf.insert(0, text)
