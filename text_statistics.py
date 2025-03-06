import string
from collections import Counter


def text_analyzer(text):
    text = text.translate(str.maketrans('','', string.punctuation)).lower()
    
    if not text:
        print("No valid words to analyze")
        return

    words = text.split()

    num_words = len(words)
    num_characters = sum(len(word) for word in words)
    
    longest_word = max(words,key=len)
    shortest_word = min(words,key=len)

    unique_words = set(words)

    word_frequencies = Counter(words)
    word_frequencies = dict(sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True))

    print(f"Number of words: {num_words}")
    print(f"Number of characters: {num_characters}")
    print(f"Longest word: {longest_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Unique words: {unique_words}")
    print("Word frequencies:")
    for word, freq in word_frequencies.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    text = input("Enter a text: ")
    text_analyzer(text)