import unittest
import translator

class TestTranslation(unittest.TestCase):
    def test_hello_to_bonjour(self):
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')

    def test_bonjour_to_hello(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')

    def test_null_inputs(self):
        self.assertEqual(
            translator.englishToFrench(''), 
            '{"message": "Input cannot be null."}'
        )
        self.assertEqual(
            translator.frenchToEnglish(''),
            '{"message": "Input cannot be null."}'
        )

unittest.main()