from dataclasses import dataclass


def create_field(size):
    field = []
    for x in range(size):
        line = []
        for y in range(size):
            line.append(".")
        field.append(line)
    return field


def print_field(field):
    for line in field:
        print(line)


field = create_field(1000)


@dataclass
class Coordinate:
    right: int
    down: int


@dataclass
class Stripe:
    begin: Coordinate
    end: Coordinate

def get_to_draws_example():
    stripes = []
    stripes.append(Stripe(Coordinate(0, 9), Coordinate(5, 9)))
    stripes.append(Stripe(Coordinate(8, 0), Coordinate(0, 8)))
    stripes.append(Stripe(Coordinate(9, 4), Coordinate(3, 4)))
    stripes.append(Stripe(Coordinate(2, 2), Coordinate(2, 1)))
    stripes.append(Stripe(Coordinate(7, 0), Coordinate(7, 4)))
    stripes.append(Stripe(Coordinate(6, 4), Coordinate(2, 0)))
    stripes.append(Stripe(Coordinate(0, 9), Coordinate(2, 9)))
    stripes.append(Stripe(Coordinate(3, 4), Coordinate(1, 4)))
    stripes.append(Stripe(Coordinate(0, 0), Coordinate(8, 8)))
    stripes.append(Stripe(Coordinate(5, 5), Coordinate(8, 2)))
    return stripes


def get_to_draws_from_file():
    text_file = open("coordinates.txt", "r")
    lines = text_file.readlines()
    text_file.close()
    strip_newline_chars(lines)
    return lines


def strip_newline_chars(lines):
    for x in range(len(lines)):
        lines[x] = lines[x].strip()

def get_file_input_as_objects():
    fileInArray = get_to_draws_from_file()
    stripes = []

    for instructionString in fileInArray:
        stringWithoutComma = instructionString.replace(",", " ")

        numbers = []
        for word in stringWithoutComma.split():
            if word.isdigit():
                numbers.append(int(word))
        stripe = Stripe(Coordinate(numbers[0], numbers[1]), Coordinate(numbers[2], numbers[3]))
        stripes.append(stripe)

    return stripes




def draw_line(stripe):
    direction = get_direction(stripe)
    draw_stripe(stripe, direction)


def get_direction(stripe):

    # check if any direction changed
    if stripe.begin.down == stripe.end.down & stripe.begin.right == stripe.end.right:
        return "same"

    # check if horizontal or vertical
    if stripe.begin.down == stripe.end.down:
        return "hor"
    elif stripe.begin.right == stripe.end.right:
        return "ver"
    else:
        return "vertical i think? "

    # prob vertical if both are different


def draw_stripe(stripe, direction):
    if direction == "hor":
        draw_horizontal_stripe(stripe)
        print("in hor exit")
    elif direction == "ver":
        draw_vertical_stripe(stripe)
        print("in ver exit")
    else: # if diag
        draw_diagonal_stripe(stripe)


def draw_diagonal_stripe(stripe):
    sort = determine_stripe_sort(stripe) # e.g. left up to right down
    draw_diagonal_stripe_on_board(stripe, sort)


def draw_diagonal_stripe_on_board(stripe, sort):
    draw_diagonal_line(stripe, sort)


def UpFieldWithOne(down, right):
    print("upf1 down: " + str(down))
    print("upf1 right: " + str(right))
    currentValueOfField = field[down][right]

    if currentValueOfField == ".":
        field[down][right] = "1"
    else:
        currentValueOfFieldAsInt = int(currentValueOfField)
        newValueForField = currentValueOfFieldAsInt + 1
        field[down][right] = newValueForField



def draw_diagonal_line(stripe, sort):
    notAtEndPoint = True

    currentRight = stripe.begin.right
    currentDown = stripe.begin.down

    while notAtEndPoint:
        UpFieldWithOne(currentDown, currentRight)
        if currentDown == stripe.end.down:
            notAtEndPoint = False
        else:
            if sort == "leftup":
                print("leftup")
                currentDown -= 1
                currentRight -= 1
            elif sort == "leftdown":
                print("leftdown")
                currentDown += 1
                currentRight -= 1
            elif sort == "rightup":
                print("rightup")
                currentDown -= 1
                currentRight += 1
            elif sort == "rightdown":
                print("rightdown")
                currentDown += 1
                currentRight += 1
            else:
                print("SOMETHING WENT COMPLETELY WRONG HERE")





def determine_stripe_up_or_down(stripe):
    if stripe.begin.down - stripe.end.down > 0:
        return "up"
    else:
        return "down"


def determine_stripe_sort(stripe):
    stripeVerticalDir = determine_stripe_up_or_down(stripe)

    if  stripe.begin.right - stripe.end.right > 0: # LEFT
        if stripeVerticalDir == "up":
            return "leftup"
        else:
            return "leftdown"
    else: # RIGHT
        if stripeVerticalDir == "up":
            return "rightup"
        else:
            return "rightdown"






def draw_vertical_stripe(stripe):
    if stripe.begin.down < stripe.end.down:
        draw_ver_stripe_generic(stripe, "down")
    else:
        draw_ver_stripe_generic(stripe, "up")


def draw_ver_stripe_generic(stripe, direction):
    notAtEndPoint = True

    currentDown = stripe.begin.down
    currentRight = stripe.begin.right

    while notAtEndPoint:
        UpFieldWithOne(currentDown, currentRight)

        if currentDown == stripe.end.down:
            notAtEndPoint = False
        elif direction == "down":
            currentDown += 1
        elif direction == "up":
            currentDown -= 1
        else:
            print("SOMETHING goes wrong here !")

def draw_horizontal_stripe(stripe):
    if stripe.begin.right < stripe.end.right:
        draw_hor_stripe_generic(stripe, "right")
    else:
        draw_hor_stripe_generic(stripe, "left")


def draw_hor_stripe_generic(stripe, direction):
    notAtEndPoint = True

    currentDown = stripe.begin.down
    currentRight = stripe.begin.right

    while notAtEndPoint:
        UpFieldWithOne(currentDown, currentRight)

        if currentRight == stripe.end.right:
            notAtEndPoint = False
        elif direction == "right":
            currentRight += 1
        elif direction == "left":
            currentRight -= 1
        else:
            print("SOMETHING goes wrong here !")


# draw_diagonal_stripe(Stripe(Coordinate(0, 8), Coordinate(8, 0)))
# draw_diagonal_stripe(Stripe(Coordinate(5, 5), Coordinate(8, 2)))
# draw_diagonal_stripe(Stripe(Coordinate(0, 0), Coordinate(8, 8)))
# draw_diagonal_stripe(Stripe(Coordinate(6, 4), Coordinate(2, 0)))


to_draws = get_file_input_as_objects()


for x in to_draws:
    draw_line(x)

pointsWhereTwoLinesOverlap = 0

for x in range(1000):
    for y in range(1000):
        value = field[x][y]
        if value != ".":
            valueAsInt = int(value)
            if valueAsInt >= 2:
                pointsWhereTwoLinesOverlap += 1

print("overlap: " + str(pointsWhereTwoLinesOverlap))


#print_field(field)