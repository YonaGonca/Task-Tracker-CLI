import argparse
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
    new_task = {"id": task_id, "description": task}
    data["tasks"].append(new_task)
    write_json(data)
    print(f'Task "{task}" added successfully with ID = "{task_id}".')
    
# Function that lists all the tasks of the JSON file
def list_tasks():
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

    # Parsear los argumentos
    args = parser.parse_args()

    # Ejecutar el comando correspondiente
    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "remove":
        remove_task(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    ensure_json_file_exists()
    main()