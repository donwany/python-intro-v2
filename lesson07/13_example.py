class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        return self

    def remove(self, item):
        self.items.remove(item)
        return self

    def show(self):
        print(self.items)
        return self


class Coffee:
    def __init__(self):
        self.order = []

    def milk(self):
        self.order.append("Milk")
        return self

    def sugar(self):
        self.order.append("Sugar")
        return self

    def whipped_cream(self):
        self.order.append("Whipped Cream")
        return self

    def display(self):
        print(self.order)
        return self


if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add("Laptop").add("Mouse").add("Keyboard").remove("Mouse").show()

    coffee = Coffee()
    coffee.milk().sugar().whipped_cream().display()
