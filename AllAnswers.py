from Day1.Challenge_1 import *
from Day2.Challenge_1 import *
from Day2.Challenge_2 import *
from Day3.Challenge_1 import *
from Day3.Challenge_2 import *

day = 3

if day == 1:
    print("Day 1!")
    input_lines = read_input_file_int("Day1/input1.txt")
    answer = get_previous_bigger(input_lines)
    print("The answer for day 1 challenge 1 is: " + str(answer)) # for some reason the +1 was needed (BUG)

    from Day1.Challenge_2 import calculate_all_sums_using_three_measurement_window
    three_sum_measurement_calculation = calculate_all_sums_using_three_measurement_window(input_lines)
    answer = get_previous_bigger(three_sum_measurement_calculation)
    print("The answer for day 1 challenge 2 is: " + str(answer))
elif day == 2:
    print("Day 2!")
    input_lines = read_input_file_string("Day2/input1.txt")
    tasks = convert_list_to_submarine_tasks(input_lines)
    performedTasks = perform_submarine_tasks(tasks)
    print("The answer for day 2 challenge 1 is: " + str(calculate_end_result(performedTasks)))

    performedTasks_new_style = perform_submarine_tasks_new_style(tasks)
    print("The answer for day 2 challenge 2 is: " + str(calculate_end_result(performedTasks_new_style)))
elif day == 3:
    print("Day 3!")
    input_lines = read_input_file_string("Day3/input1.txt")
    binaryGamma = create_binary_number_based_on_most_common_values(input_lines)
    binaryEpsilon = calculate_epsilon_based_on_gamma(binaryGamma)
    decimalGamma = convert_binary_to_decimal(binaryGamma)
    decimalEpsilon = convert_binary_to_decimal(binaryEpsilon)
    print("Gamma is: {} ({}) and epsilon is: {} ({}) which is multiplied {}".format(binaryGamma, decimalGamma, binaryEpsilon ,decimalEpsilon, (decimalEpsilon * decimalGamma)))

    print("The life support rating is: {}".format(calculate_life_support_rating(input_lines)))