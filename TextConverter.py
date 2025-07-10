import re

def TextToListConverter(PathToTextFile):
    output = []

    file = open(PathToTextFile)
    for line in file:
        if line[0].isdigit():
            match = re.match(r'^(\d+)\s+(.*)\s+\(([^()]+)\)$', line)
            if match:
                quantity = int(match.group(1))
                name = match.group(2).strip()
                code = match.group(3).strip()[:-1]
                output.append([quantity, name, code])
    SortListForDuplicates(output)
    return output

def SortListForDuplicates(card_list):
    list_copy = card_list[:]
    sorted_card_list = []
    index = 0

    #loop through card list
    for card in card_list:
        if card[0] == 0:
            list_copy[index] = [0, 0, 0, 0]
            index += 1
            continue
        else:
            list_copy[index] = [0, 0, 0, 0]

        #loop through compare list
        for item in list_copy:
            if card[2] == item[2]:
                card[0] += item[0]
                item[0] = 0
        sorted_card_list.append(card)
        index += 1
    return sorted_card_list