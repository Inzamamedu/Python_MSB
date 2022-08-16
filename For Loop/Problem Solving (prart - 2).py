"""
text = "Python"
for i in text:
    print(i)
"""

"""
text = "Python"
for i in range(len(text)):  # ai khana len use na korla error dakha ba tai len dea int convart kora print kora hoi ca
    print(text[i])
"""
"""
for i in range(0, 11):
    if i % 2 == 0:
        print(i, "is an even")
    else:
        print(i, "is an odd")
"""

# 1234
number = input("Enter the number: ")
summation = 0
for i in range(len(number)):
    summation += int(number[i])
print(summation)