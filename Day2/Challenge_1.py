from dataclasses import dataclass

test_input = ["forward 2", "up 5", "down 3", "forward 6"]


def convert_list_to_submarine_tasks(list):
    submarineTasks = []
    for x in list:
        st = SubmarineTask("", 0)
        st.direction = x.split(" ")[0]
        st.amount = int(x.split(" ")[1])
        submarineTasks.append(st)
    print(submarineTasks)
    return submarineTasks


def perform_submarine_tasks(tasks):
    horizontalPosition = 0
    depth = 0

    for task in tasks:
        if task.direction == "forward":
            horizontalPosition += task.amount
        elif task.direction == "down":
            depth += task.amount
        elif task.direction == "up":
            depth -= task.amount
        else:
            print("WARNING: Task with unknown direction in tasks list")
    return PostTasks(horizontalPosition, depth)


def calculate_end_result(postTask):
    return postTask.horizontal * postTask.depth


@dataclass
class SubmarineTask:
    direction: str
    amount: int

@dataclass
class PostTasks:
    horizontal: int
    depth: int
