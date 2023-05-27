from flask import Flask, render_template
import random
import string
import logging
import nltk
from nltk.corpus import words

app = Flask(__name__)
nltk.download('words')

def generate_passphrase(length=4, amount=5):
    word_list = words.words()
    passphrases = []
    for _ in range(amount):
        selected_words = random.sample(word_list, length)
        delimiter_list = [random.choice(string.punctuation + string.digits) for _ in range(length - 1)]
        passphrase = ""
        for i, word in enumerate(selected_words):
            passphrase += word
            if i < length - 1:
                passphrase += delimiter_list[i]
        passphrases.append(passphrase)
    return passphrases



@app.route('/')
def home():
    try:
        pass
    except Exception as e:
        logging.exception("An error occurred:")
        return "An internal error occurred.", 500
    passphrases = generate_passphrase(length=4, amount=5)
    return render_template('index.html', passphrases=passphrases)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
