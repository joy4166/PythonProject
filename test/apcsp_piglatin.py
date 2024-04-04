string = input("Type word: ")
vowels = ["a", "e", "i", "o", "u"]
if string[0] in vowels:
    string += "-yay"
else:
    f_word = string[0]
    string = string[1:]
    string += f"-{f_word}ay"
print(string)