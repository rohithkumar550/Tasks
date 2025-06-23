def longest_unique_substring(s):
    current = ""
    longest = 0
    for char in s:
        if char in current:
            index = current.index(char)
            current = current[index + 1:]
        current += char
        longest = max(longest, len(current))

    return longest
user_input = input("Enter a string: ")
result = longest_unique_substring(user_input)
print("Length of the longest substring without repeating characters is:", result)
