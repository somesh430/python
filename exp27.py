class Reverse:
    def reverse_word(self, s):
        words = s.split()             
        reversed_words = []
        for word in words:
            reversed_words.append(word[::-1])  
        return " ".join(reversed_words)
r = Reverse()
s = input("Enter string: ")
print(r.reverse_word(s))
