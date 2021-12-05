def get_previous_bigger(lines):
    biggerThanPrevious = 0
    for x in range(len(lines)):
        if x != 0:
            if lines[x] > lines[x - 1]:
                biggerThanPrevious += 1
    return biggerThanPrevious


# Get all numbers of the file as array of numbers
def read_input_file(filename):
    text_file = open(filename, "r")
    lines = text_file.readlines()
    text_file.close()
    strip_newline_chars(lines)
    desired_array = [int(numeric_string) for numeric_string in lines]
    return desired_array


def strip_newline_chars(lines):
    for x in range(len(lines)):
        lines[x] = lines[x].strip()

