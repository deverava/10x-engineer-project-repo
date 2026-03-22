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

This project demonstrates **real-world full-stack development**, including API design, frontend integration, and UI/UX design.

---

## ✨ Features List

### 🔧 Backend Features
- Create, read, update, and delete prompts
- Organize prompts into collections
- Search prompts by title/content
- Filter prompts by collection
- Automatic timestamp tracking
- REST API built with FastAPI
- In-memory storage for rapid development
- Interactive API documentation (Swagger)

### 🎨 Frontend Features
- Responsive React dashboard (Vite)
- Sidebar with collections
- Create, edit, and delete prompts
- Create and manage collections
- Search prompts dynamically
- Prompt detail view
- Clean UI with modern styling
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
- CSS (Custom styling)

### Tools
- Git & GitHub
- Codespaces
- Uvicorn

---

## ⚙️ Prerequisites and Installation

Before running PromptLab, ensure the following are installed:

- Python 3.10+
- Node.js (v16+ recommended)
- Git
- pip

Clone the repository:

```bash
git clone <your-repo-url>
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

```
http://127.0.0.1:8000
```

Swagger Docs:

```
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

```
http://localhost:5173
```

---

## 🔗 API Integration

Make sure frontend uses:

```js
const BASE_URL = "http://127.0.0.1:8000";
```

⚠️ Do not use Codespaces URL for final submission.

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
| POST | /collections | Create a new collection |
| DELETE | /collections/{id} | Delete a collection |

---

## 🧪 Development Setup

Run backend:

```bash
cd backend
pip install -r requirements.txt
uvicorn app.api:app --reload
```

Run tests:

```bash
pytest tests/ -v --cov=app
```

Run frontend:

```bash
cd frontend
npm install
npm run dev
```

---

## 📂 Project Structure

```
10x-engineer-project-repo/
│
├── backend/
│   ├── app/
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 🎨 Frontend Features

- Dashboard view for prompts
- Sidebar for collections
- Prompt creation form
- Edit and delete functionality
- Search and filtering
- Responsive UI design

---

## 📚 Documentation

Additional documentation:

- API Reference: `docs/API_REFERENCE.md`
- Feature Specs:
  - `specs/prompt-versions.md`
  - `specs/tagging-system.md`

---

## 🤝 Contributing Guidelines

1. Fork the repository  
2. Create a new branch  
3. Make your changes  
4. Run tests  
5. Submit a pull request  

Example:

```bash
git checkout -b feature/update-readme
git add .
git commit -m "Improve README"
git push origin feature/update-readme
```

---

## 📝 Summary

PromptLab is a **full-stack AI prompt management platform** built using FastAPI and React.

It supports:
- Prompt CRUD operations
- Collection management
- Search and filtering
- Modern frontend dashboard

This project demonstrates practical full-stack development and can be extended with features like authentication, database integration, and cloud deployment.

---

## ✅ Status

✔ Backend Completed  
✔ Frontend Completed  
✔ Full CRUD Working  
✔ API Integration Working  
✔ Responsive UI Implemented  

---