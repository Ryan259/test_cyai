import time
import random

start = time.time()
for i in range(1, 20):
    a = random.random()
    print('Random data is:', a)

cost = time.time() - start

print('Cost time is:', cost)

