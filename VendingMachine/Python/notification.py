class Notification:
    def __init__(self, owner_contact: str):
        self.owner_contact = owner_contact

    def send_notification(self, message: str):
        print(f"NOTIFICATION SENT TO {self.owner_contact}: {message}")