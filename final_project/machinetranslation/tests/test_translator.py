import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def testTranslation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test that Hello as input gives Bonjour as output
        self.assertNotEqual(english_to_french('Hello'), 'Bonjourno') # test that Hello as input gives Bonjour as output


class TestFrenchToEnglish(unittest.TestCase): 
    def testTranslation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test that Bonjour as input gives Hello as output
        self.assertNotEqual(french_to_english('Bonjourno'), 'Hello') # test that Bonjour as input gives Hello as output

unittest.main()