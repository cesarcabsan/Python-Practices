from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailSender(MessageSender):
    def send(self, message: str):
        print(f"Sending email: {message}")

class SmsSender(MessageSender):
    def send(self, message: str):
        print(f"Sending SMS: {message}")


class MessageService:
    def __init__(self, m_sender: MessageSender):
        self.m_sender = m_sender

    def send_message(self, message: str):
        self.m_sender.send(message)


email_sender = EmailSender()
notification_service = MessageService(email_sender)
notification_service.send_message("This is a message send from email!")

sms_sender = SmsSender()
notification_service = MessageService(sms_sender)
notification_service.send_message("This is a message send from SMS!")
