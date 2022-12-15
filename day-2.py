
# Rock = A Paper = B Scissors = C
# Rock = X Paper = Y Scissors = Z
# Rock = 1 Paper = 2 Scissors = 3
# Rock > Scissors Paper > Rock Scissors > Paper

def part_one():
    total = 0

    points = {'X': 1, 'Y': 2, 'Z': 3}
    win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}

    file = open("input-2.txt", "r")

    for row in file:
        guess = row[0]
        play = row[2]
        total = total + points[play]
        if(guess == win[play]):
            total = total + 6
        elif(guess == draw[play]):
            total = total + 3
    print(total)
    file.close()

# Rock = A Paper = B Scissors = C
# Rock = X Paper = Y Scissors = Z
# Rock = 1 Paper = 2 Scissors = 3
# Rock > Scissors Paper > Rock Scissors > Paper

def part_two():
    total = 0
    points = {
        'X': {
            'A': 3,
            'B': 1,
            'C': 2
            },
        'Y': {
            'A': 1,
            'B': 2,
            'C': 3
        },
        'Z': {
            'A': 2,
            'B': 3,
            'C': 1
        }
    }

    file = open("input-2.txt", "r")

    for row in file:
        guess = row[0]
        play = row[2]
         
        if(play == 'Z'):
            total = total + 6
        elif(play == 'Y'):
            total = total + 3
        
        total = total + points[play][guess]
    print(total)
    file.close()


print('Part 1:')
part_one()
print('Part 2:')
part_two()

