"""Pydantic models for PromptLab.

This module defines all request/response schemas used by the PromptLab API,
including prompt models, collection models, and common API response models.
"""

from datetime import datetime
from typing import Optional, List
from uuid import uuid4

from pydantic import BaseModel, Field


def generate_id() -> str:
    """Generate a unique identifier.

    Returns:
        A UUID4 string that can be used as a unique resource identifier.

    Example:
        >>> value = generate_id()
        >>> isinstance(value, str)
        True
    """
    return str(uuid4())


def get_current_time() -> datetime:
    """Get the current UTC time.

    Returns:
        A timezone-naive datetime representing current UTC time.

    Example:
        >>> ts = get_current_time()
        >>> isinstance(ts, datetime)
        True
    """
    return datetime.utcnow()


# ============== Prompt Models ==============

class PromptBase(BaseModel):
    """Base model for prompt payloads.

    This model contains the common fields shared between prompt creation,
    update, and response models.

    Attributes:
        title: Short title for the prompt.
        content: The prompt template content. May include variables like {{input}}.
        description: Optional longer description for context or usage notes.
        collection_id: Optional ID of the collection the prompt belongs to.
    """

    title: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Short title for the prompt (1-200 characters).",
    )
    content: str = Field(
        ...,
        min_length=1,
        description="Prompt template content (must not be empty).",
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional description of the prompt (max 500 characters).",
    )
    collection_id: Optional[str] = Field(
        None,
        description="Optional ID of the collection that this prompt belongs to.",
    )


class PromptCreate(PromptBase):
    """Request model for creating a prompt.

    Inherits:
        PromptBase: Includes title, content, description, and collection_id.
    """
    pass


class PromptUpdate(PromptBase):
    """Request model for updating a prompt (full update).

    This model represents a full replacement update (PUT) where all fields are
    expected (same as PromptBase).

    Inherits:
        PromptBase: Includes title, content, description, and collection_id.
    """
    pass


class Prompt(PromptBase):
    """Response model representing a stored prompt.

    Includes server-generated fields such as id and timestamps.

    Attributes:
        id: Unique identifier for the prompt.
        created_at: Timestamp when the prompt was created (UTC).
        updated_at: Timestamp when the prompt was last updated (UTC).
    """

    id: str = Field(
        default_factory=generate_id,
        description="Unique identifier for the prompt.",
    )
    created_at: datetime = Field(
        default_factory=get_current_time,
        description="UTC timestamp when the prompt was created.",
    )
    updated_at: datetime = Field(
        default_factory=get_current_time,
        description="UTC timestamp when the prompt was last updated.",
    )

    class Config:
        """Pydantic configuration for model behavior."""
        from_attributes = True


# ============== Collection Models ==============

class CollectionBase(BaseModel):
    """Base model for collection payloads.

    A collection groups prompts together for organization.

    Attributes:
        name: Name of the collection.
        description: Optional description of the collection.
    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Name of the collection (1-100 characters).",
    )
    description: Optional[str] = Field(
        None,
        max_length=500,
        description="Optional description of the collection (max 500 characters).",
    )


class CollectionCreate(CollectionBase):
    """Request model for creating a collection.

    Inherits:
        CollectionBase: Includes name and description.
    """
    pass


class Collection(CollectionBase):
    """Response model representing a stored collection.

    Attributes:
        id: Unique identifier for the collection.
        created_at: Timestamp when the collection was created (UTC).
    """

    id: str = Field(
        default_factory=generate_id,
        description="Unique identifier for the collection.",
    )
    created_at: datetime = Field(
        default_factory=get_current_time,
        description="UTC timestamp when the collection was created.",
    )

    class Config:
        """Pydantic configuration for model behavior."""
        from_attributes = True


# ============== Response Models ==============

class PromptList(BaseModel):
    """Response model for listing prompts.

    Attributes:
        prompts: List of prompts returned by the API.
        total: Total number of prompts returned.
    """

    prompts: List[Prompt] = Field(..., description="List of prompts.")
    total: int = Field(..., description="Total count of prompts returned.")


class CollectionList(BaseModel):
    """Response model for listing collections.

    Attributes:
        collections: List of collections returned by the API.
        total: Total number of collections returned.
    """

    collections: List[Collection] = Field(..., description="List of collections.")
    total: int = Field(..., description="Total count of collections returned.")


class HealthResponse(BaseModel):
    """Response model for health check endpoint.

    Attributes:
        status: Health status string (e.g., 'ok' or 'healthy').
        version: Application version string.
    """

    status: str = Field(..., description="Health status of the API.")
    version: str = Field(..., description="Current application version.")
