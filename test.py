import re 
from collections import Counter

def clean_and_tokenize(text):
    # Convert to lowercase and remove non-alphabetical characters
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return words

translated_titles=['']

all_words = []

for title in translated_titles:
        words = clean_and_tokenize(title)
        all_words.extend(words)

    # Count word occurrences
word_counts = Counter(all_words)

print(word_counts)

    # Step 3: Identify and print words that appear more than twice
repeated_words = {word: count for word, count in word_counts.items() if count > 2}

print("Repeated words (appearing more than twice):")
for word, count in repeated_words.items():
    print(f"{word}: {count}")