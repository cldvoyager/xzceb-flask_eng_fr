import unittest
import translator

class TestTranslation(unittest.TestCase):
    def test_null_french_to_english(self):
        self.assertNotEqual(translator.french_to_english("None"), '')

    def test_null_english_to_french(self):
        self.assertNotEqual(translator.english_to_french("None"), '')
            
    def test_equal_french_to_english(self):
        # translate from french to english
        french_text = 'Bonjour'
        result = translator.french_to_english(french_text)
        english_text = result['translations'][0]['translation']
        print("French text:"+french_text)
        print("Translated English text:"+english_text)
             
    def test_equal_english_to_french(self):
        # translate from english to french
        english_text = 'Hello'
        result = translator.english_to_french(english_text)
        french_text = result['translations'][0]['translation']
        print("English text:"+english_text)
        print("Translated French text:"+french_text)
             
if __name__ == '__main__':
    unittest.main()
    