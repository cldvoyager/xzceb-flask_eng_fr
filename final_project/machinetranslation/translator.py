import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['APIKEY']
URL = os.environ['URL']
VERSION = "2018-05-01"
authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(version=VERSION,authenticator=authenticator)
language_translator.set_service_url(URL)
def english_to_french(english_text):
   # Translate
    translation_response = language_translator.translate(\
    text=english_text, model_id='en-fr')
    french_text = translation_response.get_result()
    return french_text
def french_to_english(french_text):
    #Translate
    translation_response = language_translator.translate(\
    text=french_text, model_id='fr-en')
    english_text = translation_response.get_result()
    return english_text