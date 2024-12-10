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
while back_ptr > 0:
    while huge_thing[back_ptr] == '.':
        back_ptr -= 1

    ch = huge_thing[back_ptr]
    ch_count = 0
    while huge_thing[back_ptr] == ch:
        ch_count += 1
        back_ptr -= 1
    back_ptr += 1

    i = 0
    dot_count = 0

    while i < back_ptr:
        dot_count = 0
        while huge_thing[i] != '.':
            i += 1

        while i + dot_count < len(huge_thing) and huge_thing[i + dot_count] == '.':
            dot_count += 1

        diff = dot_count - ch_count
        if diff >= 0 and i < back_ptr:
            huge_thing[back_ptr:back_ptr + ch_count], huge_thing[i:i + ch_count] = huge_thing[i:i + ch_count], huge_thing[back_ptr:back_ptr + ch_count]
            i -= 1
            break
        i += 1

    back_ptr -= 1

# while huge_thing[back_ptr] == '.':
#     back_ptr -= 1
#     continue

# i = 0
# dot_size = 0
# while i < len(huge_thing) and back_ptr > 0:
#     if huge_thing[i] == '.':
#         dot_size += 1
#         i += 1
#         continue

#     if dot_size > 0:
#         j = back_ptr
#         while j > 0:
#             while huge_thing[j] == '.':
#                 j -= 1
#                 continue

#             ch = huge_thing[j]
#             ch_count = 0
#             while huge_thing[j] == ch:
#                 ch_count += 1
#                 j -= 1
#             j += 1

#             diff = dot_size - ch_count
#             if diff >= 0 and i < j:
#                 print(i-ch_count, j, huge_thing[i-ch_count:i], huge_thing[j:j+ch_count])
#                 huge_thing[i-dot_size:i-diff], huge_thing[j:j+ch_count] = huge_thing[j:j+ch_count], huge_thing[i-dot_size:i-diff]
#                 print(huge_thing)
#                 # back_ptr = j
#                 back_ptr = len(huge_thing) - 1
#                 i -= dot_size
#                 break
#             j -= 1

#     while huge_thing[back_ptr] == '.':
#         back_ptr -= 1
#         continue
#     i += 1
#     dot_size = 0

accum = 0
for i in range(len(huge_thing)):
    if huge_thing[i] != '.':
        accum += i * int(huge_thing[i])

# print(''.join(str(i) for i in huge_thing))
print(accum)
