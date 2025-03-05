# translator_ui.py
# Requirements: pip install google-cloud-translate argparse
import tkinter as tk
from tkinter import messagebox
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

class TranslatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Translator UI")
        self.geometry("600x400")
        
        # Create an instance of the Translator
        self.translator = Translator()
        
        # Input label and text field for the text to translate
        tk.Label(self, text="Text to translate:").pack(pady=5)
        self.text_input = tk.Text(self, height=10, width=70)
        self.text_input.pack(pady=5)
        
        # Source language input
        tk.Label(self, text="Source Language (default 'auto'):").pack(pady=5)
        self.source_entry = tk.Entry(self, width=10)
        self.source_entry.insert(0, "auto")
        self.source_entry.pack(pady=5)
        
        # Target language input
        tk.Label(self, text="Target Language (e.g., 'es', 'fr', 'de'):").pack(pady=5)
        self.target_entry = tk.Entry(self, width=10)
        self.target_entry.pack(pady=5)
        
        # Translate button
        self.translate_button = tk.Button(self, text="Translate", command=self.perform_translation)
        self.translate_button.pack(pady=10)
        
        # Output label and text field for the translated text
        tk.Label(self, text="Translated Text:").pack(pady=5)
        self.output_text = tk.Text(self, height=10, width=70)
        self.output_text.pack(pady=5)

    def perform_translation(self):
        # Get values from UI fields
        text = self.text_input.get("1.0", tk.END).strip()
        target_lang = self.target_entry.get().strip()
        source_lang = self.source_entry.get().strip() or "auto"

        # Validate inputs
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to translate.")
            return
        if not target_lang:
            messagebox.showwarning("Warning", "Please enter a target language code.")
            return

        # Translate and display the result
        try:
            translated = self.translator.translate_text(text, target_lang, source_lang)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated)
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed: {str(e)}")

if __name__ == "__main__":
    app = TranslatorUI()
    app.mainloop()
