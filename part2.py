# Uni code of character

Character = input("Enter your character: ")
print(ord(Character))

# Check the phone number

Phone = input("Enter your number: ")
print(Phone.isnumeric())

# Information of string

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

# End of second part :D
