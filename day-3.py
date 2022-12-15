

def part_one():
    total = 0
    file = open("input-3.txt", "r")

    for row in file:
        first = list(row[:len(row)//2])
        second = list(row[len(row)//2:])

        for i in first:
            if i in second:
                ascii = ord(i)
                total = total + ascii
                if (ascii < 95): 
                    total = total - 38
                else:
                    total = total - 96
                break
    print(total)
    file.close()

def part_two():
    total = 0
    array = []
    file = open("input-3.txt", "r")

    for row in file:
        array.append(row)
        if len(array) == 3:
            print(len(array))
            for i in list(array[0]):
                if i in array[1]:
                     if i in array[2]:
                        ascii = ord(i)
                        total = total + ascii
                        if (ascii < 95): 
                            total = total - 38
                        else:
                            total = total - 96
                        break
            array = []
    print(total)
    file.close()

print('Part 1:')
part_one()
print('Part 2:')
part_two()