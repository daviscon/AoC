

def get_calorie_array():
    max = 0
    calories = 0

    array = []

    file = open("input-1.txt", "r")

    for row in file:
        if row == '\n':
            array.append(calories)
            calories = 0
        else:
            if row[-1] == '\n':
                calories = calories + int(row[:-1])
            else:
                calories = calories + int(row)
        if calories > max:
            max = calories
            
    file.close()
    return sorted(array)
    

array = get_calorie_array()

print("Part 1:")
print(array[-1])

print("Part 2:")
total = array[-1] + array[-2] + array[-3]
print(total)