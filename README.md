PromptLab

AI Prompt Engineering Platform

Project Overview

PromptLab is a backend application for managing AI prompt templates.

It allows AI engineers to create, organize, update, and retrieve prompt templates through a REST API built with FastAPI.

This project demonstrates professional backend development practices including:

RESTful API design

Documentation standards

Testing with pytest

CI/CD integration

Docker containerization

Purpose of the Project

PromptLab is designed to provide a structured way to manage reusable AI prompts.

The platform allows users to:

Store prompt templates

Organize prompts into collections

Retrieve prompts by ID

Update prompts fully or partially

Track creation and modification timestamps

Over four weeks, this project evolves into a production-ready full-stack application.

Features
Prompt Management

Create a prompt

Retrieve all prompts

Retrieve a prompt by ID

Update a prompt (PUT)

Partially update a prompt (PATCH)

Delete a prompt

Automatic created_at and updated_at tracking

Collection Management

Create collection

Retrieve collections

Retrieve collection by ID

Delete collection

Prerequisites

Before running the project, ensure you have:

Python 3.10+

pip

Git

Node.js 18+ (for frontend development)

Docker (optional for containerization)

Installation

Clone the repository:

git clone <your-repository-url>
cd promptlab


Install backend dependencies:

cd backend
pip install -r requirements.txt

Quick Start

Run the backend server:

cd backend
python main.py


The API will be available at:

http://localhost:8000

Interactive API documentation (Swagger UI):

http://localhost:8000/docs

API Endpoint Summary
Health

GET /health

Prompts

GET /prompts
GET /prompts/{id}
POST /prompts
PUT /prompts/{id}
PATCH /prompts/{id}
DELETE /prompts/{id}

Example: Create Prompt

Request:

POST /prompts
{
  "title": "Summarize Text",
  "content": "Summarize the following: {{input}}",
  "collection_id": "1"
}


Response:

{
  "id": "123",
  "title": "Summarize Text",
  "content": "Summarize the following: {{input}}",
  "collection_id": "1",
  "created_at": "2024-01-01T10:00:00",
  "updated_at": "2024-01-01T10:00:00"
}

Collections

GET /collections
GET /collections/{id}
POST /collections
DELETE /collections/{id}

Running Tests

Run tests:

cd backend
pytest tests/ -v


Run tests with coverage:

pytest tests/ -v --cov=app --cov-report=term-missing

Development Setup

Project structure:

promptlab/
├── backend/
│   ├── app/
│   ├── tests/
│   └── main.py
├── frontend/
├── docs/
├── specs/
└── .github/


Development guidelines:

Follow RESTful API principles

Add docstrings to all functions and classes

Write tests for new features

Maintain meaningful commit history

Ensure tests pass before pushing

Contributing

Create a new branch

Make your changes

Ensure all tests pass

Commit with clear messages

Push and open a Pull Request

License

This project is developed for educational purposes as part of the PromptLab engineering assignment.