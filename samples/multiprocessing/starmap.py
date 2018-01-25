from multiprocessing import Pool

def multiply(x, y):
    return x * y

args = [(1, 2), (3, 4), (5, 6)]
with Pool() as pool:
    results = pool.starmap(multiply, args)

print(results)
# prints [2, 12, 30]

