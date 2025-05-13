# Multilingual Translator Web Application

## Overview

This project is a web application that translates articles between English, Spanish, French, and Hindi. It also summarizes the articles within a 50-word limit. Built with Python and Flask, the application allows users to input an article in any of the supported languages and receive a translated version in their desired language, along with a brief summary. This is achieved by utilizing machine learning libraries and APIs for both translation and summarization tasks within the Flask framework.

## Key Features

*   **Multilingual Translation:** Translates articles between English, Spanish, French, and Hindi.
*   **Article Summarization:** Generates concise summaries of input articles, limited to 50 words.
*   **User-Friendly Interface:** Simple and intuitive web interface for easy interaction.

## Tech Stack

*   **Backend:** Python, Flask
*   **Machine Learning Models:**
    *   **Translation:**
        *   `Helsinki-NLP/opus-mt-en-es` (English to Spanish)
        *   `Helsinki-NLP/opus-mt-es-en` (Spanish to English)
        *   `Helsinki-NLP/opus-mt-en-fr` (English to French)
        *   `Helsinki-NLP/opus-mt-fr-en` (French to English)
        *   `Helsinki-NLP/opus-mt-en-hi` (English to Hindi)
        *   `Helsinki-NLP/opus-mt-hi-en` (Hindi to English)
    *   **Summarization:**
        *   `facebook/bart-large-cnn` (English, Spanish, French, Hindi)



## ML Model Details

The project utilizes the following machine learning models for translation and summarization:

*   **Translation Models:** The `Helsinki-NLP/opus-mt-*` models are used for translation between English, Spanish, French, and Hindi.  These models are loaded using the Hugging Face `pipeline` function:

    ```python
    translator_en_to_es = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")
    translator_es_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
    # ... other translation models
    ```

*   **Summarization Models:** The `facebook/bart-large-cnn` model is used for summarization.

    ```python
    summarizer_en = pipeline("summarization", model="facebook/bart-large-cnn")
    # ... other summarization models
    ```

## Usage

1.  Enter the text you want to translate and/or summarize into the input field.
2.  Select the source language.
3.  Select the target language (for translation).
4.  Submit the form.
5.  The translated text and/or summary will be displayed on the page.

## Future Enhancements

*   Support for more languages.
*   Customizable summary length.
*   Improved error handling and user feedback.

## Contributors

*   Aditi Singh
