from multiprocessing import Pool

def count_words(line):
    word2count = {}
    for w in line.lower().split(" "):
        word2count[w] = word2count.get(w, 0) + 1
    return word2count

lines = [
    "I am a boy",
    "I love programming",
    "We go to hiking today",
    "The weather is nice",
    "We have to check the weather forecast"
]

with Pool(4) as pool:
    results = pool.map(count_words, lines)

word2count = {}
for r in results:
    for w, n in r.items():
        word2count[w] = word2count.get(w, 0) + n

print(word2count)
 
