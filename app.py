import gradio as gr
from src.translation import translate  # Adjust import path as per your project structure

# Function to translate text
def gradio_translate(input_text):
    translate_text = translate(input_text, source_lang="en", target_lang="es")
    return translate_text

# Create Gradio interface
interface = gr.Interface(fn=gradio_translate, inputs="textbox", outputs="textbox")

if __name__ == "__main__":
    interface.launch()
