from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load translation models
translator_en_to_es = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")
translator_es_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
translator_en_to_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
translator_fr_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
translator_en_to_hi = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")
translator_hi_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-hi-en")

# Load multilingual summarization models
summarizer_en = pipeline("summarization", model="facebook/bart-large-cnn")
summarizer_es = pipeline("summarization", model="facebook/bart-large-cnn")  # Use Spanish-specific model if available
summarizer_fr = pipeline("summarization", model="facebook/bart-large-cnn")  # Use French-specific model if available
summarizer_hi = pipeline("summarization", model="facebook/bart-large-cnn")  # Use Hindi-specific model if available

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']

    if source_lang == 'en' and target_lang == 'es':
        translated_text = translator_en_to_es(text)[0]['translation_text']
    elif source_lang == 'es' and target_lang == 'en':
        translated_text = translator_es_to_en(text)[0]['translation_text']
    elif source_lang == 'en' and target_lang == 'fr':
        translated_text = translator_en_to_fr(text)[0]['translation_text']
    elif source_lang == 'fr' and target_lang == 'en':
        translated_text = translator_fr_to_en(text)[0]['translation_text']
    elif source_lang == 'en' and target_lang == 'hi':
        translated_text = translator_en_to_hi(text)[0]['translation_text']
    elif source_lang == 'hi' and target_lang == 'en':
        translated_text = translator_hi_to_en(text)[0]['translation_text']
    else:
        translated_text = "Translation not supported for the selected languages."

    return jsonify({'translated_text': translated_text})

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    language = request.form['language']

    if language == 'en':
        summary = summarizer_en(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    elif language == 'es':
        summary = summarizer_es(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    elif language == 'fr':
        summary = summarizer_fr(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    elif language == 'hi':
        summary = summarizer_hi(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    else:
        summary = "Summary not available for the selected language."

    return jsonify({'summary': summary})

if __name__ == "__main__":
    app.run(debug=True)
