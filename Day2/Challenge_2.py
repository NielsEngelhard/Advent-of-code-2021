from dataclasses import dataclass

test_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def perform_submarine_tasks_new_style(tasks):
    horizontalPosition = 0
    depth = 0
    aim = 0

    for task in tasks:
        if task.direction == "forward":
            horizontalPosition += task.amount
            if aim != 0:
                depth += (task.amount * aim)
        elif task.direction == "down":
            aim += task.amount
        elif task.direction == "up":
            aim -= task.amount
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
