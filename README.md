# PromptLab

**AI Prompt Engineering Platform**

PromptLab is a backend application for managing AI prompt templates. It provides a REST API built with FastAPI to create, organize, update, and retrieve prompts and collections.

---

## Project Overview and Purpose

PromptLab is designed for AI engineers who need a structured way to manage reusable prompts.

It helps teams:
- Store prompt templates with variables like `{{input}}` and `{{context}}`
- Organize prompts into collections
- Update prompts (full update and partial update)
- Track timestamps (`created_at`, `updated_at`) for changes

This project is built as a 4-week engineering assignment to practice backend development, documentation, testing, CI/CD, Docker, and frontend integration.

---

## Features

### Prompt Management
- Create a prompt
- List all prompts
- Get a prompt by ID
- Update a prompt (PUT)
- Partially update a prompt (PATCH)
- Delete a prompt
- Automatic `created_at` and `updated_at` timestamps

### Collection Management
- Create a collection
- List collections
- Get collection by ID
- Delete a collection

---

## Prerequisites and Installation

### Prerequisites
- Python 3.10+
- pip
- Git
- Node.js 18+ (for Week 4 frontend)
- Docker (optional, used in Week 3)

### Installation

Clone the repository:
```bash
git clone <your-repo-url>
cd promptlab

Install backend dependencies:

cd backend
pip install -r requirements.txt

Quick Start Guide

Run the backend server:

cd backend
python main.py


API will run at:

http://localhost:8000

Swagger API docs:

http://localhost:8000/docs

API Endpoint Summary (with example)
Health

GET /health

Prompts

GET /prompts

GET /prompts/{id}

POST /prompts

PUT /prompts/{id}

PATCH /prompts/{id}

DELETE /prompts/{id}

Collections

GET /collections

GET /collections/{id}

POST /collections

DELETE /collections/{id}

Example: Create Prompt

Request

POST /prompts

{
  "title": "Summarize Text",
  "content": "Summarize the following: {{input}}",
  "collection_id": "1"
}


Response

{
  "id": "123",
  "title": "Summarize Text",
  "content": "Summarize the following: {{input}}",
  "collection_id": "1",
  "created_at": "2024-01-01T10:00:00",
  "updated_at": "2024-01-01T10:00:00"
}

Development Setup

Project structure:

promptlab/
├── README.md
├── PROJECT_BRIEF.md
├── GRADING_RUBRIC.md
├── backend/
│   ├── app/
│   ├── tests/
│   ├── main.py
│   └── requirements.txt
├── frontend/      # Week 4
├── docs/          # Week 2
├── specs/         # Week 2
└── .github/       # Week 3


Developer notes:

Keep changes small and commit often

Ensure tests pass before pushing

Add docstrings for functions/classes during Week 2

Running Tests

Run tests:

cd backend
pytest tests/ -v


Run tests with coverage:

pytest tests/ -v --cov=app --cov-report=term-missing

Contributing Guidelines

Create a new branch

Make changes

Run tests locally

Commit with meaningful messages

Push branch and open a Pull Request

Example:

git checkout -b week2-readme
git add README.md
git commit -m "Week 2: Add comprehensive README"
git push origin week2-readme

License

This project is created for educational purposes as part of the PromptLab engineering assignment.