with open('input.txt') as f:
    grid = [[element for element in line.strip()] for line in f.readlines()]

def find_caret():
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '^':
                return (r, c)

c_r, c_c = find_caret()

def next_thing():
    global c_r, c_c
    direction_y = 0
    direction_x = 0
    match grid[c_r][c_c]:
        case '^':
            direction_y = -1
        case 'v':
            direction_y = 1
        case '<':
            direction_x = -1
        case '>':
            direction_x = 1

    if grid[c_r + direction_y][c_c + direction_x] == '#':
        match grid[c_r][c_c]:
            case '^':
                grid[c_r][c_c] = '>'
            case 'v':
                grid[c_r][c_c] = '<'
            case '<':
                grid[c_r][c_c] = '^'
            case '>':
                grid[c_r][c_c] = 'v'
    else:
        caret = grid[c_r][c_c]
        grid[c_r][c_c] = ''
        c_c += direction_x
        c_r += direction_y
        grid[c_r][c_c] = caret

    if c_r > len(grid) and c_r < 0:
        raise RuntimeError()

    if c_c > len(grid[0]) and c_c < 0:
        raise RuntimeError()

def count_empty():
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '':
                counter += 1
    return counter

try:
    while True:
        next_thing()
except:
    pass

# print('\n'.join(str(line) for line in grid))
print(count_empty() + 1)
