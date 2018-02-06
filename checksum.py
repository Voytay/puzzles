def get_numbers(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split("\t") for element in lines]
    return table


def line_calc(table):
    max_num = 0
    min_num = 100000
    check = 0
    for element in table:
        for word in element:
            if int(word) > max_num:
                max_num = int(word)
            elif int(word) < min_num:
                min_num = int(word)
        print(min_num, max_num)
        diffrence = max_num - min_num
        check = check + diffrence
        diffrence = 0
        max_num = 0
        min_num = 100000

    print(check)


def division_calc(table):
    check = 0
    for element in table:
        for word in element:
            diviser = int(word)
            for i in range (1, len(element)):
                if int(element[i]) % diviser == 0 and int(element[i]) / diviser != 1:
                    check = check + (int(element[i]) / diviser)
    print(check)


line_calc(get_numbers("numbers.txt"))

division_calc(get_numbers("numbers.txt"))