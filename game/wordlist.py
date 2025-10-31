# game/wordlist.py
import os
import random

CATEGORY_FILES = {
    "animals": "animals.txt",
    "fruits": "fruits.txt",
    "english": "english_general.txt",
    "science": "science.txt"
}

def load_words(category=None):
    words = []
    base_path = os.path.join(os.path.dirname(__file__), "../words/categories")
    if category and category.lower() in CATEGORY_FILES:
        filepath = os.path.join(base_path, CATEGORY_FILES[category.lower()])
        with open(filepath, "r") as f:
            words = [line.strip() for line in f if line.strip()]
    else:
        for file in CATEGORY_FILES.values():
            filepath = os.path.join(base_path, file)
            with open(filepath, "r") as f:
                words += [line.strip() for line in f if line.strip()]
    return words

def choose_word(category=None):
    words = load_words(category)
    return random.choice(words)

