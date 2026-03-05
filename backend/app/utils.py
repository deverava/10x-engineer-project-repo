"""Utility functions for PromptLab.

This module contains helper functions used for sorting,
filtering, searching, and validating prompts.
"""

from typing import List
import re

from app.models import Prompt


def sort_prompts_by_date(prompts: List[Prompt], descending: bool = True) -> List[Prompt]:
    """Sort prompts by their last updated timestamp.

    Args:
        prompts: List of Prompt objects to sort.
        descending: If True, sorts newest first.
                    If False, sorts oldest first.

    Returns:
        A sorted list of Prompt objects based on `updated_at`.

    Example:
        >>> sorted_prompts = sort_prompts_by_date(prompts, descending=True)
    """
    return sorted(prompts, key=lambda x: x.updated_at, reverse=descending)


def filter_prompts_by_collection(
    prompts: List[Prompt], collection_id: str
) -> List[Prompt]:
    """Filter prompts by collection ID.

    Args:
        prompts: List of Prompt objects.
        collection_id: ID of the collection to filter by.

    Returns:
        A list of Prompt objects that belong to the given collection.

    Example:
        >>> collection_prompts = filter_prompts_by_collection(prompts, "123")
    """
    return [p for p in prompts if p.collection_id == collection_id]


def search_prompts(prompts: List[Prompt], query: str) -> List[Prompt]:
    """Search prompts by title or description.

    The search is case-insensitive and checks whether the query
    exists within the prompt title or description.

    Args:
        prompts: List of Prompt objects.
        query: Search string.

    Returns:
        A list of Prompt objects that match the query.

    Example:
        >>> results = search_prompts(prompts, "summarize")
    """
    query_lower = query.lower()
    return [
        p
        for p in prompts
        if query_lower in p.title.lower()
        or (p.description and query_lower in p.description.lower())
    ]


def validate_prompt_content(content: str) -> bool:
    """Validate prompt content.

    A valid prompt must:
    - Not be empty
    - Not contain only whitespace
    - Be at least 10 characters long (after trimming)

    Args:
        content: The prompt content string to validate.

    Returns:
        True if the content is valid, False otherwise.

    Example:
        >>> validate_prompt_content("Summarize this text")
        True
        >>> validate_prompt_content("   ")
        False
    """
    if not content or not content.strip():
        return False
    return len(content.strip()) >= 10


def extract_variables(content: str) -> List[str]:
    """Extract template variables from prompt content.

    Variables must follow the format: {{variable_name}}

    Args:
        content: Prompt content string.

    Returns:
        A list of variable names found inside double curly braces.

    Example:
        >>> extract_variables("Hello {{name}}, your id is {{id}}")
        ['name', 'id']
    """
    pattern = r"\{\{(\w+)\}\}"
    return re.findall(pattern, content)
