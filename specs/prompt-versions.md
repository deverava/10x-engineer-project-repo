# Prompt Versions Specification

## Overview

Prompt version tracking allows users to maintain a history of changes made to a prompt over time. Each time a prompt is updated, a new version should be created, enabling users to view previous versions, compare changes, and restore older versions if needed.

This feature improves reliability, auditability, and collaboration when prompts evolve.

---

## User Stories and Acceptance Criteria

### User Story 1: Automatically create versions on update
**As a user,** I want a new version to be created whenever a prompt is updated, so I can track changes over time.

**Acceptance Criteria**
- When a prompt is updated using PUT (and later PATCH if implemented), a new version entry is created.
- The current prompt record reflects the latest content and metadata.
- The version history includes the previous content before the update.
- Each version includes:
  - version number (incrementing)
  - prompt_id
  - title/content/description/collection_id snapshot
  - created_at timestamp of the version
  - optional change summary (future enhancement)

---

### User Story 2: View version history
**As a user,** I want to view all versions of a prompt so I can understand how it changed.

**Acceptance Criteria**
- A new endpoint exists to list versions for a prompt.
- Versions are returned newest → oldest.
- Version entries include version number and timestamps.
- If prompt_id does not exist, return 404.

---

### User Story 3: Retrieve a specific version
**As a user,** I want to view a specific version of a prompt so I can inspect older content.

**Acceptance Criteria**
- A new endpoint exists to retrieve a version by version number (or version_id).
- If the version does not exist, return 404.
- Response includes full snapshot of that version.

---

### User Story 4: Restore a version as current
**As a user,** I want to restore an old version as the current prompt, so I can roll back mistakes.

**Acceptance Criteria**
- A restore endpoint exists.
- Restoring creates a new version entry (representing the state before restore) OR records the restore action explicitly.
- After restore, the prompt’s current fields match the restored version.
- updated_at is updated.
- If prompt/version not found, return 404.

---

## Data Model Changes Needed

### Option A: Separate Version Model (Recommended)

Add a new Pydantic model and storage structure:

**PromptVersion**
- id: str
- prompt_id: str
- version: int
- title: str
- content: str
- description: Optional[str]
- collection_id: Optional[str]
- created_at: datetime

Storage changes:
- Add `_prompt_versions: Dict[str, List[PromptVersion]]` keyed by prompt_id
- On every prompt update:
  - create version snapshot before applying update
  - append snapshot to version list

### Notes
- Version numbers start at 1.
- The “current prompt” is stored in existing `Prompt`.
- Versions store historical snapshots only.

---

## API Endpoint Specifications

### List all versions for a prompt
**GET /prompts/{prompt_id}/versions**

**Response (200)**
- Returns a list of versions with metadata.

Example response:
- versions: [ { version, created_at }, ... ]
- total: int

Errors:
- 404 if prompt not found

---

### Get a specific version
**GET /prompts/{prompt_id}/versions/{version}**

**Response (200)**
- Returns full snapshot for the requested version.

Errors:
- 404 if prompt not found
- 404 if version not found

---

### Restore a version
**POST /prompts/{prompt_id}/versions/{version}/restore**

**Response (200)**
- Returns the updated current prompt.

Errors:
- 404 if prompt not found
- 404 if version not found

---

## Edge Cases to Handle

- Updating a prompt that does not exist → 404 (already implemented)
- Prompt updated without any meaningful changes (same values):
  - Still creates a version OR skip version creation (choose one behavior and document)
- Deleting prompts:
  - Decide whether versions are deleted too (recommended: delete versions along with prompt)
- Version list is empty:
  - If prompt has never been updated, versions endpoint returns empty list (200)
- Concurrent updates:
  - Ensure version numbers remain consistent (for in-memory storage, serialize updates)
- Collection deleted:
  - Old versions may reference deleted collection_id (acceptable; versions represent history)
