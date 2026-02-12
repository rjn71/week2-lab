# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework in Python. You will create a simple task management API that handles creating, reading, updating, and deleting (CRUD) tasks, demonstrating fundamental concepts of API development and HTTP methods.

## 📝 Tasks

### 🛠️	Task 1: Set Up Your FastAPI Project

#### Description
Install FastAPI and create a basic API server with a welcome endpoint. This task introduces you to the FastAPI framework and helps you understand how to run a local development server.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn using pip (`pip install fastapi uvicorn`)
- Create a FastAPI application instance
- Define a GET endpoint at the root path (`/`) that returns a welcome message
- Run the server using Uvicorn and verify it works by visiting `http://localhost:8000`
- Include automatic API documentation at `http://localhost:8000/docs`


### 🛠️	Task 2: Create Task Management Endpoints

#### Description
Build a complete task management system with endpoints to create, retrieve, update, and delete tasks. Each task should have an ID, title, description, and completion status.

#### Requirements
Completed program should:

- Define a Task model using Pydantic with fields: `id` (int), `title` (str), `description` (str), and `completed` (bool)
- Implement a POST endpoint `/tasks` to create new tasks
- Implement a GET endpoint `/tasks` to retrieve all tasks
- Implement a GET endpoint `/tasks/{task_id}` to retrieve a specific task by ID
- Implement a PUT endpoint `/tasks/{task_id}` to update an existing task
- Implement a DELETE endpoint `/tasks/{task_id}` to remove a task
- Store tasks in a Python list (in-memory storage)
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Handle errors gracefully (e.g., task not found)


### 🛠️	Task 3: Add Data Validation and Testing

#### Description
Enhance your API with proper data validation and test your endpoints using the interactive documentation or a tool like Postman.

#### Requirements
Completed program should:

- Use Pydantic models to validate that task titles are not empty
- Ensure task descriptions have a minimum length of 5 characters
- Add optional query parameters to filter tasks by completion status (e.g., `/tasks?completed=true`)
- Test all endpoints using the automatic Swagger UI documentation at `/docs`
- Verify that invalid data returns appropriate error messages
- Document at least 3 different test scenarios you performed and their results
