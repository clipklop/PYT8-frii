"""
    * Merge sort
"""


lst_to_sort = [3, 6, 4, 3, 5, 1, 9, 2]


def merge_lst(l1, l2):
    l1_idx = 0
    l2_idx = 0
    new_lst = []
    while True:
        if l1_idx == len(l1):
            new_lst.extend(l2[l2_idx:])
            break
        if l2_idx == len(l2):
            new_lst.extend(l1[l1_idx:])
            break
        if l1[l1_idx] < l2[l2_idx]:
            new_lst.append(l1[l1_idx])
            l1_idx += 1
        else:
            new_lst.append(l2[l2_idx])
            l2_idx += 1
    return new_lst


def sort_lst(lst):
    if len(lst) == 1:
        return lst
    else:
        lst_l = sort_lst(lst[0:len(lst) // 2])
        lst_r = sort_lst(lst[len(lst) // 2:])
        return merge_lst(lst_l, lst_r)


print(sort_lst(lst_to_sort))
