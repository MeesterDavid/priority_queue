import math
import numpy as np
import random
import time
import priority_queue

random.seed(10)


def generate_patients(n):
    new_patients = np.array([])
    for i in range(n):
        y = random.randint(1,100)
        new_patients = np.append(new_patients, y)

    return new_patients


def brute_force_save_most_important_patient(patients: np.ndarray):
    most_urgent = np.argwhere(patients == patients.min())[0]
    patients = np.delete(patients, most_urgent)
    return patients

nr_of_new_patients =3
bigloop=100000

i=0
patients = np.array([])
start = time.time()
while i < bigloop:
    patients = np.append(patients, generate_patients(nr_of_new_patients))
    patients = brute_force_save_most_important_patient(patients)
    i+=1

duration = time.time()-start
print(f"brute force: {duration}")



"""
super nice heap minheap implementatie
"""
import heapq
start = time.time()
i =0
patients_pq = []
while i < bigloop:
    new_patients = generate_patients(nr_of_new_patients)
    for p in new_patients:
        heapq.heappush(patients_pq, p)
    heapq.heappop(patients_pq)

    i+=1

duration = time.time()-start

print(f"lib heapq  {duration}")

start = time.time()
i = 0
patients_pq_custom = []
while i < bigloop:
    new_patients = generate_patients(nr_of_new_patients)
    for p in new_patients:
        priority_queue.insert(patients_pq_custom, p)
    priority_queue.pop(patients_pq_custom)
    i+=1

duration  = time.time()-start
print(f"custom min heap: {duration}")