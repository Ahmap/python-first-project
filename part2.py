# s1 = input("enter a string1: ")
# s2 = input("enter a string2: ")
# print(s1 in s2)

# ---------------------------------
#
# s = input("enter something: ")
# print(s.replace(" ", "").replace("\t", ""))

# ---------------------------------

# ch = input("enter your char: ")
# print(ord(ch))

# ---------------------------------

# tel = input("enter your number: ")
# print(tel.isnumeric())

# ---------------------------------

s = input("enter a string: ")
sentences = s.count(".") + s.count("?") + s.count("!") + s.count(";")
words = s.count(" ") + 1
Characters = len(s)
Letters = Characters - (s.count(".") + s.count("?") + s.count("!") + s.count(";") + s.count(",") + s.count(":")
                        + s.count("-") + s.count(" "))
print("amount of sentences: ", sentences)
print("amount of words: ", words)
print("amount of characters : ", Characters)
print("amount of english letters: ", Letters)
