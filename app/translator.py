from langdetect import detect
from deep_translator import GoogleTranslator

def detect_language(text: str) -> str:
    return detect(text)

def translate_text(text: str, target_lang: str = 'en') -> str:
    return GoogleTranslator(source='auto', target=target_lang).translate(text)
