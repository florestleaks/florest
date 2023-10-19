from enum import Enum


class TicketPriority(Enum):
    HIGH = "High Priority"
    LOW = "Low Priority"
    MEDIUM = "Medium Priority"
    CRITICAL = "Critical Priority"
    URGENT = "Urgent Priority"
