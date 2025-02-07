# Abstraction
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class CreditCardPayment(Payment):
    def __init__(self):
        pass

    def process_payment(self):
        print("Processing credit card payment...")


class StripePayment(Payment):
    def __init__(self):
        pass

    def process_payment(self):
        print("Processing Stripe payment...")


class PayPalPayment(Payment):
    def __init__(self):
        pass

    def process_payment(self):
        print("Processing PayPal payment...")


payments = [CreditCardPayment(), StripePayment(), PayPalPayment()]

for payment in payments:
    payment.process_payment()
