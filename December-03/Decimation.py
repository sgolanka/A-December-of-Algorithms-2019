# ----> decimate a list (keep removing half until sorted)

sorted_list = [1, 2, 3, 4, 5, 6]
unsorted_list = [3, 5, 6, 2, 1, 4, 8, 0, 14, -1, 88]
unsorted_list_with_dups = [1, 2, 3, 4, 5, 3, 4, 5, 2, 1, 8, 3, 5]

def decimate(d):
    # ----> these two lines are used for both versions
    s_list = d[:] # creates a copy of the list
    s_list.sort()

    # ----> non-recursive way (it works)
    while s_list != d:
        half = int(len(d)/2)
        d = d[half:]
        s_list = d[:]
        s_list.sort()
    return d

    # ---> recursive attempt (only works for pre-sorted lists)
    # if d == s_list:
    #     print('equal')
    #     print('working{}'.format(d))
    #     return d
    # else:
    #     # remove second half
    #     half = int(len(d)/2)
    #     decimate(d[half:])



print('First list = {}'.format(sorted_list))
print('After decimating: {}'.format(decimate(sorted_list)))
print()
print('Second list = {}'.format(unsorted_list))
print('After decimating: {}'.format(decimate(unsorted_list)))
print()
print('Third list = {}'.format(unsorted_list_with_dups))
print('After decimating: {}'.format(decimate(unsorted_list_with_dups)))
