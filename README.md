# FastAPI To-Do Application

## Overview

This project is a simple To-Do application built using FastAPI. It allows you to manage a list of tasks, each of which has a title, description, due date, priority, and completion status.

## Features

The application supports the following endpoints:

1. **GET /tasks** - Retrieve the list of all tasks.
2. **POST /tasks** - Add a new task to the list. The request body should contain the task's title, description, due date, priority, and completion status.
3. **GET /tasks/{task_id}** - Retrieve the details of a task by its ID.
4. **PUT /tasks/{task_id}** - Update the details of a task by its ID. The request body should allow updating the title, description, due date, priority, and completion status.
5. **DELETE /tasks/{task_id}** - Delete a task by its ID.
6. **GET /tasks/due/{date}** - Retrieve the list of tasks due on a specific date.
7. **GET /tasks/priority/{priority}** - Retrieve the list of tasks with a specific priority.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Vidhi1290/FastAPI--To-do-task-docker.git
    cd FastAPI--To-do-task-docker
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install fastapi uvicorn
    ```

## Running the Application

1. Start the FastAPI application:
    ```sh
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to see the welcome message.

3. To view and interact with the API documentation, go to `http://127.0.0.1:8000/docs`.

## Dockerization

1. Build the Docker image:
    ```sh
    docker build -t vidhi1290/todo-app .
    ```

2. Run the Docker container:
    ```sh
    docker run -d -p 8000:8000 vidhi1290/todo-app
    ```

3. The application will be available at `http://localhost:8000`.

## Example

To add a task, you can send a POST request to `/tasks` with the following JSON body:
```json
{
    "id": 1,
    "title": "Sample Task",
    "description": "This is a sample task.",
    "due_date": "2023-12-31",
    "priority": 1,
    "completed": false
}
```

To retrieve all tasks, send a GET request to `/tasks`.
