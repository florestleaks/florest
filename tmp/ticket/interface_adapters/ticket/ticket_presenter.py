from abc import ABC

from florest.user.entities.ticket import Ticket


class TicketPresenter(ABC):
    @staticmethod
    def to_dict(ticket: Ticket) -> dict:
        """
        Convert a Ticket object to a dictionary representation.

        Parameters
        ----------
        ticket : Ticket
            The ticket to be converted.

        Returns
        -------
        dict
            Dictionary representation of the ticket.
        """
        return {
            "ticket_id": ticket.ticket_id,
            "title": ticket.title,
            "description": ticket.description,
            "severity": ticket.severity.value
            if hasattr(ticket.severity, "value")
            else str(ticket.severity),
            "status": ticket.status.value
            if hasattr(ticket.status, "value")
            else str(ticket.status),
            "category": ticket.category,
            "timestamp": ticket.timestamp.isoformat(),
            "assigned_to": ticket.assigned_to,
            "created_by": ticket.created_by,
            "priority": ticket.priority.value
            if hasattr(ticket.priority, "value")
            else str(ticket.priority),
            "action_plan": ticket.action_plan,
            "related_incidents": ticket.related_incidents,
            "comments": [
                comment.to_dict() if hasattr(comment, "to_dict") else str(comment)
                for comment in ticket.comments
            ],
            "attachments": [
                attachment.to_dict() if hasattr(attachment, "to_dict") else str(attachment)
                for attachment in ticket.attachments
            ],
            "due_date": ticket.due_date.isoformat() if ticket.due_date else None,
        }

    @staticmethod
    def from_dict(data: dict) -> Ticket:
        """
        Convert a dictionary representation back to a Ticket object.

        Parameters
        ----------
        data : dict
            The dictionary representation of a ticket.

        Returns
        -------
        Ticket
            The Ticket object constructed from the dictionary data.
        """
        # Note: You may need to further expand this method to handle nested objects like comments and attachments.
        return Ticket(
            ticket_id=data["ticket_id"],
            title=data["title"],
            description=data["description"],
            severity=data[
                "severity"
            ],  # You may need to convert back to the respective enum or type
            status=data["status"],  # Similarly for other fields
            category=data["category"],
            assigned_to=data["assigned_to"],
            created_by=data["created_by"],
            priority=data["priority"],
            action_plan=data["action_plan"],
            related_incidents=data.get("related_incidents", []),
            comments=data.get("comments", []),
            attachments=data.get("attachments", []),
            due_date=data["due_date"] if "due_date" in data and data["due_date"] else None,
        )
