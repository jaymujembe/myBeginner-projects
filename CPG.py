grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = 0
y = 0

while True:


    for i in grid[x][y]:

        print(i, end='')

    x += 1
    if x == 9:
        print('')
        break

x = 0
y = 1
while True:
    for a in grid[x][y]:
        print(a, end='')

    x += 1
    if x == 9:
        print('')
        break

x = 0
y = 2
while True:
    for s in grid[x][y]:
        print(s, end='')

    x += 1
    if x == 9:
        print('')
        break


x = 0
y = 3
while True:
    for d in grid[x][y]:
        print(d, end='')

    x += 1
    if x == 9:
        print('')
        break

x = 0
y = 4
while True:
    for f in grid[x][y]:
        print(f, end='')

    x += 1
    if x == 9:
        print('')
        break

x = 0
y = 5
while True:
    for g in grid[x][y]:
        print(g, end='')

    x += 1
    if x == 9:
        #print('')
        break
