# PromptLab

AI Prompt Engineering Platform for managing reusable prompts and collections through a REST API.

---

## Table of Contents

- [Project Overview and Purpose](#project-overview-and-purpose)
- [Features List](#features-list)
- [Tech Stack](#tech-stack)
- [Prerequisites and Installation](#prerequisites-and-installation)
- [Quick Start Guide](#quick-start-guide)
- [API Endpoint Summary with Examples](#api-endpoint-summary-with-examples)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Contributing Guidelines](#contributing-guidelines)
- [Summary](#summary)

---

# Project Overview and Purpose

PromptLab is an **AI Prompt Engineering Platform** designed to help AI engineers store, organize, and manage prompts efficiently.

It provides a structured environment where prompts can be created, updated, organized into collections, and retrieved using a REST API. The system enables teams to reuse prompt templates, manage prompt collections, and build better workflows for AI-powered applications.

The platform is built using **FastAPI and Python**, making it lightweight, scalable, and easy to extend for future improvements such as database integration and frontend interfaces.

---

# Features List

PromptLab currently provides the following features:

- Create, read, update, and delete prompts
- Organize prompts into collections
- Search prompts by title or description
- Filter prompts by collection
- Automatic timestamp tracking
- REST API built with FastAPI
- In-memory storage for rapid development
- Interactive API documentation using Swagger

### Future Improvements

- Database integration
- Authentication and authorization
- Prompt versioning
- Tagging system
- Web-based frontend interface

---

# Tech Stack

PromptLab is built using the following technologies:

- **Python 3.10+** – Core programming language
- **FastAPI** – High-performance API framework
- **Pydantic** – Data validation and serialization
- **Pytest** – Testing framework
- **GitHub** – Version control and collaboration

---

# Prerequisites and Installation

Before running PromptLab, ensure the following are installed:

- Python 3.10 or higher
- Git
- pip (Python package manager)

Clone the repository:

```bash
git clone <your-repo-url>
cd promptlab
```

Install backend dependencies:

```bash
cd backend
pip install -r requirements.txt
```

---

# Quick Start Guide

Start the PromptLab backend server:

```bash
cd backend
python main.py
```

The API will run at:

```
http://localhost:8000
```

FastAPI automatically generates interactive API documentation.

Visit:

```
http://localhost:8000/docs
```

You can test API endpoints directly from the browser.

---

# API Endpoint Summary with Examples

## Health Endpoint

| Method | Endpoint | Description |
|------|------|------|
| GET | /health | Check API health status |

Example:

```bash
curl -X GET http://localhost:8000/health
```

Example Response

```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

## Prompt Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | /prompts | Retrieve all prompts |
| GET | /prompts/{prompt_id} | Retrieve a specific prompt |
| POST | /prompts | Create a new prompt |
| PUT | /prompts/{prompt_id} | Update an existing prompt |
| DELETE | /prompts/{prompt_id} | Delete a prompt |

Example: Create Prompt

```http
POST /prompts
```

```json
{
  "title": "Summarize Text",
  "content": "Summarize the following: {{input}}",
  "description": "Summarizes input text"
}
```

---

## Collection Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | /collections | Retrieve all collections |
| GET | /collections/{collection_id} | Retrieve a specific collection |
| POST | /collections | Create a new collection |
| DELETE | /collections/{collection_id} | Delete a collection |

Example:

```bash
curl -X GET http://localhost:8000/collections
```

---

# Development Setup

Prepare the development environment:

```bash
cd backend
pip install -r requirements.txt
python main.py
```

Run tests:

```bash
cd backend
pytest tests/ -v
```

Run tests with coverage:

```bash
pytest tests/ --cov=app
```

---

# Project Structure

```
promptlab/
├── README.md
├── PROJECT_BRIEF.md
├── backend/
│   ├── app/
│   │   ├── api.py
│   │   ├── models.py
│   │   ├── storage.py
│   │   └── utils.py
│   ├── tests/
│   ├── main.py
│   └── requirements.txt
│
├── docs/
│   └── API_REFERENCE.md
│
├── frontend/
│   └── (future frontend application)
│
├── specs/
│   ├── prompt-versions.md
│   └── tagging-system.md
│
└── .github/
    └── copilot-instructions.md
```

---

# Documentation

Additional documentation is available in the following files:

- **API Reference:** `docs/API_REFERENCE.md`
- **Feature Specifications:**
  - `specs/prompt-versions.md`
  - `specs/tagging-system.md`

These documents provide detailed API explanations and planned feature specifications.

---

# Contributing Guidelines

To contribute to PromptLab:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes
4. Run tests locally
5. Push your branch and create a Pull Request

Example workflow:

```bash
git checkout -b feature/update-readme
git add .
git commit -m "Improve README documentation"
git push origin feature/update-readme
```

All contributions should follow clean coding practices and include documentation where necessary.

---

# Summary

PromptLab provides a structured platform for managing AI prompts using a modern backend stack based on **FastAPI and Python**.

It supports prompt management, collection organization, and search functionality, forming the foundation for a scalable AI prompt engineering platform.

Future development may include database support, authentication systems, prompt version tracking, tagging features, and a web-based frontend interface.
