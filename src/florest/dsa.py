from datetime import datetime
from enum import Enum
from typing import Optional


# Using Python's `enum` module for more elegant and pythonic enumerations
class Severity(Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Status(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    COMPLETED = "Completed"


class Priority(Enum):
    HIGH = "High Priority"
    LOW = "Low Priority"
    MEDIUM = "Medium Priority"
    CRITICAL = "Critical Priority"
    URGENT = "Urgent Priority"


# Using nested classes for a cleaner organization of Categories
class Category:
    class Phishing:
        SpearphishingAttachment = "Spearphishing Attachment"
        SpearphishingLink = "Spearphishing Link"
        SpearphishingViaService = "Spearphishing via Service"

    class GatherVictimIdentityInformation:
        Credentials = "Credentials"
        EmailAddresses = "Email Addresses"
        EmployeeNames = "Employee Names"

    class GatherVictimOrgInformation:
        DeterminePhysicalLocations = "Determine Physical Locations"
        BusinessRelationships = "Business Relationships"
        IdentifyBusinessTempo = "Identify Business Tempo"
        IdentifyRoles = "Identify Roles"

    class EstablishAccounts:
        SocialMediaAccounts = "Social Media Accounts"
        EmailAccounts = "Email Accounts"
        CloudAccounts = "Cloud Accounts"

    class ValidAccounts:
        DefaultAccounts = "Default Accounts"
        DomainAccounts = "Domain Accounts"
        LocalAccounts = "Local Accounts"
        CloudAccounts = "Cloud Accounts"  # This category is repeated, you might want to verify if this redundancy is intentional


class Comment:
    def __init__(self, author: str, text: str):
        self.author = author
        self.timestamp: datetime = datetime.now()
        self.text = text


class Attachment:
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


class Ticket:
    def __init__(
        self,
        ticket_id: str,
        title: str,
        description: str,
        severity: Severity,
        status: Status,
        category: str,
        assigned_to: str,
        created_by: str,
        priority: Priority,
        action_plan: str,
        related_incidents: list[int] = [],
        comments: list[Comment] = [],
        attachments: list[Attachment] = [],
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

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def add_attachment(self, attachment: Attachment):
        self.attachments.append(attachment)


# Note: You can extend the `Ticket` class to include more methods based on your needs.
if __name__ == "__main__":
    # Create some comments and attachments for a ticket
    comment1 = Comment(author="John Smith", text="Initial analysis done.")
    comment2 = Comment(author="Jane Doe", text="Sent for review.")

    attachment1 = Attachment(
        file_name="analysis.pdf",
        file_type="pdf",
        file_size="1MB",
    )

    # Create a ticket
    ticket = Ticket(
        ticket_id="12345",
        title="Potential Spearphishing Attack",
        description="Received an email with suspicious links.",
        severity=Severity.HIGH,
        status=Status.OPEN,
        category=Category.Phishing.SpearphishingLink,
        assigned_to="Jane Doe",
        created_by="John Smith",
        priority=Priority.CRITICAL,
        action_plan="1. Verify sender. 2. Analyze links. 3. Inform IT department.",
        related_incidents=[101, 102],
        comments=[comment1],
        attachments=[attachment1],
    )

    # Adding an additional comment to the ticket
    ticket.add_comment(comment2)

    # Print ticket details
    print(f"Ticket ID: {ticket.ticket_id}")
    print(f"Title: {ticket.title}")
    print(f"Severity: {ticket.severity.value}")
    print(f"Status: {ticket.status.value}")
    print(f"Category: {ticket.category}")
    print(f"Assigned to: {ticket.assigned_to}")
    print(f"Priority: {ticket.priority.value}")

    # Print comments for the ticket
    print("\nComments:")
    for comment in ticket.comments:
        print(f"{comment.timestamp} - {comment.author}: {comment.text}")

    # Print attachments for the ticket
    print("\nAttachments:")
    for attachment in ticket.attachments:
        print(
            f"Name: {attachment.file_name}, Type: {attachment.file_type}, Size: {attachment.file_size}"
        )

    # ... you can continue using other methods and attributes as needed.
