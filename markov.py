"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    
    opened_file = open(file_path)
    opened_file = opened_file.read()

    return opened_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    split_word = text_string.split()

    for word in range(len(split_word) - 2):
        #new_tuple is two words being added to dictionary key
        new_tuple = (split_word[word], split_word[word + 1])
        if chains.get(new_tuple) == None:
            chains[new_tuple] = []
            chains[new_tuple].append(split_word[word + 2])
        else: 
            chains[new_tuple].append(split_word[word + 2])
        

    return chains
   




def make_text(chains):
    """Return text from chains."""
    
    # words             = randomized text being formed into list
    # rand_start        = random key from chains
    # next_first_key    = first string in next key
    # next_second_key   = second string in next key
    # next_key          = next key to values added to words

    words = []
    rand_start = choice(list(chains.keys()))
    current_key = rand_start
    next_first_key = current_key[1]
    next_second_key = choice(list(chains.get(current_key)))
    next_key = (next_first_key, next_second_key)
    
    # while loop that operates until next_key is not in chains
    while next_key in chains.keys(): 
        #append first word in key to list of randomized words
        words.append(current_key[0])
        #gets next first word of key from second word in current_key
        next_first_key = current_key[1]
        #gets second word of next key from a random list of the current_key's value
        next_second_key = choice(list(chains.get(current_key)))
        next_key = (next_first_key, next_second_key)
        current_key = next_key
    
    words.append(current_key[0] + " " + current_key[1])
    
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# prints the original text
print(input_text)

# Get a Markov chain dictionary
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
