# **Kwargs
# dictionary {key: value}

"""
def marks (**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


student1 = {"Bangla": 87, "Math": 98, "English": 77}
marks(**student1)
"""

"""
# ai bar amra ak line a print korbo

def marks (**kwargs):
    blank_dict = dict()
    for k, v in kwargs.items():
        blank_dict[k] = v
    return blank_dict


student1 = {"Bangla": 87, "Math": 98, "English": 77}
print(marks(**student1))
"""

def marks (**kwargs):
    print(type(kwargs))


marks()
