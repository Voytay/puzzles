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
    unique = []
    not_anagrams = []
    for element in table:
        data.append(element.split())

    for line in data:
        for element in line:
            if element not in unique:
                unique.append(element)
            else:
                count += 1

        for word in unique:
            if sorted(word) not in not_anagrams:
                not_anagrams.append(sorted(word))
            else:
                count += 1

        not_anagrams= []
        unique = []

        if count == 0:
            valid += 1
        count = 0

    print(valid)

count_word(get_input('passes.txt'))