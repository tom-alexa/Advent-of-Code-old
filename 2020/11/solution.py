import time
from pathlib import PurePath

# --- Day 11: Seating System ---


###############
#  constants  #
###############

YEAR = 2020
DAY = 11

INPUT_FILE = PurePath(f"{YEAR:04}/{DAY:02}/input")

ESTIMATED_TIME = "4 sec"

TO_BE_EMPTY = {"empty": 0, "occupied": {1: 3, 2: 4}}


###########
#  input  #
###########

def get_data_from_input():
    with open(INPUT_FILE, "r") as file:
        return [ line.strip() for line in file.readlines() ]


###############
#  functions  #
###############

def check_seat_one(row, column, layout):
    letter = layout[row][column]
    if letter == ".":
        return letter
    rows_to_check = range(max(0, row - 1), min(len(layout) - 1, row + 1) + 1)
    columns_to_check = range(max(0, column - 1), min(len(layout[0]) - 1, column + 1) + 1)
    count_to_empty = TO_BE_EMPTY["occupied"][1] if letter == "#" else TO_BE_EMPTY["empty"]
    occupied_seats = 0
    for row_to_check in rows_to_check:
        for column_to_check in columns_to_check:
            if row_to_check == row and column_to_check == column:
                continue
            if layout[row_to_check][column_to_check] == "#":
                occupied_seats += 1
                if occupied_seats > count_to_empty:
                    return "L"
    return "#"


def check_seat_two(row, column, layout):
    letter = layout[row][column]
    if letter == ".":
        return letter
    occupied_seats = 0
    occupied_seats += check_direction(1, -1, row, column, layout)
    occupied_seats += check_direction(1, 0, row, column, layout)
    occupied_seats += check_direction(1, 1, row, column, layout)
    occupied_seats += check_direction(0, 1, row, column, layout)
    occupied_seats += check_direction(-1, 1, row, column, layout)
    occupied_seats += check_direction(-1, 0, row, column, layout)
    occupied_seats += check_direction(-1, -1, row, column, layout)
    occupied_seats += check_direction(0, -1, row, column, layout)

    count_to_empty = TO_BE_EMPTY["occupied"][2] if letter == "#" else TO_BE_EMPTY["empty"]
    if occupied_seats > count_to_empty:
        return "L"
    return "#"


def check_direction(plus_x, plus_y, row, column, layout):
    y, x = row, column
    while True:
        x += plus_x
        y += plus_y
        if x < 0 or x > len(layout[0]) - 1 or y < 0 or y > len(layout) - 1:
            return 0
        if layout[y][x] == "#":
            return 1
        elif layout[y][x] == "L":
            return 0


def get_occupied_seats(part, seat_layout):
    new_layout = seat_layout[:]
    while True:
        to_modify = []
        occupied_seats = 0
        for row in range(len(seat_layout)):
            row_to_add = ""
            for column in range(len(seat_layout[0])):
                if part == 1:
                    letter_to_add = check_seat_one(row, column, new_layout)
                else:
                    letter_to_add = check_seat_two(row, column, new_layout)
                row_to_add += letter_to_add
                if letter_to_add == "#":
                    occupied_seats += 1
            to_modify.append(row_to_add)
        if to_modify == new_layout:
            break
        new_layout = to_modify[:]
    return occupied_seats


#############
#  answers  #
#############

def get_answer_1(seat_layout):
    time_start = time.perf_counter()
    occupied_seats = get_occupied_seats(1, seat_layout)
    time_spent = time.perf_counter() - time_start
    return {"value": occupied_seats, "time": time_spent}


def get_answer_2(seat_layout):
    time_start = time.perf_counter()
    occupied_seats = get_occupied_seats(2, seat_layout)
    time_spent = time.perf_counter() - time_start
    return {"value": occupied_seats, "time": time_spent}


###########
#  print  #
###########

def print_estimated_time():
    indetation = " " * 2
    print(f"\n{indetation*3}Estimated time: {ESTIMATED_TIME}")


def print_answers(answer_1, answer_2):
    answer_1_value = answer_1["value"]
    answer_2_value = answer_2["value"]
    answer_1_time = round(answer_1["time"], 3)
    answer_2_time = round(answer_2["time"], 3)

    to_add = abs(len(str(answer_1_value)) - len(str(answer_2_value)))
    lenght_to_add_1 = " " * to_add if len(str(answer_1_value)) < len(str(answer_2_value)) else " " * 0
    lenght_to_add_2 = " " * to_add if len(str(answer_1_value)) > len(str(answer_2_value)) else " " * 0

    indetation = " " * 2
    print(f"\n{indetation}{YEAR} > {DAY}")
    print(f"{indetation*2}Answer 1: {answer_1_value}{lenght_to_add_1} | {answer_1_time:.3f} sec")
    print(f"{indetation*2}Answer 2: {answer_2_value}{lenght_to_add_2} | {answer_2_time:.3f} sec\n")


##########
#  main  #
##########

def main():
    print_estimated_time()
    puzzle_input = get_data_from_input()
    answer_1 = get_answer_1(puzzle_input)
    answer_2 = get_answer_2(puzzle_input)
    print_answers(answer_1, answer_2)


if __name__ == "__main__":
    main()