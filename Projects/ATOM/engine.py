from ai import ask_ai
from modules import tasks, maps, music, search

def detect(cmd):
    if "distance between" in cmd: return "distance"
    if cmd.startswith("route"): return "route"
    if cmd.startswith("add task"): return "add_task"
    if cmd.startswith("list tasks"): return "list_tasks"
    if cmd.startswith("play"): return "music"
    if "search" in cmd: return "search"
    return "ai"


def run(cmd):
    intent = detect(cmd)

    if intent == "add_task":
        return tasks.add_task(cmd)

    if intent == "list_tasks":
        return tasks.list_tasks(cmd)

    if intent == "music":
        return music.play(cmd)

    if intent == "search":
        return search.web_search(cmd)

    if intent == "distance":
        return maps.distance(cmd)

    if intent == "route":
        return maps.route(cmd)

    return ask_ai(cmd)
