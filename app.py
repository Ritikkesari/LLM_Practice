import gradio as gr
from src.trasnformer import translate

def gradio_translate(text):
    translate_text = translate(text, source_lang = "en", target_lang = "es")

input_text = gr.inputs.Textbox(label = "Enter text to translate to spanish")

ouput_text = gr.outputs.Textbox(label = "Translated text")

interface = gr.Interface(fn=gradio_translate, inputs=input_text, outputs=output_text, title="Text translation")

if __name__ == "__main__":
    interface.launch()