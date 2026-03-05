"""In-memory storage for PromptLab.

This module provides simple in-memory storage for prompts and collections.
In a production environment, this would be replaced with a database.
"""

from typing import Dict, List, Optional
from app.models import Prompt, Collection


class Storage:
    """In-memory storage engine for prompts and collections.

    This class manages CRUD operations for Prompt and Collection objects.
    Data is stored in dictionaries during application runtime.

    Note:
        This storage is ephemeral. All data will be lost when the
        application restarts.
    """

    def __init__(self):
        """Initialize empty in-memory storage dictionaries."""
        self._prompts: Dict[str, Prompt] = {}
        self._collections: Dict[str, Collection] = {}

    # ============== Prompt Operations ==============

    def create_prompt(self, prompt: Prompt) -> Prompt:
        """Store a new prompt.

        Args:
            prompt: The Prompt object to store.

        Returns:
            The stored Prompt object.
        """
        self._prompts[prompt.id] = prompt
        return prompt

    def get_prompt(self, prompt_id: str) -> Optional[Prompt]:
        """Retrieve a prompt by ID.

        Args:
            prompt_id: Unique identifier of the prompt.

        Returns:
            The Prompt object if found, otherwise None.
        """
        return self._prompts.get(prompt_id)

    def get_all_prompts(self) -> List[Prompt]:
        """Retrieve all stored prompts.

        Returns:
            A list of all Prompt objects.
        """
        return list(self._prompts.values())

    def update_prompt(self, prompt_id: str, prompt: Prompt) -> Optional[Prompt]:
        """Update an existing prompt.

        Args:
            prompt_id: ID of the prompt to update.
            prompt: Updated Prompt object.

        Returns:
            The updated Prompt if it exists, otherwise None.
        """
        if prompt_id not in self._prompts:
            return None
        self._prompts[prompt_id] = prompt
        return prompt

    def delete_prompt(self, prompt_id: str) -> bool:
        """Delete a prompt by ID.

        Args:
            prompt_id: ID of the prompt to delete.

        Returns:
            True if the prompt was deleted, False otherwise.
        """
        if prompt_id in self._prompts:
            del self._prompts[prompt_id]
            return True
        return False

    # ============== Collection Operations ==============

    def create_collection(self, collection: Collection) -> Collection:
        """Store a new collection.

        Args:
            collection: The Collection object to store.

        Returns:
            The stored Collection object.
        """
        self._collections[collection.id] = collection
        return collection

    def get_collection(self, collection_id: str) -> Optional[Collection]:
        """Retrieve a collection by ID.

        Args:
            collection_id: Unique identifier of the collection.

        Returns:
            The Collection object if found, otherwise None.
        """
        return self._collections.get(collection_id)

    def get_all_collections(self) -> List[Collection]:
        """Retrieve all stored collections.

        Returns:
            A list of all Collection objects.
        """
        return list(self._collections.values())

    def unassign_prompts_from_collection(self, collection_id: str) -> None:
        """Remove collection reference from associated prompts.

        Args:
            collection_id: ID of the collection being removed.

        This method sets the collection_id field of all prompts
        associated with the given collection to None.
        """
        for prompt in self._prompts.values():
            if prompt.collection_id == collection_id:
                prompt.collection_id = None

    def delete_collection(self, collection_id: str) -> bool:
        """Delete a collection and unassign related prompts.

        Args:
            collection_id: ID of the collection to delete.

        Returns:
            True if the collection was deleted, False otherwise.

        Side Effects:
            Prompts associated with the collection will have their
            collection_id set to None.
        """
        if collection_id in self._collections:
            for prompt in self._prompts.values():
                if prompt.collection_id == collection_id:
                    prompt.collection_id = None
            del self._collections[collection_id]
            return True
        return False

    def get_prompts_by_collection(self, collection_id: str) -> List[Prompt]:
        """Retrieve prompts belonging to a specific collection.

        Args:
            collection_id: ID of the collection.

        Returns:
            A list of Prompt objects associated with the collection.
        """
        return [
            prompt
            for prompt in self._prompts.values()
            if prompt.collection_id == collection_id
        ]

    # ============== Utility ==============

    def clear(self) -> None:
        """Clear all stored prompts and collections.

        This is typically used in testing scenarios to reset state.
        """
        self._prompts.clear()
        self._collections.clear()


# Global storage instance
storage = Storage()
