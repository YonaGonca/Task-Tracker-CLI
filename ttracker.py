import argparse
import time
import json
import os

# JSON Adress
JSON_FILE = "data.json"

# Function that verifies if the JSON file exists. If not, it creat it.
def ensure_json_file_exists():
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as file:
            json.dump({"tasks": []}, file, indent=4)
        print(f"'{JSON_FILE}' File created automatically.")

# Function that read the JSON file
def read_json():
    ensure_json_file_exists()
    with open(JSON_FILE, "r") as file:
        return json.load(file)

# Function that write into the JSON file
def write_json(data):
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function that add a task to the JSON file
def add_task(task):
    data = read_json()
    task_id = len(data["tasks"]) 
    task_time = time.ctime(time.time())
    task_status = "todo"
    new_task = {"id": task_id, "description": task, "status": task_status, "createdAt": task_time, "updatedAt": task_time}
    data["tasks"].append(new_task)
    write_json(data)
    print(f'Task "{task}" added successfully with ID = "{task_id}".')

def update_task(id,new_task):
    data = read_json()
    find = False
    for i in data["tasks"]:
        if i["id"] == id:
            find = True
            i["description"] = new_task
            i["updatedAt"] = time.ctime(time.time())
            write_json(data)
            print(f'Task ID = "{id}" updated successfully to "{new_task}".')
    if find == False:
        print(f"Task ID = \"{id}\" doesn\'t exists.")
            
def delete_task(id):
    data = read_json()
    find = False
    for i in data["tasks"]:
        if i["id"] == id:
            find = True
            data["tasks"].pop(id)
            write_json(data)
    if find == False:
        print(f"Task ID = \"{id}\" doesn\'t exists.")
    else:
        data = read_json()
        for i in data["tasks"]:
            if i["id"] > int(id):
                i["id"] = i["id"] - 1
        write_json(data)
        print(f'Task ID = "{id}" deleted successfully.')

def mark_in_progress(id):
    data = read_json()
    find = False
    for i in data["tasks"]:
        if i["id"] == id:
            find = True
            i["status"] = "in-progress"
            write_json(data)
            print(f'Task ID = "{id}" marked successfully to "in-progress".')
    if find == False:
        print(f"Task ID = \"{id}\" doesn\'t exists.")
  
  
def mark_done(id):
    data = read_json()
    find = False
    for i in data["tasks"]:
        if i["id"] == id:
            find = True
            i["status"] = "done"
            write_json(data)
            print(f'Task ID = "{id}" marked successfully to "done".')
    if find == False:
        print(f"Task ID = \"{id}\" doesn\'t exists.")
        
def mark_todo(id):
    data = read_json()
    find = False
    for i in data["tasks"]:
        if i["id"] == id:
            find = True
            i["status"] = "todo"
            write_json(data)
            print(f'Task ID = "{id}" marked successfully to "todo".')
    if find == False:
        print(f"Task ID = \"{id}\" doesn\'t exists.")
          
# Function that lists all the tasks of the JSON file
def list_tasks(status="all"):
    data = read_json()
    for i in data["tasks"]:
        print(i['id'],i['description'])
    


def main():
    # Crear el parser principal
    parser = argparse.ArgumentParser(description=" CLI Aplication to track your tasks")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Comando para añadir una tarea
    add_parser = subparsers.add_parser("add", help="Añadir una nueva tarea")
    add_parser.add_argument("task", type=str, help="Descripción de la tarea")
    
    # Comando para listar las tareas
    list_parser = subparsers.add_parser("list", help="List all the tasks")
    list_parser.add_argument("status", type=str, help="Status of the task", nargs="?",  default="all")


    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="ID of the task")
    update_parser.add_argument("new_task", type=str, help="New description of the task")
    
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task")
    
    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as \"in-progress\"")
    mark_in_progress_parser.add_argument("id", type=int, help="ID of the task")
    
    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as \"done\"")
    mark_done_parser.add_argument("id", type=int, help="ID of the task")
    
    mark_todo_parser = subparsers.add_parser("mark-todo", help="Mark a task as \"todo\"")
    mark_todo_parser.add_argument("id", type=int, help="ID of the task")

    # Parsear los argumentos
    args = parser.parse_args()

    # Ejecutar el comando correspondiente
    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks(args.status)
    elif args.command == "update":
        update_task(args.id, args.new_task)
    elif args.command == "delete":
       delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_in_progress(args.id)
    elif args.command == "mark-done":
        mark_done(args.id)
    elif args.command == "mark-todo":
        mark_todo(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    ensure_json_file_exists()
    main()