from datetime import datetime


class TicketAttachment:
    def __init__(
        self,
        file_name: str,
        file_type: str,
        file_size: str,
    ):
        self.file_name = file_name
        self.file_type = file_type
        self.file_size = file_size
        self.upload_timestamp: datetime = datetime.now()
