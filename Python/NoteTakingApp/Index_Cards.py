
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

class Index_Cards:

    # Input the notes
    notes = "The quick brown fox jumps over the lazy dog. The dog is not impressed."

    # Preprocess the notes
    sentences = sent_tokenize(notes)
    tokens = [word_tokenize(sentence) for sentence in sentences]
    tagged_tokens = [nltk.pos_tag(token) for token in tokens]

    # Create index cards
    index_cards = []
    for tagged_sentence in tagged_tokens:
        for i in range(len(tagged_sentence)):
            word, pos = tagged_sentence[i]
            if pos == "NN":
                index_cards.append((word, " ".join([tagged_sentence[j][0] for j in range(i + 1, len(tagged_sentence)) if tagged_sentence[j][1] != "IN"])))

    # Output the index cards
    for card in index_cards:
        print(f"{card[0]}: {card[1]}")
