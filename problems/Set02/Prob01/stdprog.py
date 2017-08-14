n = int(input())
dictionary = []
for i in range(n):
    dictionary.append(input())
for word in dictionary:
    if len(word) <= 1:
        continue
    for i in range(1, len(word)):
        if word[:i] in dictionary and word[i:] in dictionary:
            print(word)
            break
