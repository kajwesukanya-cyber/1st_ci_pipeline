
def rotate_list(items, k):
    if len(items) == 0:
        return []

    n = len(items)
    k = k % n

    if k == 0:
        return items.copy()

    return items[-k:] + items[:-k]
