# transltor.py
# Requirements: pip install google-cloud-translate argparse

import argparse
from google.cloud import translate_v2 as translate

class Translator:
    def __init__(self):
        self.client = translate.Client()

    def translate_text(self, text: str, target_lang: str, source_lang: str = "auto") -> str:
        """Translate text using Google Cloud Translation API"""
        result = self.client.translate(
            values=text,
            target_language=target_lang,
            source_language=source_lang
        )
        return result['translatedText']

def main():
    parser = argparse.ArgumentParser(description="Command-line Translation Tool")
    parser.add_argument("--text", required=True, help="Text to translate")
    parser.add_argument("--target", required=True, 
                       help="Target language code (e.g., 'es', 'fr', 'de')")
    parser.add_argument("--source", default="auto", 
                       help="Source language code (default: auto-detect)")
    
    args = parser.parse_args()
    
    try:
        translator = Translator()
        translated_text = translator.translate_text(
            args.text,
            args.target,
            args.source
        )
        
        print(f"\nSource Text ({args.source}): {args.text}")
        print(f"Translated Text ({args.target}): {translated_text}\n")
        
    except Exception as e:
        print(f"Translation failed: {str(e)}")

if __name__ == "__main__":
    main()