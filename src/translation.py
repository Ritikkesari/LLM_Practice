from transformers import pipeline


# Function to translate text
def translate(text, source_lang="en", target_lang="es"):
    # Load the translation pipeline for translation tasks
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")

    # Translate the text from source_lang to target_lang
    translated_text = translator(text, src_lang=source_lang, tgt_lang=target_lang)[0]['translation_text']
    return translated_text

# Example usage:
if __name__ == "__main__":
    text_to_translate = "thankyou so much"
    translated_text = translate(text_to_translate, source_lang="en", target_lang="es")
    print(f"Translated text: {translated_text}")
