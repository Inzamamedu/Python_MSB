"""
my_set = {"John", "Rock", "Inzamam"}

for i in my_set:
    print(i)

"""

"""
# one line a nea ashar neaom 
my_set = {"John", "Rock", "Inzamam"}
blank_set = {*()}

for i in my_set:
    blank_set.add(i)
print(blank_set)
"""

# ai bar ame veery word ar first letter ka access korbo
my_set = {"John", "Rock", "Inzamam"}
blank_set = {*()}

for i in my_set:
    blank_set.add(i[0])
print(blank_set)

