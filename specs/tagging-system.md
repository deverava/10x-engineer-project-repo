# Tagging System Specification

## Overview

The tagging system allows users to apply tags to prompts to improve organization, search, and filtering. Tags are lightweight labels such as "marketing", "summarization", or "customer-support".

This feature helps teams quickly find prompts by theme, use-case, or owner-defined categories.

---

## User Stories and Acceptance Criteria

### User Story 1: Add tags to a prompt
**As a user,** I want to add tags to a prompt so I can categorize it.

**Acceptance Criteria**
- Prompt create/update supports tags (list of strings).
- Tags are stored and returned in the prompt response.
- Duplicate tags are automatically removed (case-insensitive recommendation).
- Tag length is validated (example: 1–30 characters).
- Tags are normalized (example: trim whitespace).

---

### User Story 2: Remove tags from a prompt
**As a user,** I want to remove tags from a prompt so I can keep tagging accurate.

**Acceptance Criteria**
- Updating a prompt can remove tags by replacing the tags list.
- The returned prompt reflects the updated tag list.

---

### User Story 3: List prompts by tag
**As a user,** I want to filter prompts by tag so I can quickly find relevant prompts.

**Acceptance Criteria**
- GET /prompts supports filtering by tag query parameter.
- Filtering returns only prompts that contain the requested tag.
- If tag does not exist on any prompt, return empty list with total=0 (200).

---

### User Story 4: List all available tags
**As a user,** I want to see all tags used in the system so I can reuse consistent tags.

**Acceptance Criteria**
- New endpoint exists to list distinct tags.
- Response includes sorted tag list.
- Total count returned.

---

## Data Model Changes Needed

Update Prompt models to include tags.

### PromptBase changes
Add:

- tags: List[str] = Field(default_factory=list)

Rules:
- tags must be a list of strings
- each tag trimmed and lowercased (recommended)
- max tags per prompt (example: 20)
- max tag length (example: 30)

Storage changes:
- In-memory Prompt objects already store data; no new top-level model required.
- Optionally store a tag index for faster search:
  - `_tag_index: Dict[str, List[str]]` where key is tag, value is list of prompt_ids

---

## API Endpoint Specifications

### Add/Update tags (via existing prompt endpoints)
- POST /prompts (include tags)
- PUT /prompts/{prompt_id} (include tags)

Example request body:
- tags: ["summarization", "marketing"]

Errors:
- 422 for invalid tag schema (non-string, too long, etc.)

---

### Filter prompts by tag
**GET /prompts?tag={tag_name}**

**Response (200)**
- PromptList response (prompts + total)

Behavior:
- Case-insensitive match recommended
- Tag must match exactly after normalization

---

### List all tags
**GET /tags**

**Response (200)**
- tags: List[str]
- total: int

---

## Search and Filter Requirements

Update GET /prompts to support combined filters:

- collection_id (optional)
- search (optional)
- tag (optional)

Rules:
- Filters can be combined (AND behavior):
  - Example: collection_id=1 AND tag=marketing AND search=summarize
- Sorting remains newest-first (by updated_at)

---

## Edge Cases to Handle (Recommended)

- Tags with spaces:
  - Decide whether to allow "customer support" or enforce "customer-support"
- Case sensitivity:
  - Normalize tags to lowercase
- Duplicate tags in request:
  - Remove duplicates
- Empty tag list:
  - Allowed (means no tags)
- Large number of prompts:
  - Tag index can improve performance (optional)
