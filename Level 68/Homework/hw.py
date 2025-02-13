

def insert_at_index(lst, index, item):
    lst.insert(index, item)
    return lst



def append_items(lst, items):
    for item in items:
        lst.append(item)
    return lst


def append_lists(lst1, lst2):
    lst1.extend(lst2)
    return lst1
