from collections import Counter
def find_extra_char(s1, s2):
    return (Counter(s2) - Counter(s1)).most_common(1)[0][0]
# Example
print(find_extra_char("abc", "abcz"))
