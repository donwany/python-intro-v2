# Polymorphism: comes from the greek word, Poly: many, Morph: forms
# Different objects respond to the same method call in their own way
# or polymorphism allows different classes to use the same method name but implement that method differently

class CreditCard:
    def pay(self, amount):
        print(f"Credit card: ${amount}")


class ApplyPay:
    def pay(self, amount):
        print(f"ApplyPay: ${amount}")


class PayPal:
    def pay(self, amount):
        print(f"PayPal: ${amount}")


if __name__ == '__main__':
    payments = [CreditCard(), PayPal(), ApplyPay()]
    for payment in payments:
        payment.pay(amount=100)