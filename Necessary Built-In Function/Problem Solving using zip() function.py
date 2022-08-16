"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

# (1 + 4 + 7) / 3, (2 + 5 + 8) / 3, (3 + 6 + 9) / 3 = [4.0, 5.0, 6.0]

def avg(*args):
    mew_list = []
    zipped_list = zip(*args)
    for pair in list(zipped_list):
        result = sum(pair) / len(pair)     # ai prigram ta run korta pare nai
        new_list.append(result)
    return new_list

final_result = avg(l1, l2, l3)
print(final_result)

"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]


my_avg = lambda *args: [sum(pair) / len(pair) for pair in zip(*args)]

print(my_avg(11, 12, 13))