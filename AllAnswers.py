from Day1.Challenge_1 import read_input_file, get_previous_bigger

day = 1

if day == 1:
    input_lines = read_input_file("Day1/input1.txt")
    answer = get_previous_bigger(input_lines)
    print("The answer for day 1 challenge 1 is: " + str(answer)) # for some reason the +1 was needed (BUG)

    from Day1.Challenge_2 import calculate_all_sums_using_three_measurement_window
    three_sum_measurement_calculation = calculate_all_sums_using_three_measurement_window(input_lines)
    answer = get_previous_bigger(three_sum_measurement_calculation)
    print("The answer for day 1 challenge 2 is: " + str(answer))
elif day == 2:
    print("")