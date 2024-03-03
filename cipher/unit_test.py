import unittest
import random
from ReproCipher import Cipher

class TestCipher(unittest.TestCase):

    
    def test_invalid_postitive_keys(self):
        """ 
            Enter unusuel positive values and test raising value error or not
        """
        unusual_positive_values = [random.randint(25, 100_000) for _ in range(10)]
        for key in unusual_positive_values:
            with self.subTest(key=key):
                with self.assertRaises(ValueError):
                    Cipher("test", key=key)

    def test_invalid_negative_keys(self):
        """ 
            Enter unusuel negative values and test raising value error or not
        """
        unusual_negative_values = [random.randint(-100_000, 1) for _ in range(10)]
        for key in unusual_negative_values:
            with self.subTest(key=key):
                with self.assertRaises(ValueError):
                    Cipher("test", key=key)

    def test_invalid_text(self):
        # Test if ValueError is raised when text is None
        with self.assertRaises(ValueError):
            cipher_instance = Cipher(text=None, key=3)

    def test_random_text_generation(self):
        # Test if generated random text has the correct length
        random_text = Cipher.generated_text(10)
        self.assertEqual(len(random_text), 10)

    def test_adder(self):
        # Test the adder function with known input and expected output
        encrypted_text = "abcd"
        random_text1 = "xyz"
        random_text2 = "123"
        divide = 2
        expected_result = "abxyzcd123"
        result = Cipher.adder(encrypted_text, random_text1, random_text2, divide)
        self.assertEqual(result, expected_result)

    def test_substitution_cipher_lower_case(self):
        # Test with lower case letters
        text = "hello"
        key = 3
        expected_result = "khoor"
        self.assertEqual(Cipher.substitution_cipher(text, key), expected_result)

    def test_substitution_cipher_upper_case(self):
        # Test with upper case letters
        text = "HELLO"
        key = 3
        expected_result = "KHOOR"
        self.assertEqual(Cipher.substitution_cipher(text, key), expected_result)

    def test_substitution_cipher_mixed_case(self):
        # Test with mixed case letters
        text = "Hello World"
        key = 5
        expected_result = "Mjqqt Btwqi"
        self.assertEqual(Cipher.substitution_cipher(text, key), expected_result)

    def test_substitution_cipher_special_characters(self):
        # Test with special characters
        text = "!@#$%^&*()"
        key = 10
        expected_result = "!@#$%^&*()"
        self.assertEqual(Cipher.substitution_cipher(text, key), expected_result)

    def test_substitution_cipher_empty_string(self):
        # Test with an empty string
        text = ""
        key = 7
        expected_result = ""
        self.assertEqual(Cipher.substitution_cipher(text, key), expected_result)

if __name__ == '__main__':
    unittest.main()
