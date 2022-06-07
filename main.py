# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    import string
    with open(filename) as f:        
        text = " ".join(f.readlines())
        print(text)
        text.strip()
        text = text.translate(str.maketrans('','',string.punctuation))
    
    return text


def count_words():
    from collections import Counter
    text = read_file_content("./story.txt").split(' ')
    text = Counter(text)
    del text['\n']
    del text['\t']
    del text[' ']
    return text
print(count_words())

