from dataclasses import dataclass


@dataclass
class LanternFish:
    nOfDaysUntilNewLanternFish: int
    justBorn: bool


def cycle_day(fishesToCycle):
    currentFishes = []
    for fish in fishesToCycle:
        if fish.nOfDaysUntilNewLanternFish > 0:
            fish.nOfDaysUntilNewLanternFish -= 1
            currentFishes.append(fish)
        elif fish.nOfDaysUntilNewLanternFish == 0:
            fish.nOfDaysUntilNewLanternFish = 6
            currentFishes.append(fish)
            currentFishes.append(LanternFish(8, False))
    return currentFishes

        # elke 6 een nieuwe fish - een net geboren vis +2 dagen

def strip_newline_chars_and_empty(lines):
    numbers = []
    for x in range(len(lines)):
        lines[x] = lines[x].strip()
        if lines[x] != "":
            numbers.append(lines[x])
    return numbers


def read_fish_file():
    text_file = open("fishes.txt", "r")
    lines = text_file.readlines()
    text_file.close()
    values = strip_newline_chars_and_empty(lines)[0]
    values = values.split(",")
    integer_map = map(int, values)
    integer_list = list(integer_map)
    return integer_list

def get_fishes_from_file():
    fishArray = read_fish_file()

    fishesToReturn = []

    for number in fishArray:
        fishesToReturn.append(LanternFish(number, False))
    return fishesToReturn


fishes = get_fishes_from_file()

# fishes = []
# fishes.append(LanternFish(3, False))
# fishes.append(LanternFish(4, False))
# fishes.append(LanternFish(3, False))
# fishes.append(LanternFish(1, False))
# fishes.append(LanternFish(2, False))

days = 80

for day in range(days):
    tempFishes = (cycle_day(fishes))
    fishes = tempFishes

print("Total n of fish: " + str(len(fishes)))

