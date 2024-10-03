import random

morning_students = []
afternoon_students = []
previous_groups = set()
current_groups = []


def parse_previous_groups():
    read_file = open("previous_groups.txt", "r")
    for line in read_file:
        line = line[:-1]
        split_line = frozenset(line.split(", "))
        previous_groups.add(split_line)


def populate_lists(file):
    morning = True
    for line in file:
        line = line[:-1]
        if line == "# Morning":
            continue
        elif line == "# Afternoon":
            morning = False
        else:
            if morning:
                morning_students.append(line)
            else:
                afternoon_students.append(line)


def set_to_string(group):
    str_group = ""
    for name in group:
        str_group += name + ", "
    return str_group[:-2] + "\n"


def select_random(lst):
    index0 = random.randrange(0, len(lst))
    index1 = random.randrange(0, len(lst))
    index2 = random.randrange(0, len(lst))
    while index0 == index1:
        index1 = random.randrange(0, len(lst))
    while index0 == index2 or index1 == index2:
        index2 = random.randrange(0, len(lst))
    return lst[index0], lst[index1], lst[index2]


def select_group(lst, count):
    first, second, third = select_random(lst)
    group = frozenset({first, second, third})
    if group in previous_groups:
        if count < 20:
            return select_group(lst, count+1)
    lst.remove(first)
    lst.remove(second)
    lst.remove(third)
    return set_to_string(group)


def read_current_groups(file):
    for line in file:
        if line == "Morning Lab\n" or line == "Afternoon Lab\n" or line == "\n":
            continue
        else:
            current_groups.append(line)


def update_previous_groups():
    read_file = open("lab_groups.txt", "r")
    read_current_groups(read_file)
    read_file.close()

    write_file = open("previous_groups.txt", "a")
    for group in current_groups:
        write_file.write(group)
    write_file.close()



def main():
    parse_previous_groups()
    read_file = open("student_list.txt", "r")
    populate_lists(read_file)
    read_file.close()

    write_file = open("lab_groups.txt", "w")
    write_file.write("Morning Lab\n")
    if len(morning_students) % 3 == 0:
        while len(morning_students) > 0:
            write_file.write(select_group(morning_students, 0))
    elif len(morning_students) % 3 == 1:
        while len(morning_students) > 4:
            write_file.write(select_group(morning_students, 0))
        write_file.write(morning_students[0] + ", " + morning_students[1] + "\n")
        write_file.write(morning_students[2] + ", " + morning_students[3] + "\n")
    elif len(morning_students) % 3 == 2:
        while len(morning_students) > 2:
            write_file.write(select_group(morning_students, 0))
        write_file.write(morning_students[0] + ", " + morning_students[1] + "\n")

    write_file.write("\nAfternoon Lab\n")
    if len(afternoon_students) % 3 == 0:
        while len(afternoon_students) > 0:
            write_file.write(select_group(afternoon_students, 0))
    elif len(afternoon_students) % 3 == 1:
        while len(afternoon_students) > 4:
            write_file.write(select_group(afternoon_students, 0))
        write_file.write(afternoon_students[0] + ", " + afternoon_students[1] + "\n")
        write_file.write(afternoon_students[2] + ", " + afternoon_students[3] + "\n")
    elif len(afternoon_students) % 3 == 2:
        while len(afternoon_students) > 2:
            write_file.write(select_group(afternoon_students, 0))
        write_file.write(afternoon_students[0] + ", " + afternoon_students[1] + "\n")
    write_file.close()
    update_previous_groups()

if __name__ == "__main__":
    main()
