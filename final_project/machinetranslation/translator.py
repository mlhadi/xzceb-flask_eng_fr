import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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

def englishToFrench(englishText):
    """Translates English to French"""
    if englishText == '':
        return json.dumps(dict(message='Input cannot be null.'))
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr'
    ).get_result()
    # return print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation['translations'][0]['translation']

def frenchToEnglish(frenchText):
    """Translates French to English"""
    if frenchText == '':
        return json.dumps(dict(message='Input cannot be null.'))
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en'
    ).get_result()
    # return print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation['translations'][0]['translation']
