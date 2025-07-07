n = int(input())
words = []
for i in range(n):
    word = input().strip()
    words.append(word)
word_count = {}
unique_words = []

for word in words:
    if word not in word_count:
        word_count[word] = 0 
        unique_words.append(word)  
    word_count[word] += 1


result_counts = [word_count[word] for word in unique_words]

print(len(unique_words))
print(" ".join(map(str, result_counts)))