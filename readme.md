# Task Tracker CLI

A command-line interface (CLI) application to help you track and manage your tasks. This application allows you to create, list, update, delete, and mark tasks with different statuses such as "todo", "in-progress", and "done".

## Features

- Add a new task
- List all tasks or filter tasks by status
- Update a task's description
- Delete a task
- Change task statuses (Todo, In-progress, Done)

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/YonaGonca/Task-Tracker-CLI.git
   cd task-tacker-cli
    ```

## Usage

### Adding a Task

To add a new task, use the add command:

```
python ttracker.py add "Your task description"
```

### Listing Tasks

To list all tasks:

```
python ttracker.py list
```

To list tasks filtered by status (you can choose from `todo`, `in-progress`, or `done`)

```
python ttracker.py list done
```

### Updating a Task

To update the description of a task:

```
python ttracker.py update <task_id> "New task description"
```

### Deleting a Task

To delete a task by its ID:

```
python ttracker.py delete <task_id>
```

### Marking Tasks

To mark a task as "in-progress":

```
python ttracker.py mark-in-progress <task_id>
```

To mark a task as "done":

```
python ttracker.py mark-done <task_id>
```

To mark a task as "todo":

```
python ttracker.py todo <task_id>
```

## JSON Data File

This project uses a JSON file (`data.json`) to store task data. The file is automatically created if it doesn't already exist.

- **data.json** contains a list of tasks, with each task having the following properties:
  - `id`: A unique identifier for the task.
  - `description`: The description of the task.
  - `status`: The current status of the task (`todo`, `in-progress`, `done`).
  - `createdAt`: The time when the task was created.
  - `updatedAt`: The time when the task was last updated.

## Code Structure

- `ttracker.py`: The main Python script containing the logic for managing tasks.
- `data.json`: The JSON file that stores task data.

## Contributing

Feel free to fork this repository and make improvements. If you find any bugs or want to suggest new features, open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Python for providing the tools to build yhis CLI.

