import random

morning_students = []
afternoon_students = []
evening_students = []
previous_pairs = set()
current_pairs = []


def parse_previous_pairs():
    read_file = open("previous_pairs.txt", "r")
    for line in read_file:
        line = line[:-1]
        split_line = frozenset(line.split(", "))
        previous_pairs.add(split_line)


def populate_lists(file):
    morning = True
    afternoon = False
    evening = False
    for line in file:
        line = line[:-1]
        if line == "# Morning":
            afternoon = False
            evening = False
            morning = True
        elif line == "# Afternoon":
            morning = False
            evening = False
            afternoon = True
        elif line == "# Evening":
            morning = False
            afternoon = False
            evening = True
        else:
            if morning:
                morning_students.append(line)
            elif afternoon:
                afternoon_students.append(line)
            elif evening:
                evening_students.append(line)


def set_to_string(pair):
    str_pair = ""
    for name in pair:
        str_pair += name + ", "
    return str_pair[:-2] + "\n"


def select_random(lst):
    index0 = random.randrange(0, len(lst))
    index1 = random.randrange(0, len(lst))
    while index0 == index1:
        index1 = random.randrange(0, len(lst))
    return lst[index0], lst[index1]


def select_pair(lst, count):
    first, second = select_random(lst)
    pair = frozenset({first, second})
    if pair in previous_pairs:
        if count < 20:
            return select_pair(lst, count+1)
    lst.remove(first)
    lst.remove(second)
    return set_to_string(pair)


def read_current_pairs(file):
    for line in file:
        if line == "Morning Lab\n" or line == "Afternoon Lab\n" or line == "Evening Lab\n" or line == "\n":
            continue
        else:
            current_pairs.append(line)


def update_previous_pairs():
    read_file = open("lab_pairs.txt", "r")
    read_current_pairs(read_file)
    read_file.close()

    write_file = open("previous_pairs.txt", "a")
    for pair in current_pairs:
        write_file.write(pair)
    write_file.close()


def main():
    parse_previous_pairs()
    read_file = open("student_list.txt", "r")
    populate_lists(read_file)
    read_file.close()

    write_file = open("lab_pairs.txt", "w")
    write_file.write("Morning Lab\n")
    if len(morning_students) % 2 == 0:
        while len(morning_students) > 0:
            write_file.write(select_pair(morning_students, 0))
    else:
        while len(morning_students) > 3:
            write_file.write(select_pair(morning_students, 0))
        write_file.write(
            morning_students[0] + ", " + morning_students[1] + ", " + morning_students[2] + "\n")

    write_file.write("\nAfternoon Lab\n")
    if len(afternoon_students) % 2 == 0:
        while len(afternoon_students) > 0:
            write_file.write(select_pair(afternoon_students, 0))
    else:
        while len(afternoon_students) > 3:
            write_file.write(select_pair(afternoon_students, 0))
        write_file.write(
            afternoon_students[0] + ", " + afternoon_students[1] + ", " + afternoon_students[2] + "\n")
    
    write_file.write("\nEvening Lab\n")
    if len(evening_students) % 2 == 0:
        while len(evening_students) > 0:
            write_file.write(select_pair(evening_students, 0))
    else:
        while len(afternoon_students) > 3:
            write_file.write(select_pair(evening_students, 0))
        write_file.write(
            evening_students[0] + ", " + evening_students[1] + ", " + evening_students[2] + "\n")

    write_file.close()
    update_previous_pairs()

if __name__ == "__main__":
    main()
