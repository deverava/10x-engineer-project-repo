"""FastAPI routes for PromptLab.

This module defines the HTTP API for PromptLab using FastAPI. It includes:
- Health check endpoint
- CRUD endpoints for prompts
- CRUD endpoints for collections

The API uses an in-memory storage layer (app.storage.storage) and helper
functions (app.utils) for sorting, filtering, and searching prompts.
"""

from typing import Optional

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

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
    """Health check endpoint."""
    return HealthResponse(status="healthy", version=__version__)


# ============== Prompt Endpoints ==============


@app.get("/prompts", response_model=PromptList)
def list_prompts(
    collection_id: Optional[str] = None,
    search: Optional[str] = None,
    tag: Optional[str] = None,
) -> PromptList:
    """List prompts with optional filtering, search, and tag filtering."""
    prompts = storage.get_all_prompts()

    if collection_id:
        prompts = filter_prompts_by_collection(prompts, collection_id)

    if search:
        prompts = search_prompts(prompts, search)

    if tag:
        prompts = [
            prompt
            for prompt in prompts
            if tag.lower() in [existing_tag.lower() for existing_tag in (prompt.tags or [])]
        ]

    prompts = sort_prompts_by_date(prompts, descending=True)

    return PromptList(prompts=prompts, total=len(prompts))


@app.get("/prompts/{prompt_id}", response_model=Prompt)
def get_prompt(prompt_id: str) -> Prompt:
    """Retrieve a single prompt by ID."""
    prompt = storage.get_prompt(prompt_id)
    if prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt


@app.post("/prompts", response_model=Prompt, status_code=201)
async def create_prompt(request: Request) -> Prompt:
    """Create a new prompt with custom validation and 400 responses."""
    try:
        data = await request.json()
        prompt_data = PromptCreate(**data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid input",
        )

    if not prompt_data.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty.",
        )

    if prompt_data.collection_id:
        collection = storage.get_collection(prompt_data.collection_id)
        if not collection:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Collection not found",
            )

    prompt = Prompt(**prompt_data.model_dump())
    return storage.create_prompt(prompt)


@app.put("/prompts/{prompt_id}", response_model=Prompt)
def update_prompt(prompt_id: str, prompt_data: PromptUpdate) -> Prompt:
    """Update an existing prompt (full update)."""
    existing = storage.get_prompt(prompt_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Prompt not found")

    if prompt_data.collection_id:
        collection = storage.get_collection(prompt_data.collection_id)
        if not collection:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Collection not found",
            )

    updated_prompt = Prompt(
        id=existing.id,
        title=prompt_data.title,
        content=prompt_data.content,
        description=prompt_data.description,
        collection_id=prompt_data.collection_id,
        tags=prompt_data.tags,
        created_at=existing.created_at,
        updated_at=get_current_time(),
    )

    updated = storage.update_prompt(prompt_id, updated_prompt)
    if updated is None:
        raise HTTPException(status_code=404, detail="Prompt not found")

    return updated


@app.delete("/prompts/{prompt_id}", status_code=204)
def delete_prompt(prompt_id: str) -> None:
    """Delete a prompt by ID."""
    if not storage.delete_prompt(prompt_id):
        raise HTTPException(status_code=404, detail="Prompt not found")
    return None


# ============== Collection Endpoints ==============


@app.get("/collections", response_model=CollectionList)
def list_collections() -> CollectionList:
    """List all collections."""
    collections = storage.get_all_collections()
    return CollectionList(collections=collections, total=len(collections))


@app.get("/collections/{collection_id}", response_model=Collection)
def get_collection(collection_id: str) -> Collection:
    """Retrieve a single collection by ID."""
    collection = storage.get_collection(collection_id)
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    return collection


@app.post("/collections", response_model=Collection, status_code=201)
def create_collection(collection_data: CollectionCreate) -> Collection:
    """Create a new collection."""
    collection = Collection(**collection_data.model_dump())
    return storage.create_collection(collection)


@app.delete("/collections/{collection_id}", status_code=204)
def delete_collection(collection_id: str) -> None:
    """Delete a collection by ID."""
    if not storage.delete_collection(collection_id):
        raise HTTPException(status_code=404, detail="Collection not found")

    storage.unassign_prompts_from_collection(collection_id)
    return None