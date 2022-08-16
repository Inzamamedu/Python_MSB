"""
# Required Arguments

# Hello, Inzamam ul

def welcome(first_name, last_name):
    return print("Hello",first_name, last_name)


f_name = "Inzamam"
l_name = "ul"
welcome(f_name, l_name)  # Arguments

"""

"""
def welcome(first_name, last_name):
    return print("Hello,",first_name, last_name)



welcome("Inzamam", "ul")  # Arguments

"""

"""
#  keyword Arguments
def welcome(first_name, last_name):
    return print("Hello",first_name, last_name)


welcome(first_name="Inzamam",last_name="ul")
welcome(last_name="ul",first_name="Inzamam")
"""

# Default Arguments
# Hi Inzamam, how are you?
def messege(name,question= "how are you?"):   # parameter
    return print("Hi", name + ",", question)


name = "Inzamam"
qus = "Where are you going?"   # parameter ar ar vitor a default value ar thaka baira thaka assign kora valu ar priority bashe 
messege(name, qus)   # Arguments