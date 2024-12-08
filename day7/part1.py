import itertools

def parse(line):
    objective, inputs = line.split(':')
    inputs = inputs.strip().split(' ')
    return (int(objective), [int(input) for input in inputs])

def manual_evaluation(expr):
    accum = 0
    operation = ''
    operand = ''
    first = True
    for c in expr:
        if c != '+' and c != '*':
            operand += c
            continue

        if first:
            accum = int(operand)
            operand = ''
            operation = c
            first = False
            continue

        accum = eval(f'{accum}{c}{operand}')
        operand = ''

    accum = eval(f'{accum}{operation}{operand}')
    return accum

def do_line(thing) -> bool:
    objective, input = thing
    for possibilities in itertools.product('+*', repeat=(len(input) - 1)):
        expr = ''.join(list(f'{t[0]}{t[1]}' for t in zip(input, possibilities))) + str(input[-1])
        if objective == manual_evaluation(expr):
            return True
    return False

with open('input.txt') as f:
    exprs = [parse(line) for line in f.readlines()]

# print(do_line(exprs[-1]))
print(sum(list(map(lambda x: x[0], filter(do_line, exprs)))))
