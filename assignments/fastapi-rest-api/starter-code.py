"""
FastAPI Task Management API - Starter Code

This starter code provides the basic structure for building a REST API
with FastAPI. Complete the TODOs to implement a full task management system.

To run this application:
1. Install dependencies: pip install fastapi uvicorn
2. Run the server: uvicorn starter-code:app --reload
3. Visit http://localhost:8000/docs to see the interactive API documentation
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

# Create FastAPI application instance
app = FastAPI(
    title="Task Management API",
    description="A simple REST API for managing tasks",
    version="1.0.0"
)

# TODO: Define the Task model using Pydantic
class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1, description="Task title cannot be empty")
    description: str = Field(..., min_length=5, description="Task description must be at least 5 characters")
    completed: bool = False

# In-memory storage for tasks
tasks: List[Task] = []
task_id_counter = 1


# TODO: Task 1 - Create a welcome endpoint
@app.get("/")
async def root():
    """
    Welcome endpoint that returns a greeting message.
    """
    # TODO: Return a welcome message dictionary
    pass


# TODO: Task 2 - Create endpoint to add a new task
@app.post("/tasks", status_code=201)
async def create_task(task: Task):
    """
    Create a new task.
    
    Args:
        task: Task object with title, description, and completed status
        
    Returns:
        The created task with its assigned ID
    """
    # TODO: Implement task creation logic
    # Hint: Use the global task_id_counter and tasks list
    pass


# TODO: Task 2 - Get all tasks with optional filtering
@app.get("/tasks")
async def get_tasks(completed: Optional[bool] = None):
    """
    Retrieve all tasks, optionally filtered by completion status.
    
    Args:
        completed: Optional filter for completed status
        
    Returns:
        List of tasks
    """
    # TODO: Implement task retrieval with optional filtering
    pass


# TODO: Task 2 - Get a specific task by ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    """
    Retrieve a specific task by its ID.
    
    Args:
        task_id: The ID of the task to retrieve
        
    Returns:
        The task object
        
    Raises:
        HTTPException: If task is not found
    """
    # TODO: Implement task retrieval by ID
    # Hint: Raise HTTPException(status_code=404, detail="Task not found") if task doesn't exist
    pass


# TODO: Task 2 - Update an existing task
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, updated_task: Task):
    """
    Update an existing task.
    
    Args:
        task_id: The ID of the task to update
        updated_task: The updated task data
        
    Returns:
        The updated task object
        
    Raises:
        HTTPException: If task is not found
    """
    # TODO: Implement task update logic
    pass


# TODO: Task 2 - Delete a task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """
    Delete a task by its ID.
    
    Args:
        task_id: The ID of the task to delete
        
    Returns:
        Success message
        
    Raises:
        HTTPException: If task is not found
    """
    # TODO: Implement task deletion logic
    pass


# BONUS: Add any additional endpoints or features you think would be useful!
