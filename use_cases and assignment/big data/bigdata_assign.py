from collections import defaultdict
import string

def remove_punctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))

def mapper(words):
    word_count = defaultdict(int)
    for word in words:
        cleaned_word = remove_punctuation(word)
        word_count[cleaned_word] += 1
    return word_count

def reducer(mapped_dicts):
    reduced_dict = defaultdict(int)
    for word_count in mapped_dicts:
        for word, count in word_count.items():
            reduced_dict[word] += count
    return reduced_dict

# Define the file text
file_text = """
The quick brown fox jumps over the lazy dog. 
How much wood would a woodchuck chuck if a woodchuck could chuck wood? 
Peter Piper picked a peck Of pickled peppers. 
She sells seashells by the keashore. 
I scream, you scream, we all scream for ice cream. 
To be or not to be, that is the question. 
All's well that ends well.
"""

# Split the file text into lines and then into words
lines = [line.split() for line in file_text.splitlines()]

mapped_dicts = [mapper(words) for words in lines]
reduced_dict = reducer(mapped_dicts)

# Print the word count
for word, count in reduced_dict.items():
    print(f"{word}: {count}")



