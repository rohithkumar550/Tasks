def has_duplicate_letters(sentence):
    for word in sentence.split():
        if len(set(word)) < len(word):
            return True
    return False

# Example
print(has_duplicate_letters("hello world"))
