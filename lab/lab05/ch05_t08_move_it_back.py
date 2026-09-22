original = input("Enter a word:")
pyg = 'ay'

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
else:
    print("empty")
