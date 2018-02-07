def get_data(filename):
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "") for element in lines]

    data = []
    for element in table:
        data = list(element)

    return data


def captcha(data):
    suma = 0
    for i in range(len(data)):
        if data[i] == data[(i+1)%len(data)]:
            suma = suma + int(data[i])

    return suma


print(captcha(get_data("day1.txt")))
