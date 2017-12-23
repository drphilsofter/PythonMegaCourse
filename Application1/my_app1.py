import random

vowels = "AEIOU"
consanants = "BCDFGHJKLMNPQRSTVWXYZ"
letters = "QWERTYUIOPLKJHGFDSAZXCVBNM"

var_1 = input('V for vowel, C for consanant, A for any letter: ')
var_2 = input('V for vowel, C for consanant, A for any letter: ')
var_3 = input('V for vowel, C for consanant, A for any letter: ')

def random_letters():
    if var_1 == 'V':
        l1 = random.choice(vowels)
    elif var_1 == 'C':
        l1 = random.choice(consanants)
    elif var_1 == "A":
        l1 = random.choice(letters)
    else:
        print("You did not follow instructions. I hope it was worth it. Monster")
        l1 = 'You fuckwit'
        
    if var_2 == 'V':
        l2 = random.choice(vowels)
    elif var_2 == 'C':
        l2 = random.choice(consanants)
    elif var_2 == 'A':
        l2 = random.choice(letters)
    else:
        print("You did not follow instructions. I hope it was worth it. Monster")
        l2 = 'You fuckwit'
    
    if var_3 == 'V':
        l3 = random.choice(vowels)
    elif var_3 == 'C':
        l3 = random.choice(consanants)
    elif var_3 == 'A':
        l3 = random.choice(letters)
    else:
        print("You did not follow instructions. I hope it was worth it. Monster")
        l3 = 'You fuckwit'
    
    combo = l1 + l2 + l3
    return combo

for i in range(10):
    print(random_letters())