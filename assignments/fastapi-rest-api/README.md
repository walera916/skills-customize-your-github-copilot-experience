# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Build a REST API using FastAPI to practice route definitions, request validation, and JSON response handling.

## 📝 Tasks

### 🛠️ Build API Endpoints

#### Description

Create a FastAPI application with endpoints for listing items, retrieving a single item by ID, and adding new items.

#### Requirements
Completed program should:

- Import and use `FastAPI` to create the application
- Define at least three endpoints: `GET /items`, `GET /items/{item_id}`, and `POST /items`
- Use Pydantic models for request and response data validation
- Return JSON responses with appropriate HTTP status codes
- Handle missing items by raising `HTTPException(status_code=404)`

### 🛠️ Add Query and Update Support

#### Description

Extend the API so users can filter results with query parameters and update existing items.

#### Requirements
Completed program should:

- Add an optional `limit` query parameter to `GET /items`
- Add a `PUT /items/{item_id}` endpoint to update item data
- Validate incoming update requests using a Pydantic model
- Return updated item data after a successful update
- Include example request/response behavior in comments or documentation
