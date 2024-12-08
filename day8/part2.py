from collections import defaultdict
import itertools

bucket = defaultdict(list)

with open('input.txt') as f:
    grid = [[element for element in line.strip()] for line in f.readlines()]

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != '.':
            bucket[grid[r][c]].append((r, c))

bucket = dict(bucket)
already_covered = set(itertools.chain.from_iterable([v for v in bucket.values()]))
antis = set()

def taxi_cab(x1, y1, x2, y2):
    return (x1 - x2, y1 - y2)

def is_in_bound(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def print_grid():
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (r, c) in already_covered:
                print('?', end='')
            elif (r, c) in antis:
                print('#', end='')
            else: print('.', end='')
        print()

for (key, coords) in bucket.items():
    for ((r1, c1), (r2, c2)) in itertools.product(coords, repeat=2):
        dr, dc = taxi_cab(r1, c1, r2, c2)
        thing = []
        for k in range(1, len(grid)):
            thing.extend([(r1 + k * dr, c1 + k * dc), (r2 + k * dr, c2 + k * dc),
                          (r1 - k * dr, c1 - k * dc), (r2 - k * dr, c2 - k * dc)])
        possibilities = filter(lambda x: ((r1 != x[0] or c1 != x[1]) and (r2 != x[0] or c2 != x[1])) and (x[0], x[1]) not in antis and is_in_bound(x[0], x[1]), thing)
        antis.update(possibilities)

print(len(antis.union(already_covered)))
# print_grid()
