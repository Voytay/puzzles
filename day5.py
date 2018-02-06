def get_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    table = [int(element.replace("\n", "")) for element in lines]
    return table


def calculate(table):
    i = 0
    a = 0
    while i < len(table) and i >= 0:
        x = table[i]
        if x >= 3 and x == 0:
            table[i] -= 1
        else:
            table[i] += 1
        i += x
        a += 1
    print(a)


calculate(get_data("data5.txt"))