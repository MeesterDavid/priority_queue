import math
import sys


"""" 
https://medium.com/@verdi/binary-heap-basics-40a0f3f41c8f
"""


def get_parent(pq, index):
    if index == 0:
        return None
    else:
        return math.floor((index-1)/2)


def get_child(pq, index):
    if index >= len(pq):
        return None
    else:
        return index


def get_left_child(pq, index):
    """returns index, value"""
    left_child_index = 2*index+1
    return get_child(pq, left_child_index)


def get_right_child(pq, index):
    right_child_index = 2*index+2
    return get_child(pq, right_child_index)


def _right_child_index(index):
    return 2*index+2


def compare(v1, v2, comparator=lambda x,y: x < y) -> bool:
    if v1 is None or v2 is None:
        return False
    else:
        return comparator(v1, v2)


def get_smallest_child(pq, index):
    left = get_left_child(pq, index)
    right = get_right_child(pq, index)
    if left is None:
        return None
    elif right is None:
        return left
    elif compare(pq[left], pq[right]):
        return left
    else:
        return right


def top(pq):
    return pq[0]


def swap(pq, i, j):
    pq[i], pq[j] = pq[j], pq[i]


def pop(pq):
    result = pq[0]

    current_index = 0
    pq[0] = pq.pop(-1)  # this is built-in list pop

    smallest_child = get_smallest_child(pq, current_index)

    while smallest_child is not None and not compare(pq[current_index], pq[smallest_child]):
        swap(pq, current_index, smallest_child)
        current_index = smallest_child
        smallest_child = get_smallest_child(pq, current_index)

    return result


def insert(pq, value):
    pq.append(value)
    current_index = len(pq)-1
    parent = get_parent(pq, current_index)

    while parent is not None and compare(pq[current_index], pq[parent]):
        swap(pq, current_index, parent)
        current_index = parent
        parent = get_parent(pq, current_index)


def from_list(lst):
    pq = []

    for e in lst:
        insert(pq, e)

    return pq

