from enum import Enum


class TicketStatus(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    COMPLETED = "Completed"
