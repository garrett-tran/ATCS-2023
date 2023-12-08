import random 
class Customer:
    def __init__(self):
        self.order = None

    def place_order(self):
        menu = ["chips", "burrito",]
        self.order = random.choice(menu)
        print(f"Customer placed an order for {self.order}.")
        return self.order

    def receive_order(self):
        print(f"Customer received {self.order}. Enjoy!")