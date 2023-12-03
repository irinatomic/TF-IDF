from functools import reduce
from collections import defaultdict
import glob

# REDUCE - reduce(function, iterable, initializer)
# LAMBDA - lambda arguments (accumulator, value): expression

# Clean text
def clean_text(text):

    replacements = {'\'': '', ',': '', '.': '', '!': '', '?': '', '\"': '', '“': '', '(': '', ')': '', '#': '', '@': '', '$': '', '-': '', '’': '', '/': '', '\\': ''}

    # x - text (accumulator)
    # y - replacements[i] (old, new) (value)
    text = reduce(lambda x, y: x.replace(y[0], y[1]), replacements.items(), text)

    text = text.lower()
    return text

def calculate_tf(file_path):
    with open(file_path, 'r') as file:

        # Clean text
        text = file.read()
        text = clean_text(text)

        # Char by char (space -> new word, else append to last word)
        words = reduce(lambda acc, char: acc[:-1] + [acc[-1] + char] if char != ' ' else acc + [''], text, [''])
        non_empty_words = [word for word in words if word != '']

        # Filter words len <= 3
        lengthy_words = reduce(
            lambda acc, word: acc + ([word] if len(word) > 3 else []),  
            non_empty_words,
            []  
        )
        
        # Calculate word frequencies using reduce and map
        # ** - unpacking operator (shallow copy) -> keep the function pure
        word_freq = reduce(
            lambda freq_dict, word: {**freq_dict, word: freq_dict.get(word, 0) + 1},  
            words,
            defaultdict(int)  
        )

        # Length of an array 
        length = reduce(lambda acc, _: acc + 1, lengthy_words, 0)
        
        # TUPLE: (file_path, word, tf_value)
        tf_values = list(reduce(
            lambda acc, item: acc + [(file_path, item[0], item[1] / length)],  
            word_freq.items(),
            []
        ))
        
        return tf_values


if __name__ == "__main__":

    file_paths = glob.glob('data/*.txt')

    all_tf_values = list(reduce(
        lambda acc, file_path: acc + calculate_tf(file_path),  
        file_paths,
        []
    ))

    print(len(all_tf_values))
    # for tf_value in all_tf_values:
    #     print(tf_value)