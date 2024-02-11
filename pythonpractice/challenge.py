# 1. Adding a prefix to a word
print("1. Adding a prefix to a word\n")

def add_prefix_un(word):
    return  "un" + word

word = str(input("Enter a word: "))
    
print(add_prefix_un(word))

# 2. Add prefixes to word groups 
print("\n2. Add prefixes to word groups\n")

def make_word_groups(vocab_words):
# prefix is always the first index
    prefix = vocab_words[0] 
    words = vocab_words[1:]

    word_groups = [f"{prefix}{word}" for word in words]
# f string to concatenate the prefix and the word_groups for loop 
    result = f"{prefix} :: {' :: '.join(word_groups)}"

    return result

# Examples given: 

print(make_word_groups(['en', 'close', 'joy', 'lighten']))
'en :: enclose :: enjoy :: enlighten'

print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
'pre :: preserve :: predispose :: preposition'

print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
'auto :: autodidactic :: autograph :: automate'

print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))
'inter :: intertwine :: interconnected :: interdependent'

# 3. Remove a suffix from a word
print("\n3. Remove a suffix from a word\n")

def remove_suffix_ness(word):
# Takes the original work and replaces 'ness' to nothing
    new_word = word.replace('ness', '')
# If the final letter of the word with 'ness' removed is 'i' then the 'i' is replaced with 'y'
    if new_word[len(new_word)-1] == 'i':
        newest_word = new_word.replace("i", "y")
        return newest_word
# If the final letter of the word with 'ness' removed is anyting other than 'i' then just return the edited word
    else:
        return new_word

print(remove_suffix_ness('heaviness'))
print(remove_suffix_ness('happiness'))

# 4. Extract and transform a word
print("\n4. Extract and transform a word\n")

def adjective_to_verb(sentence, index):
    new_sentence = sentence.strip(".,?!")
    words = new_sentence.split()
    
    verbing = words[index] + "en"
    return verbing

print(adjective_to_verb('I need to make that bright.', -1))
print(adjective_to_verb('It got dark as the sun set.', 2))

# Alternative version w/o a function
print("\nAlternative version w/o a function\n")
sentence = 'I need to make that bright.'
new_sentence = sentence.strip(".")
words = new_sentence.split() # Splits the sentence into individual words.
# Loops the sentence to get the index of each word, starting at 1 so the user can count normally.
for index, word in enumerate(words, start = 1):
    print(index, word)

index =  int(input(f"Please enter the index of the adjective 0 to {len(words)}: ")) - 1

verbing = words[index] + "en"
print(verbing)


