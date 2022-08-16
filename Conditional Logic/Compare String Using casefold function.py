"""
text = "I LOVE PythoN"
print(text.lower())
print(text.casefold())
"""

firstString = "der Fluß"
secondString = "der Flusshinkh"

# ß is equivalent to ss | lower  ar casefold ar modda diff holo casefold compare korta para ar lower para na.
if firstString.casefold() == secondString.casefold():
    print("The strings are equal.")
else:
    print("The steings are not equal.")