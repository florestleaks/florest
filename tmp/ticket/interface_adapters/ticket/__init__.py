from abc import ABC, abstractmethod
from typing import List, Optional

from florest.user.entities.ticket import Ticket


class TicketRepository(ABC):
    """
    Abstract base class for ticket repositories.

    This class provides the method signatures that any ticket repository
    implementation should adhere to.
    """

    @abstractmethod
    def create(self, ticket: Ticket) -> Ticket:
        """
        Create a new ticket.

        Parameters
        ----------
        ticket : Ticket
            The ticket to be added.

        Returns
        -------
        Ticket
            The created ticket.
        """

    @abstractmethod
    def read(self, ticket_id: str) -> Optional[Ticket]:
        """
        Retrieve a ticket by its ID.

        Parameters
        ----------
        ticket_id : str
            The ID of the ticket to retrieve.

        Returns
        -------
        Optional[Ticket]
            The ticket if found, None otherwise.
        """

    @abstractmethod
    def update(self, ticket: Ticket) -> Ticket:
        """
        Update an existing ticket.

        Parameters
        ----------
        ticket : Ticket
            The ticket with updated details.

        Returns
        -------
        Ticket
            The updated ticket.
        """

    @abstractmethod
    def delete(self, ticket_id: str) -> None:
        """
        Delete a ticket by its ID.

        Parameters
        ----------
        ticket_id : str
            The ID of the ticket to delete.

        Returns
        -------
        None
        """

    @abstractmethod
    def list_all(self) -> list[Ticket]:
        """
        List all tickets.

        Returns
        -------
        List[Ticket]
            A list of all tickets.
        """

    # ==============================
    # Batch (Bulk) Operations
    # ==============================

    @abstractmethod
    def create_bulk(self, tickets: list[Ticket]) -> list[Ticket]:
        """
        Create multiple tickets at once.

        Parameters
        ----------
        tickets : List[Ticket]
            A list of tickets to be added.

        Returns
        -------
        List[Ticket]
            A list of created tickets.
        """

    @abstractmethod
    def update_bulk(self, tickets: list[Ticket]) -> list[Ticket]:
        """
        Update multiple tickets at once.

        Parameters
        ----------
        tickets : List[Ticket]
            A list of tickets with updated details.

        Returns
        -------
        List[Ticket]
            A list of updated tickets.
        """

    @abstractmethod
    def delete_bulk(self, ticket_ids: list[str]) -> None:
        """
        Delete multiple tickets by their IDs.

        Parameters
        ----------
        ticket_ids : List[str]
            A list of IDs of the tickets to delete.

        Returns
        -------
        None
        """
