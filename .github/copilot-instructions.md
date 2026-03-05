# PromptLab – AI Coding Agent Instructions (Copilot)

These instructions define coding standards and conventions for contributing to the PromptLab codebase. Follow them for all changes, new features, and refactors.

---

## 1) Project Coding Standards

### Language and Style
- Use Python 3.10+ features.
- Follow PEP 8 formatting.
- Use type hints for all public functions and methods.
- Keep functions small and focused (prefer < 30 lines where possible).
- Prefer clear, readable code over clever code.

### Docstrings
- Use Google-style docstrings for every function, method, and class.
- Include:
  - Short summary line
  - Args / Returns
  - Raises (if applicable)
  - Example (when helpful)

### Imports
- Use standard import grouping:
  1) Standard library
  2) Third-party libraries
  3) Local application imports (`app.*`)
- Prefer explicit imports (avoid `import *`).

---

## 2) Preferred Patterns and Conventions

### FastAPI Endpoints
- Keep endpoints thin:
  - Parse/validate request
  - Call storage/business logic
  - Return response model
- Use `HTTPException` for expected errors (e.g., not found, invalid input).
- Always return Pydantic response models where applicable.

### Data Models (Pydantic)
- Use `Field(..., description="...")` for all model fields.
- Keep request models separate from response models:
  - `PromptCreate`, `PromptUpdate` for requests
  - `Prompt` for responses (includes `id`, timestamps)

### Storage Layer
- Keep storage logic inside `app/storage.py`.
- Do not store global mutable state outside of the Storage class (except the `storage` singleton instance).
- Return `None` for not found (do not raise inside storage layer).
- API layer is responsible for raising `HTTPException`.

### Utility Functions
- Keep generic, reusable helpers in `app/utils.py`.
- Avoid importing FastAPI into utilities.
- Utility functions should be side-effect free unless explicitly intended.

---

## 3) File Naming Conventions

Use the existing project structure:

- `backend/app/api.py` → FastAPI routes
- `backend/app/models.py` → Pydantic models
- `backend/app/storage.py` → in-memory storage
- `backend/app/utils.py` → helper functions
- `backend/tests/` → pytest tests
- `docs/` → documentation (Markdown)
- `specs/` → feature specifications (Markdown)
- `.github/` → GitHub workflows + instructions

Naming rules:
- Python files: `snake_case.py`
- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

---

## 4) Error Handling Approach

### API Layer (FastAPI)
- Use `HTTPException` with clear messages:
  - 404 for missing prompt/collection
  - 400 for invalid references (e.g., collection_id does not exist)
- Do not return raw dictionaries for errors; rely on `HTTPException(detail="...")`.

### Storage Layer
- Do not raise exceptions for missing objects.
- Return:
  - `None` when an object is not found
  - `False` when delete fails
- Let the API layer convert these outcomes into HTTP errors.

### Validation
- Use Pydantic validation through request models.
- Let FastAPI return `422 Unprocessable Entity` for schema validation errors.

---

## 5) Testing Requirements

### General Rules
- All new features must include tests.
- All bug fixes must include a test that would fail before the fix and pass after.
- Prefer unit tests for utilities and storage methods.
- Use API tests for endpoint behavior.

### Tools
- Use `pytest`.
- Keep tests in `backend/tests/`.
- Test names must describe behavior:
  - `test_create_prompt_returns_201`
  - `test_get_prompt_returns_404_when_missing`

### Expectations
- Run tests locally before committing:
  - `pytest -v`
- Keep behavior stable and predictable.
- Tests should be deterministic and not depend on execution order.

---

## Implementation Notes (Project-Specific)

- Prompts have timestamps: `created_at`, `updated_at`.
- Updates must refresh `updated_at`.
- Collections can be deleted; prompts assigned to that collection should be unassigned (`collection_id = None`).
- The API currently has no authentication; do not add auth unless requested in a feature spec.

---

## Output Quality Requirements

When generating code changes:
- Provide clean, minimal diffs.
- Avoid unnecessary refactors unless requested.
- Keep documentation updated (README, API_REFERENCE.md) when endpoints or request/response shapes change.
