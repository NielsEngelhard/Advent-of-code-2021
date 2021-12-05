def calculate_all_sums_using_three_measurement_window(lines):
    proceed = True
    value1Counter = 0
    value2Counter = 1
    value3Counter = 2
    allSums = []

    while proceed:
        value1 = lines[value1Counter]
        value2 = lines[value2Counter]
        value3 = lines[value3Counter]

        totalValue = (value1 + value2 + value3)
        allSums.append(totalValue)

        value1Counter += 1
        value2Counter += 1
        value3Counter += 1

        if (value3Counter == len(lines)):
            proceed = False
    return allSums
