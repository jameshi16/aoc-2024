with open('example.txt') as f:
    lines = [[int(element) for element in line.split(' ')] for line in f.read().split('\n')[:-1]]

def condition_1(input: list[int]) -> list[bool]:
    inferred_direction = 1 if input[0] < input[1] and input[1] < input[2] and input[2] < input[3] else -1
    return list(input[idx] < input[idx + 1] if inferred_direction == 1 else input[idx] > input[idx + 1] for idx, _ in enumerate(input[:-1]))

def condition_2(input: list[int]) -> list[bool]:
    return list(1 <= abs(input[idx] - input[idx + 1]) <= 3 for idx, _ in enumerate(input[:-1]))

# checking for which 2 elements are responsible for an unsafe
symptom_poly = list(map(lambda x_tuple: [(x_tuple[0][idx] and x_tuple[1][idx]) for idx, _ in enumerate(x_tuple[0])], [(condition_1(line), condition_2(line)) for line in lines]))

final_number = 0
for idx, sympton in enumerate(symptom_poly):
    if all(sympton):
        final_number += 1
        continue

    if all([not x for x in sympton]):
        continue

    most_significant_sym = sum(sympton) <= len(sympton) / 2
    try:
        index = sympton.index(most_significant_sym)
    except:
        continue

    # try removing left
    try_line_1 = lines[idx][:index] + lines[idx][index + 1:]
    try_line_2 = lines[idx][:index + 1] + lines[idx][index + 2:]

    if any(all(condition_1(try_line)) and all(condition_2(try_line)) for try_line in [try_line_1, try_line_2]):
        final_number += 1

print(final_number)
