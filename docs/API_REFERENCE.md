# PromptLab API Reference

This document provides detailed documentation for the PromptLab REST API.

The API allows users to create, manage, search, and organize AI prompts into collections.

---

# Base URL

When running locally:

http://localhost:8000

---

# Authentication

Currently, the PromptLab API **does not require authentication**.

All endpoints are publicly accessible.

Future versions of the API may include:

- API key authentication
- User accounts
- Role-based access control

---

# Content Type

All API requests and responses use **JSON**.

Request header:

Content-Type: application/json

---

# Error Response Format

When an error occurs, the API returns an HTTP status code and a JSON response.

Example error response:

{
  "detail": "Prompt not found"
}

Common status codes:

| Status Code | Meaning |
|-------------|--------|
| 200 | Success |
| 201 | Resource created |
| 204 | Resource deleted |
| 400 | Bad request |
| 404 | Resource not found |
| 422 | Validation error |

---

# Health Endpoint

## GET /health

Returns the health status of the API.

Example request:

GET /health

Example response:

{
  "status": "healthy",
  "version": "1.0.0"
}

---

# Prompt Endpoints

Prompts represent reusable prompt templates used for AI workflows.

Example Prompt Object:

{
  "id": "123",
  "title": "Summarize Text",
  "content": "Summarize the following: {{input}}",
  "description": "Summarizes text input",
  "collection_id": "1",
  "created_at": "2024-01-01T10:00:00",
  "updated_at": "2024-01-01T10:00:00"
}

---

## GET /prompts

Retrieve all prompts.

Example request:

GET /prompts

Example response:

{
  "prompts": [
    {
      "id": "123",
      "title": "Summarize Text",
      "content": "Summarize the following: {{input}}",
      "description": "Summarizes text input",
      "collection_id": "1",
      "created_at": "2024-01-01T10:00:00",
      "updated_at": "2024-01-01T10:00:00"
    }
  ],
  "total": 1
}

---

## GET /prompts/{prompt_id}

Retrieve a single prompt by ID.

Example request:

GET /prompts/123

Example response:

{
  "id": "123",
  "title": "Summarize Text",
  "content": "Summarize the following: {{input}}",
  "description": "Summarizes text input",
  "collection_id": "1",
  "created_at": "2024-01-01T10:00:00",
  "updated_at": "2024-01-01T10:00:00"
}

Error example:

{
  "detail": "Prompt not found"
}

---

## POST /prompts

Create a new prompt.

Example request:

{
  "title": "Translate Text",
  "content": "Translate this text: {{input}}",
  "description": "Translates input text",
  "collection_id": "1"
}

Example response:

{
  "id": "456",
  "title": "Translate Text",
  "content": "Translate this text: {{input}}",
  "description": "Translates input text",
  "collection_id": "1",
  "created_at": "2024-01-01T11:00:00",
  "updated_at": "2024-01-01T11:00:00"
}

Error example:

{
  "detail": "Collection not found"
}

---

## PUT /prompts/{prompt_id}

Update an existing prompt.

Example request:

{
  "title": "Updated Prompt",
  "content": "Updated prompt content",
  "description": "Updated description",
  "collection_id": "1"
}

Example response:

{
  "id": "456",
  "title": "Updated Prompt",
  "content": "Updated prompt content",
  "description": "Updated description",
  "collection_id": "1",
  "created_at": "2024-01-01T11:00:00",
  "updated_at": "2024-01-01T12:00:00"
}

---

## DELETE /prompts/{prompt_id}

Delete a prompt.

Example request:

DELETE /prompts/456

Response:

204 No Content

Error example:

{
  "detail": "Prompt not found"
}

---

# Collection Endpoints

Collections group multiple prompts together.

Example Collection Object:

{
  "id": "1",
  "name": "General Prompts",
  "description": "Common prompt templates",
  "created_at": "2024-01-01T09:00:00"
}

---

## GET /collections

Retrieve all collections.

Example request:

GET /collections

Example response:

{
  "collections": [
    {
      "id": "1",
      "name": "General Prompts",
      "description": "Common prompt templates",
      "created_at": "2024-01-01T09:00:00"
    }
  ],
  "total": 1
}

---

## GET /collections/{collection_id}

Retrieve a specific collection.

Example request:

GET /collections/1

Example response:

{
  "id": "1",
  "name": "General Prompts",
  "description": "Common prompt templates",
  "created_at": "2024-01-01T09:00:00"
}

Error example:

{
  "detail": "Collection not found"
}

---

## POST /collections

Create a new collection.

Example request:

{
  "name": "Marketing Prompts",
  "description": "Prompts used for marketing workflows"
}

Example response:

{
  "id": "2",
  "name": "Marketing Prompts",
  "description": "Prompts used for marketing workflows",
  "created_at": "2024-01-01T13:00:00"
}

---

## DELETE /collections/{collection_id}

Delete a collection.

Example request:

DELETE /collections/2

Response:

204 No Content

Error example:

{
  "detail": "Collection not found"
}
