with open('input.txt') as f:
    grid = [[int(element) for element in line[:-1]] for line in f.readlines()]

accum = 0

def explore(r, c, value):
    if r < 0 or r >= len(grid):
        return set()
    if c < 0 or c >= len(grid[r]):
        return set()

    if value == 9 and grid[r][c] == 9:
        return {(r, c)}

    results = set()
    if grid[r][c] == value:
        results |= explore(r - 1, c, value + 1)
        results |= explore(r + 1, c, value + 1)
        results |= explore(r, c - 1, value + 1)
        results |= explore(r, c + 1, value + 1)

    return results

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 0:
            accum += len(explore(r, c, 0))

print(accum)
