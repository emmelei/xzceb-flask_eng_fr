'''This module contains methods to translate from English to French and vice versa
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Translates string argument from English to French'''
    translation = language_translator.translate(
        english_text,
        model_id='en-fr').get_result()

    return translation.get("translations")[0].get("translation")

def french_to_english(french_text):
    '''Translates string argument from French to English'''
    translation = language_translator.translate(
        french_text,
        model_id='fr-en').get_result()

    return translation.get("translations")[0].get("translation")
