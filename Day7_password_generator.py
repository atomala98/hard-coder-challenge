from random import sample
import string
from pyperclip import copy

possible_characters = [string.ascii_lowercase, string.ascii_uppercase,  string.digits, string.punctuation]
possible_characters_list = "".join(possible_characters)

while True:
    try:
        k = int(input("Number of characters: "))
        if k < 8:
            raise Exception("Need more than 8 characters")
        break
    except Exception as ex:
        print(ex)
        
while True:
    password = "".join(sample(possible_characters_list, k))
    try:
        for i in possible_characters:
            if not (set(i) & set(password)):
                raise Exception(str(i))
        break
    except:
        pass
    
print("Your generated password: {}".format(password))
copy(password)