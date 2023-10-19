from datetime import datetime


class TicketComment:
    def __init__(self, author: str, text: str):
        self.author = author
        self.timestamp: datetime = datetime.now()
        self.text = text
