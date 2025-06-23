def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
