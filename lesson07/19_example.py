class Email:
    def send(self):
        print("Email sent")


class SMS:
    def send(self):
        print("SMS sent")


class PushNotification:
    def send(self):
        print("Push notification sent")


class GPT:
    def generate(self):
        print("Generating with GPT...")

class Claude:
    def generate(self):
        print("Generating with Claude...")

class Gemini:
    def generate(self):
        print("Generating with Gemini...")


if __name__ == '__main__':

    notifications = [Email(), SMS(), PushNotification()]
    for notification in notifications:
        notification.send()

    models = [GPT(), Claude(), Gemini()]
    for model in models:
        model.generate()

