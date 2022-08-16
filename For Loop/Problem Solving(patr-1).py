"""
# 1 - 10
for i in range(1, 11):
    print(i)

text = "I love Python"
for i in range(1, 6):
    print(text)
"""

"""
sumation = 0
for i in range(1, 5):
    sumation += i
print(sumation)

"""

# ai bar amra user ar kas thaka input nebo
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
end = end + 1
summation = 0
for i in range(start, end):  # end(n - 1)
    summation += i
print(summation)