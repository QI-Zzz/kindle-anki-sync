import string

def get_highlighted_words(filename):

    # Open file 
    with open(filename, "r", encoding="utf-8-sig") as f:
        content = f.read()

    # Read the file line by line. Each note is seperated by "========"
    # Extract the highlights
    # Filter highlights with only one word
    words = []

    for highlight in content.split("========"):
        lines = highlight.strip().split('\n')
        if not lines:
            continue
        last_line = lines[-1].strip()
        if len(last_line.split()) == 1:
            word = last_line.strip().translate(str.maketrans('', '', string.punctuation))
            if word:
                words.append(word.lower())
    
    return list(set(words))
    # print(words)

if __name__ == "__main__":
    get_highlighted_words("test_clippings.txt")