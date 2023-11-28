import math
import numpy as np
import random
import time
import priority_queue

random.seed(10)


def generate_bargains(n):
    new_bargains = np.array([])
    for i in range(n):
        y = random.randint(1,100)
        new_bargains = np.append(new_bargains, y)

    return new_bargains


def brute_force_get_the_best_bargains(bargains: np.ndarray):
    cheapest = np.argwhere(bargains == bargains.min())[0]
    bargains = np.delete(bargains, cheapest)
    return bargains

nr_of_new_bargains = 10
bigloop=100000

i=0
bargains = np.array([])
start = time.time()
while i < bigloop:
    bargains = np.append(bargains, generate_bargains(nr_of_new_bargains))
    bargains = brute_force_get_the_best_bargains(bargains)
    i+=1

duration = time.time()-start
print(f"brute force: {duration}")



"""
super nice heap minheap implementatie
"""
import heapq
start = time.time()
i =0
bargains_pq = []
while i < bigloop:
    new_bargains = generate_bargains(nr_of_new_bargains)
    for p in new_bargains:
        heapq.heappush(bargains_pq, p)
    heapq.heappop(bargains_pq)

    i+=1

duration = time.time()-start

print(f"lib heapq  {duration}")

start = time.time()
i = 0
bargains_pq_custom = []
while i < bigloop:
    new_bargains = generate_bargains(nr_of_new_bargains)
    for p in new_bargains:
        priority_queue.insert(bargains_pq_custom, p)
    priority_queue.pop(bargains_pq_custom)
    i+=1

duration  = time.time()-start
print(f"custom min heap: {duration}")