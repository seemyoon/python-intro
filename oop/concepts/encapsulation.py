# Encapsulation
class Email:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send_email(self):
        pass

    def read_email(self):
        pass
