
s = input("Enter the string: ")
w = int(input("Enter the width: "))

for i in range(0, len(s), w):
    print(s[i:i+w])
