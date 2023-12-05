import random 
class Customer:
    def __init__(self, name):
        self.name = name
        self.order = None

    def place_order(self):
        menu = ["Burrito", "Quesadilla", "Chips", "Drink"]
        self.order = random.choice(menu)
        print(f"{self.name} placed an order for {self.order}.")

    def receive_order(self):
        print(f"{self.name} received {self.order}. Enjoy!")