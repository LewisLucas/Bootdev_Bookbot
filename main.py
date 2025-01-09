def count_words(data):
    return len(data.split())

def count_characters(data):
    result = {}
    l = list(data.lower())
    for alpha in "abcdefghijklmnopqrstuvwxyz":
        count = 0
        for letter in l:
            if letter == alpha:
                count += 1
        result[alpha] = count
    return result
    
book_dir = "books/frankenstein.txt"
with open(book_dir) as f:
    text = f.read()

characters = count_characters(text)
words = count_words(text)

print(f"--- Begin report of {book_dir} ---")
print(f"{words} words found in the document\n")
for letter in "abcdefghijklmnopqrstuvwxyz":
    print(f"The '{letter}' character was found {characters[letter]} times")