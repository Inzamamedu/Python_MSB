"""
info = {}

info["Name"] = "Inzamam"
info["Country"] = "Bangladesh"
print(info)
"""

"""
info = {'Name': 'Inzamam', 'Country': 'Bangladesh'}

info[1] = "python"
info[2] = "java"
print(info)

"""

"""
info = {'Name': 'Inzamam', 'Country': 'Bangladesh', 1: 'python', 2: 'java'}
info["Name"] = "John De Costa"
print(info)

"""

info1 = {'Name': 'Inzamam', 'Country': 'Bangladesh'}
info2 = {1: 'python', 2: 'java'}

info1.update(info2)  # ai khana info 2 ka info1 ar modda dhukono hoi ca

info1["programming"] = "Python"
print(info1)