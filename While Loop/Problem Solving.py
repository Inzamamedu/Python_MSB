"""
# 1 + 2 + 3 + 4 + 5 + ........ + 50 = ?

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
summation = 0

while start <= end:
    summation += start
    start += 1
print(summation)

"""

# 123 = 6

number = input("Enter the number: ")
summation = 0
i = 0
while i < len(number):
    summation += int(number[i])
    i += 1
    print(summation)