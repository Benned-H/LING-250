# Class 6 Notes - 2/3/2022
# To set up my machine, I needed to install Git (using XCode) as well as Anaconda and then nltk

# In order to install data and models:

"""
import nltk
print('Downloading NLTK...')
nltk.download()
print('Done downloading...')
"""

# Let's use the Genesis corpus, with various translations of the book of Genesis

from nltk.corpus import genesis
genesis.fileids()
genesis.readme()

genesis.words('swedish.txt') # Get words [w1, w2, ...]
genesis.sents('swedish.txt') # Get sentences [[s1w1, s1w2, ...], ...]

# The NLTK includes various tokenizers for words or sentences

from nltk.tokenize import word_tokenize, sent_tokenize

word_tokenize('Hello, my name is Benned. What is yours?') # Gives list of words
sent_tokenize('Hello, my name is Benned. What is yours?') # Gives list of sentences

# We can create a vocabulary list using the set() function to turn lists into sets
kjv_words = genesis.words('english-kjv.txt')
len(kjv_words) # Total number of words
len(set(kjv_words)) # Total number of word types

# List comprehensions will also provide a clearer way to find the words we care about
