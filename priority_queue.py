import math


def get_parent(index):
    if index == 0:
        return None
    else:
        return math.floor((index-1)/2)


def get_child(index):
    if index > len(index):
        return None, None
    else:
        return index


def get_left_child(index):
    """returns index, value"""
    left_child_index = 2*index+1
    return get_child(left_child_index)


def get_right_child(pq, index):
    right_child_index = 2*index+2
    return get_child(right_child_index)


def compare(v1, v2, comparator=lambda x,y: x < y):
    if v2 is None:
        return False
    elif v1 is None:
        return True
    else:
        return comparator(v1, v2)


def get_smallest_child(pq, index):
    left = get_left_child(pq, index)
    right = get_right_child(pq, index)
    if left is None:
        return None
    elif right is None:
        return right
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
    pq[0] = pq.pop(-1)

    smallest_child = get_smallest_child(pq, current_index)

    while smallest_child is not None and compare(pq[current_index], pq[smallest_child]):
        swap(pq, current_index, smallest_child)
        current_index = smallest_child
        smallest_child = get_smallest_child(pq, current_index)

    return result


def insert(pq, value):
    pq.append(value)
    current_index = len(pq)-1
    parent = get_parent(current_index)

    while parent is not None and compare(pq, pq[current_index], pq[parent]):
        swap(pq, current_index, parent)
        current_index = parent
        parent = get_parent(current_index)


def from_list(lst):
    pq = []

    for e in lst:
        insert(pq, e)

    