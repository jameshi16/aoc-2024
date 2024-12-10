with open('input.txt') as f:
    thing = [element for element in f.readlines()[0][:-1]]

a = 1
b = len(thing) - 1
tmp = int(thing[a])

accum = 0

index = int(thing[0])

while a < b:
    thing_a, thing_b = int(thing[a]), int(thing[b])
    diff = tmp - thing_b
    # print(a, b, tmp, (a - 1) // 2, b // 2, diff, thing)
    if diff > 0:
        file_id = b // 2
        occurs = thing_a - diff
        if file_id > 0:
            for i in range(occurs):
                # print('mult', file_id, index)
                accum += file_id * index
                index += 1
        b -= 2
        tmp = diff
    elif diff == 0:
        file_id = (a - 1) // 2
        occurs = int(thing[a - 1])
        for i in range(occurs):
            # print('mult', file_id, index)
            accum += file_id * index
            index += 1

        file_id = (b // 2)
        occurs = tmp

        for i in range(occurs):
            # print('mult', file_id, index)
            accum += file_id * index
            index += 1
        a += 2
        b -= 2
        tmp = int(thing[a])
    else: # diff < 0
        file_id = (a - 1) // 2
        occurs = int(thing[a - 1])
        if file_id > 0:
            for i in range(occurs):
                # print('mult', file_id, index)
                accum += file_id * index
                index += 1

        file_id = (b // 2)
        occurs = tmp
        for i in range(occurs):
            # print('mult', file_id, index)
            accum += file_id * index
            index += 1
        thing[b] = str(thing_b - tmp)
        a += 2
        tmp = int(thing[a])
    # nprint(accum)

file_id = (a - 1) // 2
occurs = int(thing[a - 1])
for i in range(occurs):
    # print('mult', file_id, index)
    accum += file_id * index
    index += 1
# print(thing)
# print(b)
print(accum)
