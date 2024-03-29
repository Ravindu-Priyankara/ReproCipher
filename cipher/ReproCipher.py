#!/usr/bin/env python3

import random,string



class Cipher:
    def __init__(self,text=None,key = None):
        random.seed(42)
        if text is None:
            raise ValueError("Text cannot be None.")
        if key is not None and (key > 25 or key < 0):
            raise ValueError("Key must be between 0 and 25.")
        else:
            self.key = self.encrypting_key()

        self.text = text
        self._encrypted_value = None
        self.main()
    
    @property
    def encrypted_output(self):
        return self._encrypted_value
    
    @encrypted_output.setter
    def encrypted_output(self,value):
        self._encrypted_value = value

    @staticmethod
    def encrypting_key():
        """
            This function used for generate a key for encrypting which value between one and twenty five. 
            it helps to avoid zero and negative numbers. If encryption key is zero. 
            it mean no encryption in substitution cipher.

            Args:
                No arguments available in this function.
            
            Return:
                int: encrypting key
            
            This function is static method of cipher class.
        """
        return random.randint(1,25)
    
    @staticmethod
    def substitution_cipher(text, key):
        """ 
            This function is static method of cipher class and provide a encrypted user given text.
            This class main purpose is encrypting user given values. 

            Args:
                text (str): This is user given value for encrypting.
                key (int): This is random generate key through encrypting_key function.

            Return:
                encrypted_text (str): This is user given value after encrypting. 

        """
        encrypted_text = ""
        for char in text:
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + key) % 26 + 97)
            elif char.isupper():
                encrypted_text += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_text += char
        return encrypted_text
    
    @staticmethod
    def generated_text(length):
        """ 
            This function used for generating random text. it helps to hide encryption option what we are used from attackers.

            Args:
                length (int): define a randome text length
            
            Return:
                str: generated random text with specific length.
        """
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    @staticmethod
    def adder(text, random_text1, random_text2, divide):
        """
            This function used for dividing subsitution ciper encrypting value in random posision and 
            Adding random text and combine it together. After that again add random text 2 in last. after all of return the final text.

            Args:
                text(str): subsitution encrypted value
                random_text1(str): random text 01 generated by generated_text function
                random_text2(str): random text 02 generated by generated_text function
                divide(int): getting posission number for dividing encrypted value
            
            Return:
                encrypted_text(str): final combination of text,random_text1 and random_text2.
                
        """
        encrypted_text = text[:divide] + random_text1 + text[divide:]
        return encrypted_text + random_text2
    

    def main(self):
        """ 
            This is the main function. Used for calling above declared functions.

        """
        try:
            cipher_text = self.substitution_cipher(self.text, self.key)
            length = len(cipher_text)
            random_text1 = self.generated_text(random.randint(1, 6))
            random_text2 = self.generated_text(random.randint(1, 6))
            divide = random.randint(0, length)
            self._encrypted_value = (self.adder(cipher_text, random_text1, random_text2, divide))
        except Exception as e:
            print(f"Error! {e}")

if __name__ == "__main__":
    cipher_instance = Cipher(text = "Hello World")
    print(cipher_instance._encrypted_value)
    #for i in range(100_000_000): cipher_instance._encrypted_value for testing purposes
    #print(cipher_instance())