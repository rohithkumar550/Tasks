def ascii_to_hex(s):
    return ' '.join(format(ord(c), '02x') for c in s)

# Example
print(ascii_to_hex("Hi"))
