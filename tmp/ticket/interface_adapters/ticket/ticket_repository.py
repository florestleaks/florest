from abc import ABC, abstractmethod

from florest.user.entities.ticket import Ticket


class TicketRepository(ABC):
    """
    Abstract base class for ticket repository.
    Defines the contract for ticket data operations.
    """

    # ==============================
    # Individual (Unitary) Operations
    # ==============================

    @abstractmethod
    def create(self, ticket: Ticket) -> bool | None:
        """
        Add a ticket to the storage.

        Parameters
        ----------
        ticket : Ticket
            The ticket object to be added.

        Returns
        -------
        bool | None
            True if successful, False if failed, None if ticket already exists.
        """

    @abstractmethod
    def update(self, ticket: Ticket) -> bool:
        """
        Update a ticket's details.

        Parameters
        ----------
        ticket : Ticket
            The updated ticket object.

        Returns
        -------
        bool
            True if successful, False otherwise.
        """

    @abstractmethod
    def delete(self, ticket_id: int) -> bool:
        """
        Delete a ticket by their unique ID.

        Parameters
        ----------
        ticket_id : int
            The unique ID of the ticket.

        Returns
        -------
        bool
            True if successful, False otherwise.
        """

    @abstractmethod
    def find_by_id(self, ticket_id: int) -> Ticket | None:
        """
        Find a ticket by their unique ID.

        Parameters
        ----------
        ticket_id : int
            The unique ID of the ticket.

        Returns
        -------
        Ticket | None
            Ticket object if found, None otherwise.
        """

    # ==============================
    # Batch (Bulk) Operations
    # ==============================

    @abstractmethod
    def add_bulk(self, tickets: list[Ticket]) -> bool:
        """
        Add multiple tickets to the storage.

        Parameters
        ----------
        tickets : list[Ticket]
            List of ticket objects to be added.

        Returns
        -------
        bool
            True if all tickets are added successfully, False otherwise.
        """

    @abstractmethod
    def find_by_ids(self, ticket_ids: list[int]) -> list[Ticket | None]:
        """
        Find multiple tickets by their unique IDs.

        Parameters
        ----------
        ticket_ids : list[int]
            List of unique IDs of the tickets.

        Returns
        -------
        list[Ticket | None]
            List of Ticket objects corresponding to the given IDs.
            If a ticket is not found, its position in the list will be None.
        """

    @abstractmethod
    def update_bulk(self, tickets: list[Ticket]) -> bool:
        """
        Update multiple tickets' details.

        Parameters
        ----------
        tickets : list[Ticket]
            List of updated ticket objects.

        Returns
        -------
        bool
            True if all tickets are updated successfully, False otherwise.
        """

    @abstractmethod
    def delete_bulk(self, ticket_ids: list[int]) -> bool:
        """
        Delete multiple tickets by their unique IDs.

        Parameters
        ----------
        ticket_ids : list[int]
            List of unique IDs of the tickets to be deleted.

        Returns
        -------
        bool
            True if all tickets are deleted successfully, False otherwise.
        """

    @abstractmethod
    def list_all(self) -> list[Ticket]:
        """
        List all tickets in the storage.

        Returns
        -------
        list[Ticket]
            List containing all tickets.
        """
