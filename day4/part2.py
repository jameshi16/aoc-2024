with open('input.txt') as f:
    grid = [line[:-1] for line in f.readlines()]

counter = 0

def get_possibilities(r: int, c: int):
    # diagonals
    possibilities = []
    possibilities.append(''.join([grid[r + i - 1][c + i - 1] for i in range(3)]))
    possibilities.append(''.join([grid[r + i - 1][c - i + 1] for i in range(3)]))

    return possibilities

accum = 0
for r, line in enumerate(grid):
    if r == 0 or r == len(grid) - 1:
        continue
    for c in range(len(line)):
        if c == 0 or c == len(line) - 1:
            continue

        if grid[r][c] != 'A':
            continue

        possibilties = [ps for ps in get_possibilities(r, c) if ps == 'MAS' or ps == 'SAM']
        if len(possibilties) < 2:
            continue
        accum += 1

print(accum)
