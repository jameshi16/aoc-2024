import itertools

def parse(line):
    objective, inputs = line.split(':')
    inputs = inputs.strip().split(' ')
    return (int(objective), [int(input) for input in inputs])

def eval_prime(l, operation, r):
    if operation == '+':
        return l + r
    elif operation == '*':
        return l * r
    elif operation == '|':
        return int(str(l) + str(r))
    raise RuntimeError()

def manual_evaluation(expr, maximum_num):
    accum = 0
    operation = ''
    operand = ''
    first = True
    for idx, c in enumerate(expr):
        if accum > maximum_num:
            return maximum_num + 1

        if c != '+' and c != '*' and c != '|':
            operand += c
            continue

        if first:
            accum = int(operand)
            operand = ''
            first = False
            operation = c
            continue

        accum = eval_prime(accum, operation, int(operand.lstrip('0')))
        operand = ''
        operation = c

    accum = eval_prime(accum, operation, int(operand.lstrip('0')))
    return accum

def do_line_1(thing) -> bool:
    objective, input = thing
    for possibilities in itertools.product('+*', repeat=(len(input) - 1)):
        expr = ''.join(list(f'{t[0]}{t[1]}' for t in zip(input, possibilities))) + str(input[-1])
        if objective == manual_evaluation(expr, objective):
            return False
    return True

def do_line_2(thing) -> bool:
    objective, input = thing
    for possibilities in itertools.product('+*|', repeat=(len(input) - 1)):
        expr = ''.join(list(f'{t[0]}{t[1]}' for t in zip(input, possibilities))) + str(input[-1])
        if objective == manual_evaluation(expr, objective):
            return True
    return False

def counter_line_2(things):
    size = len(things)
    accum = []
    for idx, t in enumerate(filter(do_line_2, things)):
        print(f'progress: {idx + 1}/{size}')
        accum.append(t[0])
    return sum(accum)

with open('input.txt') as f:
    exprs = [parse(line) for line in f.readlines()]

# print(do_line(exprs[3]))
previous_answer = 5837374519342
filtered_first = list(filter(do_line_1, exprs))
print('length to check', len(filtered_first))
print(previous_answer + counter_line_2(filtered_first))
# print(previous_answer + sum(list(map(lambda x: x[0], filter(do_line_2, filtered_first)))))
