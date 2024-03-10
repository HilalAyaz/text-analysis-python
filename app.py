from flask import Flask, render_template, request
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

app = Flask(__name__)

# Initialize NLTK resources
nltk.download('punkt')

# Function to perform text analysis
def analyze_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    num_paragraphs = text.count('\n\n') + 1
    num_sentences = len(sentences)
    num_words = len(words)
    num_characters = sum(len(word) for word in words)
    avg_words_per_sentence = num_words / num_sentences if num_sentences > 0 else 0
    avg_characters_per_word = num_characters / num_words if num_words > 0 else 0
    most_common_words = Counter(words).most_common(5)

    return {
        'num_paragraphs': num_paragraphs,
        'num_sentences': num_sentences,
        'num_words': num_words,
        'num_characters': num_characters,
        'avg_words_per_sentence': avg_words_per_sentence,
        'avg_characters_per_word': avg_characters_per_word,
        'most_common_words': most_common_words
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        analysis_results = analyze_text(text)
        return render_template('index.html', results=analysis_results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
