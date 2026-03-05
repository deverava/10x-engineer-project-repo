"""FastAPI routes for PromptLab.

This module defines the HTTP API for PromptLab using FastAPI. It includes:
- Health check endpoint
- CRUD endpoints for prompts
- CRUD endpoints for collections

The API uses an in-memory storage layer (app.storage.storage) and helper
functions (app.utils) for sorting, filtering, and searching prompts.
"""

from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.models import (
    Collection,
    CollectionCreate,
    CollectionList,
    HealthResponse,
    Prompt,
    PromptCreate,
    PromptList,
    PromptUpdate,
    get_current_time,
)
from app.storage import storage
from app.utils import filter_prompts_by_collection, search_prompts, sort_prompts_by_date

app = FastAPI(
    title="PromptLab API",
    description="AI Prompt Engineering Platform",
    version=__version__,
)

# CORS middleware
# Note: allow_origins=["*"] is suitable for local development.
# For production, restrict origins to trusted domains.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============== Health Check ==============

@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Health check endpoint.

    Returns:
        HealthResponse: Object containing API health status and version.
    """
    return HealthResponse(status="healthy", version=__version__)


# ============== Prompt Endpoints ==============

@app.get("/prompts", response_model=PromptList)
def list_prompts(
    collection_id: Optional[str] = None,
    search: Optional[str] = None,
) -> PromptList:
    """List prompts with optional filtering and search.

    This endpoint supports:
    - Filtering prompts by a collection ID
    - Searching prompts by title/description
    - Sorting prompts by updated date (newest first)

    Args:
        collection_id: Optional collection ID to filter prompts.
        search: Optional query string to search within prompt title/description.

    Returns:
        PromptList: A list of prompts and the total count.
    """
    prompts = storage.get_all_prompts()

    # Filter by collection if specified
    if collection_id:
        prompts = filter_prompts_by_collection(prompts, collection_id)

    # Search if query provided
    if search:
        prompts = search_prompts(prompts, search)

    # Sort by date (newest first)
    prompts = sort_prompts_by_date(prompts, descending=True)

    return PromptList(prompts=prompts, total=len(prompts))


@app.get("/prompts/{prompt_id}", response_model=Prompt)
def get_prompt(prompt_id: str) -> Prompt:
    """Retrieve a single prompt by ID.

    Args:
        prompt_id: Unique identifier of the prompt.

    Returns:
        Prompt: The prompt object.

    Raises:
        HTTPException: 404 if the prompt does not exist.
    """
    prompt = storage.get_prompt(prompt_id)
    if prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt


@app.post("/prompts", response_model=Prompt, status_code=201)
def create_prompt(prompt_data: PromptCreate) -> Prompt:
    """Create a new prompt.

    Validates that the provided collection exists (if collection_id is set).

    Args:
        prompt_data: Request payload for creating a prompt.

    Returns:
        Prompt: The newly created prompt.

    Raises:
        HTTPException: 400 if collection_id is provided but collection does not exist.
    """
    if prompt_data.collection_id:
        collection = storage.get_collection(prompt_data.collection_id)
        if not collection:
            raise HTTPException(status_code=400, detail="Collection not found")

    prompt = Prompt(**prompt_data.model_dump())
    return storage.create_prompt(prompt)


@app.put("/prompts/{prompt_id}", response_model=Prompt)
def update_prompt(prompt_id: str, prompt_data: PromptUpdate) -> Prompt:
    """Update an existing prompt (full update).

    This endpoint expects all prompt fields (same shape as PromptUpdate).
    It also validates that the provided collection exists (if collection_id is set).

    Args:
        prompt_id: ID of the prompt to update.
        prompt_data: Request payload containing updated prompt fields.

    Returns:
        Prompt: The updated prompt.

    Raises:
        HTTPException: 404 if the prompt does not exist.
        HTTPException: 400 if collection_id is provided but collection does not exist.
    """
    existing = storage.get_prompt(prompt_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Prompt not found")

    if prompt_data.collection_id:
        collection = storage.get_collection(prompt_data.collection_id)
        if not collection:
            raise HTTPException(status_code=400, detail="Collection not found")

    updated_prompt = Prompt(
        id=existing.id,
        title=prompt_data.title,
        content=prompt_data.content,
        description=prompt_data.description,
        collection_id=prompt_data.collection_id,
        created_at=existing.created_at,
        updated_at=get_current_time(),
    )

    updated = storage.update_prompt(prompt_id, updated_prompt)
    # storage.update_prompt should return Prompt when prompt exists,
    # but keep a safe guard in case implementation changes.
    if updated is None:
        raise HTTPException(status_code=404, detail="Prompt not found")

    return updated


@app.delete("/prompts/{prompt_id}", status_code=204)
def delete_prompt(prompt_id: str) -> None:
    """Delete a prompt by ID.

    Args:
        prompt_id: ID of the prompt to delete.

    Returns:
        None

    Raises:
        HTTPException: 404 if the prompt does not exist.
    """
    if not storage.delete_prompt(prompt_id):
        raise HTTPException(status_code=404, detail="Prompt not found")
    return None


# ============== Collection Endpoints ==============

@app.get("/collections", response_model=CollectionList)
def list_collections() -> CollectionList:
    """List all collections.

    Returns:
        CollectionList: A list of collections and the total count.
    """
    collections = storage.get_all_collections()
    return CollectionList(collections=collections, total=len(collections))


@app.get("/collections/{collection_id}", response_model=Collection)
def get_collection(collection_id: str) -> Collection:
    """Retrieve a single collection by ID.

    Args:
        collection_id: Unique identifier of the collection.

    Returns:
        Collection: The collection object.

    Raises:
        HTTPException: 404 if the collection does not exist.
    """
    collection = storage.get_collection(collection_id)
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    return collection


@app.post("/collections", response_model=Collection, status_code=201)
def create_collection(collection_data: CollectionCreate) -> Collection:
    """Create a new collection.

    Args:
        collection_data: Request payload for creating a collection.

    Returns:
        Collection: The newly created collection.
    """
    collection = Collection(**collection_data.model_dump())
    return storage.create_collection(collection)


@app.delete("/collections/{collection_id}", status_code=204)
def delete_collection(collection_id: str) -> None:
    """Delete a collection by ID.

    If the collection exists, it will be deleted and any prompts that were
    assigned to it will be unassigned (collection_id set to None).

    Args:
        collection_id: ID of the collection to delete.

    Returns:
        None

    Raises:
        HTTPException: 404 if the collection does not exist.
    """
    if not storage.delete_collection(collection_id):
        raise HTTPException(status_code=404, detail="Collection not found")

    # Remove reference (safe even if storage.delete_collection already unassigned)
    storage.unassign_prompts_from_collection(collection_id)

    return None
