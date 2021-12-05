test_input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


def calculate_oxygen_generator_rating(lines):
    listOfNumbers = lines

    for x in range(len(lines[0])): # get length of first item and assume the others have same length
        print("Remaining numbers in list: " + str(listOfNumbers))
        count0 = 0
        count1 = 0 # reset values for each new char
        for line in listOfNumbers:
            if line[x] == "0":
                count0 += 1
            else:
                count1 += 1
        if count0 == count1:
            listOfNumbers = remove_item_from_list_based_on_binary_number_in_position(listOfNumbers, "1", x)
        elif count0 > count1:
            listOfNumbers = remove_item_from_list_based_on_binary_number_in_position(listOfNumbers, "0", x)
        elif count1 > count0:
            listOfNumbers = remove_item_from_list_based_on_binary_number_in_position(listOfNumbers, "1", x)
        if len(listOfNumbers) == 1:
            return listOfNumbers[0]


def calculate_co2_scrubber_rating(lines):
    listOfNumbers = lines

    for x in range(len(lines[0])): # get length of first item and assume the others have same length
        print("Remaining numbers in list: " + str(listOfNumbers))
        count0 = 0
        count1 = 0 # reset values for each new char
        for line in listOfNumbers:
            if line[x] == "0":
                count0 += 1
            else:
                count1 += 1
        if count0 == count1:
            listOfNumbers = remove_item_from_list_based_on_binary_number_in_position(listOfNumbers, "0", x)
        elif count0 > count1:
            listOfNumbers = remove_item_from_list_based_on_binary_number_in_position(listOfNumbers, "1", x)
        elif count1 > count0:
            listOfNumbers = remove_item_from_list_based_on_binary_number_in_position(listOfNumbers, "0", x)
        if len(listOfNumbers) == 1:
            return listOfNumbers[0]


def remove_item_from_list_based_on_binary_number_in_position(lines, dominantNumber, position):
    listWithValidNumbers = []
    for line in lines:
        if line[position] == dominantNumber:
            listWithValidNumbers.append(line)
    return listWithValidNumbers


def convert_binary_to_decimal(binaryNumber):
    return int(binaryNumber, 2)


def calculate_life_support_rating(lines):
    oxygen = calculate_oxygen_generator_rating(lines)
    co2 = calculate_co2_scrubber_rating(lines)
    multiplied = convert_binary_to_decimal(oxygen) * convert_binary_to_decimal(co2)
    return multiplied




