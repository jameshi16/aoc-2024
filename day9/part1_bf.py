with open('input.txt') as f:
    thing = [element for element in f.readlines()[0][:-1]]

huge_thing = []
counter = 0
for i in range(0, len(thing)):
    if i % 2 != 0:
        for j in range(int(thing[i])):
            huge_thing.append('.')
        continue
    for j in range(int(thing[i])):
        huge_thing.append(counter)
    counter += 1

back_ptr = len(huge_thing) - 1
for i in range(0, len(huge_thing)):
    if i > back_ptr:
        break

    if huge_thing[i] == '.':
        huge_thing[i], huge_thing[back_ptr] = huge_thing[back_ptr], huge_thing[i]
        while huge_thing[back_ptr] == '.':
            back_ptr -= 1
            continue

accum = 0
for i in range(len(huge_thing)):
    if huge_thing[i] != '.':
        accum += i * int(huge_thing[i])

# print(''.join(str(i) for i in huge_thing))
print(accum)
