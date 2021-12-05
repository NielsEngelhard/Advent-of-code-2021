def create_binary_number_based_on_most_common_values(lines):
    gamma = ""

    for x in range(len(lines[0])): # get length of first item and assume the others have same length
        count0 = 0
        count1 = 0 # reset values for each new char
        for line in lines:
            print(line)
            if line[x] == "0":
                count0 += 1
            else:
                count1 += 1
        if count0 == count1:
            print("ERROR: Values are the same, not prepared for this situation :(")
        elif count0 > count1:
            gamma += "0"
        elif count1 > count0:
            gamma += "1"
    return gamma


def calculate_epsilon_based_on_gamma(gamma):
    epsilon = ""
    for x in range(len(gamma)):
        if gamma[x] == "0":
            epsilon += "1"
        else:
            epsilon += "0"
    return epsilon


def convert_binary_to_decimal(binaryNumber):
    return int(binaryNumber, 2)
