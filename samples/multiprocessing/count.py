import codecs
import time
from multiprocessing import Pool

with codecs.open("alice.txt", "r", "utf-8") as infile:
    lines = infile.readlines()
    print(len(lines))

def count_words(line):
    num = len(line.split(" "))

start_time = time.time()
with Pool(4) as pool:
    pool.map(count_words, lines[:10])

print(time.time() - start_time)
