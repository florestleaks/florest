from datetime import datetime
from typing import Optional

from florest.user.entities.ticket.ticket_attachment import TicketAttachment
from florest.user.entities.ticket.ticket_comment import TicketComment
from florest.user.entities.ticket.ticket_priority import TicketPriority
from florest.user.entities.ticket.ticket_severity import TicketSeverity
from florest.user.entities.ticket.ticket_status import TicketStatus


class Ticket:
    def __init__(
        self,
        ticket_id: str,
        title: str,
        description: str,
        severity: TicketSeverity,
        status: TicketStatus,
        category: str,
        assigned_to: str,
        created_by: str,
        priority: TicketPriority,
        action_plan: str,
        related_incidents: list[int] = [],
        comments: list[TicketComment] = [],
        attachments: list[TicketAttachment] = [],
        due_date: Optional[datetime] = None,
    ):
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.severity = severity
        self.status = status
        self.category = category
        self.timestamp: datetime = datetime.now()
        self.assigned_to = assigned_to
        self.created_by = created_by
        self.priority = priority
        self.action_plan = action_plan
        self.related_incidents = related_incidents
        self.comments = comments
        self.attachments = attachments
        self.due_date = due_date
