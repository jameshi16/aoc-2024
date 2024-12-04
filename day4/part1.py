with open('input.txt') as f:
    grid = [line[:-1] for line in f.readlines()]

counter = 0

def get_possibilities(r: int, c: int):
    # horizontal
    possibilities = []
    if c + 3 < len(grid[r]):
        possibilities.append(''.join([grid[r][c + i] for i in range(4)]))
    if c - 3 >= 0:
        possibilities.append(''.join([grid[r][c - i] for i in range(4)]))

    # verticals
    if r + 3 < len(grid):
        possibilities.append(''.join([grid[r + i][c] for i in range(4)]))
    if r - 3 >= 0:
        possibilities.append(''.join([grid[r - i][c] for i in range(4)]))

    # diagonals
    if r + 3 < len(grid) and c + 3 < len(grid[r]):
        possibilities.append(''.join([grid[r + i][c + i] for i in range(4)]))
    if r - 3 >= 0 and c + 3 < len(grid[r]):
        possibilities.append(''.join([grid[r - i][c + i] for i in range(4)]))
    if r - 3 >= 0 and c - 3 >= 0:
        possibilities.append(''.join([grid[r - i][c - i] for i in range(4)]))
    if r + 3 < len(grid) and c - 3 >= 0:
        possibilities.append(''.join([grid[r + i][c - i] for i in range(4)]))

    return possibilities

accum = 0
for r, line in enumerate(grid):
    for c in range(len(line)):
        ps = get_possibilities(r, c)
        accum += sum(1 for ps in get_possibilities(r, c) if ps == 'XMAS')

print(accum)
