# need to beat 564

with open('input.txt') as f:
    lines = [[int(element) for element in line.split(' ')] for line in f.read().split('\n')[:-1]]

def condition_1(input: list[int]) -> list[bool]:
    inferred_direction = 1 if input[0] < input[1] else -1
    return list(input[idx] < input[idx + 1] if inferred_direction == 1 else input[idx] > input[idx + 1] for idx, _ in enumerate(input[:-1]))

def condition_2(input: list[int]) -> list[bool]:
    return list(1 <= abs(input[idx] - input[idx + 1]) <= 3 for idx, _ in enumerate(input[:-1]))

symptom_poly = list(map(lambda x_tuple: [(x_tuple[0][idx] and x_tuple[1][idx]) for idx, _ in enumerate(x_tuple[0])], [(condition_1(line), condition_2(line)) for line in lines]))

final_number = 0
for idx, sympton in enumerate(symptom_poly):
    if all(sympton):
        final_number += 1
        continue

    for index, _ in enumerate(lines[idx]):
        thing = lines[idx][:index] + lines[idx][index + 1:]
        if all(condition_1(thing)) and all(condition_2(thing)):
            final_number += 1
            break

print(final_number)
