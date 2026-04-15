from itertools import permutations
s=input("Enter a word:")
words = set()
for i in range(1, len(s)+1):
    for p in permutations(s,i):
        word=''.join(p)
        words.add(word)
print("All possible smallerwords are:")
for w in sorted(words):
    print(w)
