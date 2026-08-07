class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def print_cart(self):
        print(f"shopping cart is: {self.items}")