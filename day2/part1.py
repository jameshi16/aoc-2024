with open('input.txt') as f:
    lines = [[int(element) for element in line.split(' ')] for line in f.read().split('\n')[:-1]]

def condition_1(input: list[int]):
    inferred_direction = 1 if input[0] < input[1] else -1
    return all(input[idx] < input[idx + 1] if inferred_direction == 1 else input[idx] > input[idx + 1] for idx, _ in enumerate(input[:-1]))

def condition_2(input: list[int]):
    return all(1 <= abs(input[idx] - input[idx + 1]) <= 3 for idx, _ in enumerate(input[:-1]))

# print('\n'.join(' '.join([str(element) for element in line]) for line in filter(lambda x: condition_1(x) and condition_2(x), lines)))
print(sum(1 if condition_1(line) and condition_2(line) else 0 for line in lines))
