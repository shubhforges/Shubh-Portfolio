import json
import os

TASK_FILE = "data/tasks.json"

def load():
    try:
        return json.load(open(TASK_FILE))
    except:
        return []

def save(data):
    json.dump(data, open(TASK_FILE, "w"), indent=4)

def add_task(cmd):
    tasks = load()
    title = cmd.replace("add task", "").strip()

    tasks.append({
        "title": title,
        "progress": 0
    })

    save(tasks)
    return "Task added"

def list_tasks(cmd=None):
    tasks = load()
    return "\n".join([t["title"] for t in tasks]) or "No tasks"
