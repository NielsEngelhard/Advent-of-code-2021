from Day1.Challenge_1 import read_input_file_int, read_input_file_string, get_previous_bigger
from Day2.Challenge_1 import convert_list_to_submarine_tasks, perform_submarine_tasks, calculate_end_result
from Day2.Challenge_2 import perform_submarine_tasks_new_style

day = 2

if day == 1:
    input_lines = read_input_file_int("Day1/input1.txt")
    answer = get_previous_bigger(input_lines)
    print("The answer for day 1 challenge 1 is: " + str(answer)) # for some reason the +1 was needed (BUG)

    from Day1.Challenge_2 import calculate_all_sums_using_three_measurement_window
    three_sum_measurement_calculation = calculate_all_sums_using_three_measurement_window(input_lines)
    answer = get_previous_bigger(three_sum_measurement_calculation)
    print("The answer for day 1 challenge 2 is: " + str(answer))
elif day == 2:
    input_lines = read_input_file_string("Day2/input1.txt")
    tasks = convert_list_to_submarine_tasks(input_lines)
    performedTasks = perform_submarine_tasks(tasks)
    print("The answer for day 2 challenge 1 is: " + str(calculate_end_result(performedTasks)))

    performedTasks_new_style = perform_submarine_tasks_new_style(tasks)
    print("The answer for day 2 challenge 2 is: " + str(calculate_end_result(performedTasks_new_style)))