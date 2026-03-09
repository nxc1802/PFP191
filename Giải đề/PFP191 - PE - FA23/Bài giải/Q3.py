# Q3 (3 marks): Keyword Search & Word Frequency

import string

# 1. Count sentences containing a keyword (case-insensitive)
def count_sentences_with_keyword(filepath, keyword):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        # Split into sentences by '.', '!', '?'
        sentences = []
        for part in text.replace("!", ".").replace("?", ".").split("."):
            sentence = part.strip()
            if sentence:
                sentences.append(sentence)
        count = sum(1 for s in sentences if keyword.lower() in s.lower())
        return count
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return 0


# 2. Word frequency dictionary (case-insensitive)
def word_frequency(filepath):
    freq = {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        # Remove punctuation and split into words
        translator = str.maketrans("", "", string.punctuation)
        words = text.translate(translator).lower().split()
        for word in words:
            if word:
                freq[word] = freq.get(word, 0) + 1
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    return freq


# --- Main ---
filepath = "Vietnamese_Declaration_of_Independence.txt"

# Q3.1 — Count sentences with "independent"
keyword = "independent"
count = count_sentences_with_keyword(filepath, keyword)
print(f'Number of sentences containing "{keyword}": {count}')

print()

# Q3.2 — Top 10 most frequent words
freq = word_frequency(filepath)
top10 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 most frequent words:")
for word, cnt in top10:
    print(f"  {word}: {cnt}")
