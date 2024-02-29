#! /usr/bin env python3

#import string module for getting alphebet
import string

#getting lowercase letters
lowercase_letters = list(string.ascii_lowercase)

#getting uppercase letters
uppercase_letters = list(string.ascii_uppercase)

#show a ascii value of each letter
def get_ascii(letter):
    print(f"letter {letter} ascii value is :- "+ str(ord(letter)))

if __name__ == "__main__":
    #get ascii value of lowercase letters
    for i in range(26):
        get_ascii(lowercase_letters[i])

    #add 2 line brakes
    print("\n\n")

    #get ascii value of uppercase letters
    for i in range(26):
        get_ascii(uppercase_letters[i])
#EOF