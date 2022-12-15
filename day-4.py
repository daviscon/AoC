def part_one():
    total = 0
    file = open("input-4.txt", "r")

    #5-7, 4-8
    #if 5>4 & 7<8
    for row in file:
        sections = row.split(',')
        first = sections[0].split('-')
        second = sections[1].split('-')
        if first[0] >= second[0] and second[1] <= first[1]:
            total = total + 1
        elif first[0] >= second[0] and first[1] <= second[1]:
            total = total + 1

    print(total)
    file.close()

def part_two():
    total = 0
    file = open("input-4.txt", "r")

    for row in file:
        row = row
    print(total)
    file.close()

print('Part 1:')
part_one()
print('Part 2:')
part_two()