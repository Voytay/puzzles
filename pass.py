
#Get file with passes and convert into table.
def get_input(filename):
    table = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    table = [element.replace("\n","") for element in lines]
    return table


def count_word(table):
    count = 0
    valid = 0
    data = []
    for element in table:
        data.append(element.split())
    for line in data:
        x = 0
        for word in line:
            test = line[x]
            if word == test:
                count += 1
        if count < 2:
            valid += 1
                
    print(valid)



count_word(get_input('passes.txt'))