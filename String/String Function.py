"""
text1 = "Py"
text2 =  "thon"

print(text1 + text2)


text1 = "All"
text2 = "is"
text3 = "well"

#print(text1 + "-" + text2 + "-" + text3)
print("-".join((text1, text2, text3)))

text1 = "Python"

#print(len(text1))
#print(len("hello"))

v = len("hello")
print(v)
"""

"""
inp = input()
inp = inp.capitalize()  #tirst letter ta boro hatar kora
print(inp)
"""

"""
text = "i love python"
text = text.upper()  # shob boro hatar kora

print(text)
"""

"""
text = "i love python"
text = text.title()  # word ar first litter gula boro hatar hoba

print(text)
"""

"""
name = input()
text = name.title()  # word ar first litter gula boro hatar hoba

print(text)
"""

"""
text = "i lovE pyThon"
text = text.lower()  #sob small litter a hoi jaba

print(text)
"""

"""
text = "i lovE pyThon"
text = text.casefold()  #sob small litter a hoi jaba soto boro jai thakuk

print(text)
"""


"""
text = "i lovE pyThon"
text = text.swapcase()  #ai ta small a capital kora ar capital ka small kora {amra ja dot use kore ai ta ka period bola}
"""

"""
text = "My name is Inzamam"
print(text.count("I"))  #ar kaj hossa count kora
print(text.count("z"))
print(text.count("a",4))  # ai khana a koto bar asa ar start korba 4 no position thaka
"""


"""
text = "My name is Inzamam"
print(text.rfind("a"))  #ai ta dan dik thaka khujba
#print(text.find("n"))  #ai khana index koto number a asa oi ta khujba left side thaka
#print(text.find("a",5))  #ai tar mana holo a 5 num index ar pora kon index a asa oi ta output deba
#print(text.find("a",5,8))   #ai khana ending o boundry kora daua jai ai khana 5 num index thaka 8 index midda a ka find korba
#print(text.count("a",5,8))  #count o star and ending set kora jai
"""

"""
text = "It is a beautiful day"
new = text.replace("is","was")
print(new)
print("Original text:",text)  # non-mutable / imutable
"""

"""
text = "   Aditta Chakraborty   "
#print(text.strip(" "))  # ai .strip ar kaj holo left and right 2 side thakai cut kora
print(text.lstrip(" Adi"))
print(text.rstrip("dorty "))
"""
"""
text = "I love Bangladesh"
print(text.split())  # ai .split() ar kaj hossa ja kono text ka tukra kora vanga list akara prokash kora output a


print(text.split()[0])
print(text.split()[1])
print(text.split()[2])
"""

""" 
text = "Python"
print(text.center(9,"*"))  #static
print(text.center(len(text) +8, "*"))  #static
"""

""" .startswith()

text = "I love Python"
print(text.startswith("I"))
print(text.startswith("z"))
"""
# .endswith("")
text = "I love Python"
print(text.endswith("on"))
print(text.endswith("I"))



