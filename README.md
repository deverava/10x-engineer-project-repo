# 🚀 PromptLab

AI Prompt Engineering Platform for managing reusable prompts and collections through a REST API and modern React frontend.

---

## 📌 Table of Contents

- [Project Overview and Purpose](#project-overview-and-purpose)
- [Features List](#features-list)
- [Tech Stack](#tech-stack)
- [Prerequisites and Installation](#prerequisites-and-installation)
- [Quick Start Guide](#quick-start-guide)
- [API Endpoint Summary](#api-endpoint-summary)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Frontend Features](#frontend-features)
- [Documentation](#documentation)
- [Contributing Guidelines](#contributing-guidelines)
- [Summary](#summary)

---

## 📖 Project Overview and Purpose

PromptLab is a **Full Stack AI Prompt Engineering Platform** designed to help engineers store, organize, search, and manage prompts efficiently.

It provides:
- A **FastAPI backend** for prompt and collection management
- A **React frontend dashboard** for user interaction
- A structured workflow for reusable prompt templates

This project demonstrates practical **full-stack development**, including backend API design, frontend integration, testing, and UI/UX implementation.

---

## ✨ Features List

### 🔧 Backend Features
- Create, read, update, and delete prompts
- Organize prompts into collections
- Search prompts by title and content
- Filter prompts by collection
- Automatic timestamp tracking
- REST API built with FastAPI
- In-memory storage for rapid development
- Interactive API documentation using Swagger

### 🎨 Frontend Features
- Responsive React dashboard built with Vite
- Sidebar for collections
- Create, edit, and delete prompts
- Create and manage collections
- Search prompts dynamically
- Prompt detail view
- Modern styled UI
- Loading and error handling

---

## 🏗️ Tech Stack

### Backend
- Python 3.10+
- FastAPI
- Pydantic
- Pytest

### Frontend
- React (Vite)
- JavaScript (ES6+)
- CSS

### Tools
- Git & GitHub
- Uvicorn

---

## ⚙️ Prerequisites and Installation

Before running PromptLab, ensure the following are installed:

- Python 3.10 or higher
- Node.js v16 or higher
- Git
- pip

Clone the repository:

```bash
git clone <your-repository-url>
cd 10x-engineer-project-repo
```

---

## 🚀 Quick Start Guide

### ▶️ Run Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.api:app --reload --host 0.0.0.0 --port 8000
```

Backend will run at:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

### ▶️ Run Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

---

## 🔗 API Integration

The frontend API client should use this base URL:

```javascript
const BASE_URL = "http://127.0.0.1:8000";
```

---

## 📡 API Endpoint Summary

### Health Endpoint

| Method | Endpoint | Description |
|------|------|------|
| GET | /health | Check API health status |

---

### Prompt Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | /prompts | Retrieve all prompts |
| GET | /prompts/{id} | Retrieve a specific prompt |
| POST | /prompts | Create a new prompt |
| PUT | /prompts/{id} | Update an existing prompt |
| DELETE | /prompts/{id} | Delete a prompt |

---

### Collection Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | /collections | Retrieve all collections |
| GET | /collections/{id} | Retrieve a specific collection |
| POST | /collections | Create a new collection |
| DELETE | /collections/{id} | Delete a collection |

---

## 🧪 Development Setup

### Run Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.api:app --reload
```

### Run Tests

```bash
cd backend
pytest tests/ -v --cov=app
```

### Run Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 📂 Project Structure

```text
10x-engineer-project-repo/
├── .github/
│   └── workflows/
│       └── ci.yml
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── models.py
│   │   ├── storage.py
│   │   └── utils.py
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_api.py
│   │   ├── test_models.py
│   │   ├── test_storage.py
│   │   ├── test_tagging_feature.py
│   │   └── test_utils.py
│   ├── Dockerfile
│   ├── main.py
│   ├── pytest.ini
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   ├── client.js
│   │   │   ├── collections.js
│   │   │   └── prompts.js
│   │   ├── components/
│   │   │   ├── collections/
│   │   │   ├── layout/
│   │   │   ├── prompts/
│   │   │   └── shared/
│   │   ├── styles/
│   │   │   └── global.css
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── .env
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml
└── README.md
```

---

## 🎨 Frontend Features

- Dashboard view for all prompts
- Sidebar for collection navigation
- Prompt creation and editing form
- Prompt delete functionality
- Collection creation and deletion
- Prompt filtering by collection
- Search functionality
- Responsive layout with modern styling

---

## 📚 Documentation

Additional documentation is available in the following files:

- API Reference: `docs/API_REFERENCE.md`
- Feature Specifications:
  - `specs/prompt-versions.md`
  - `specs/tagging-system.md`

---

## 🤝 Contributing Guidelines

To contribute to PromptLab:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes
4. Run tests locally
5. Push your branch and create a Pull Request

Example:

```bash
git checkout -b feature/update-readme
git add .
git commit -m "Improve README documentation"
git push origin feature/update-readme
```

All contributions should follow clean coding practices and include documentation where necessary.

---

## 📝 Summary

PromptLab is a **full-stack AI prompt management platform** built using FastAPI and React.

It supports:
- Prompt CRUD operations
- Collection management
- Search and filtering
- Frontend-backend integration
- Responsive dashboard UI

This project demonstrates practical backend development, frontend integration, testing, and full-stack application design.

---

## ✅ Status

- Backend API Completed
- Frontend Completed
- Full CRUD Functionality Working
- API Integration Working
- Responsive UI Implemented

---