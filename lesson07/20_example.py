# Abstract Classes:
# Imagine you are building an e-commerce website, and customers can use: credit card, paypal, applepay, cashapp, bitcoin etc
# every payment method must have a pay() method, instead of letting the developers forget to implement it, we can force them
# to use abstract class. Without abstract class, one developer can write pay(), another writes make_payment(), another
# checkout(), chaos!. With abstract class, every developer must implement pay().
# Note: An abstract method is normally not implemented in the abstract base class. It defines what subclasses must implement.

from abc import ABC, abstractmethod


# Abstract base class
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using credit card")


class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using paypal")


if __name__ == '__main__':
    cc = CreditCard()
    cc.pay(100)

    pp = PayPal()
    pp.pay(50)
