from array import array
from dataclasses import dataclass


bingoNumbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

bingoBoards = 0


def read_input_file(fileName):
    text_file = open(fileName, "r")
    lines = text_file.readlines()
    text_file.close()
    values = strip_newline_chars_and_empty(lines)
    return values


def strip_newline_chars_and_empty(lines):
    numbers = []
    for x in range(len(lines)):
        lines[x] = lines[x].strip()
        if lines[x] != "":
            numbers.append(lines[x])
    return numbers


def create_bingo_line_from_five_numbers_in_string(numbersInString):
    bingoLine = [int(s) for s in numbersInString.split() if s.isdigit()]
    return bingoLine


def create_all_bingo_lines(inputLines):
    bingoLines = []
    for x in range(len(inputLines)):
        bingoLines.append(create_bingo_line_from_five_numbers_in_string(inputLines[x]))
    return bingoLines


def create_bingo_boards_from_lines(inputLines):
    allBoards = []

    bingoLines = create_all_bingo_lines(inputLines)
    linesForNewBoard = []
    countId = 1
    for x in range(len(bingoLines)):
        linesForNewBoard.append(bingoLines[x])
        if len(linesForNewBoard) == 5:
            boardToAdd = BingoBoard(linesForNewBoard, 0, countId)
            countId += 1
            allBoards.append(boardToAdd)
            linesForNewBoard = []
    return allBoards


def pull_number(number, boards):
    for board in boards:
        for x in range(5):
            for y in range(5):
                if board.lines[x][y] == number:
                    board.lines[x][y] = 100
    return boards


def check_horizontal_bingo(boards):
    checkMark = 100
    for board in boards:
        for line in board.lines:
            numberOfChecks = 0
            for number in range(5):
                if line[number] == checkMark:
                    numberOfChecks += 1
            if numberOfChecks == 5:
                board.winningNumber = 200
                return board
            numberOfChecks = 0
    return BingoBoard([], 101)


def check_vertical_bingo(boards):
    checkMark = 100
    for board in boards:
        for x in range(5):
            numberOfChecks = 0
            for y in range(5):
                if board.lines[y][x] == 100:
                    numberOfChecks += 1
            if numberOfChecks == 5:
                board.winningNumber = 200
                return board
    return BingoBoard([], 101)


def ChooseBoard():
    global winning_number
    winning_number = 0
    boards = create_bingo_boards_from_lines(read_input_file("bingoBoards1.txt"))
    bingoBalls = get_bingo_balls()

    for number in bingoBalls:
        boards = pull_number(number, boards)

        verticalBingoBoard = check_vertical_bingo(boards)
        if verticalBingoBoard.winningNumber == 200:
            winning_number = number
            return verticalBingoBoard

        horizontalBingo = check_horizontal_bingo(boards)
        if horizontalBingo.winningNumber == 200:
            winning_number = number
            return horizontalBingo
    return None


def get_bingo_balls():
    text_file = open("bingoNumbers1.txt", "r")
    lines = text_file.readlines()
    text_file.close()
    values = strip_newline_chars_and_empty(lines)[0]
    values = values.split(",")
    integer_map = map(int, values)
    integer_list = list(integer_map)
    return integer_list


def Challenge1():
    winningBoard = ChooseBoard()
    print(winningBoard)
    print("number when bingo: " + str(winning_number))
    print("Total score of board: " + str(calculate_score_winning_board(winningBoard, winning_number)))


def calculate_score_winning_board(winningBoard, winningNumber):
    totalPoints = 0
    for x in range(5):
        for y in range(5):
            if winningBoard.lines[x][y] != 100:
                totalPoints += winningBoard.lines[x][y]
    return totalPoints * winningNumber



@dataclass
class BingoBoard:
    lines: []
    winningNumber: int
    boardId: int




def go_through_boards():
    boards = create_bingo_boards_from_lines(read_input_file("bingoBoards1.txt"))
    bingoBalls = get_bingo_balls()

    for number in bingoBalls:
        boards = pull_number(number, boards)

        verticalBingoBoard = check_vertical_bingo(boards)
        if verticalBingoBoard.winningNumber == 200:
            winning_number = number
            return verticalBingoBoard

        horizontalBingo = check_horizontal_bingo(boards)
        if horizontalBingo.winningNumber == 200:
            winning_number = number
            return horizontalBingo
    return None



def remove_boards_with_bingo(boards):
    global winningNumber2
    bingoBoards = boards
    bingoBalls = get_bingo_balls()
    for x in range(90):
        print("start ball grab")
        pull_number(bingoBalls[x], bingoBoards)

        bingoBoards = get_boards_to_remove_vertical(bingoBoards)
        bingoBoards = get_boards_to_remove_horizontal(bingoBoards)

        for board in bingoBoards:
            if board.winningNumber == 200:
                if len(bingoBoards) == 1:
                    winningNumber2 = bingoBalls[x]
                    return bingoBoards[0]
                else:
                    bingoBoards.remove(board)


def Challenge2():
    boards = create_bingo_boards_from_lines(read_input_file("bingoBoards1.txt"))
    singleBoard = remove_boards_with_bingo(boards)
    print(winningNumber2)
    print(singleBoard)
    print("The final calculation is: " + str(calculate_score_winning_board(singleBoard, winningNumber2)))



def get_boards_to_remove_horizontal(boards):
    for board in boards:
        for x in range(5):
            numberOfChecks = 0
            for y in range(5):
                if board.lines[x][y] == 100:
                    numberOfChecks += 1
            if numberOfChecks == 5:
                board.winningNumber = 200
    return boards


def get_boards_to_remove_vertical(boards):
    for board in boards:
        for x in range(5):
            numberOfChecks = 0
            for y in range(5):
                if board.lines[y][x] == 100:
                    numberOfChecks += 1
            if numberOfChecks == 5:
                board.winningNumber = 200
    return boards


#Challenge1()
Challenge2()

