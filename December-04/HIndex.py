# ---->  Find H Index <----#

# A researcher has index h if at least h of his N papers have h citations each.
# If there are multiple h satisfying this formula, the maximum is chosen.

citation_list1 = [4, 3, 0, 1, 5]
citation_list2 = [4, 5, 2, 0, 6, 4]
citation_list3 = [7, 8, 9, 10, 11, 12, 13]


def h_index(c):
    h = 0
    determined = False

    # ---> in case list is empty or only contains 0
    if len(c) < 1 or (len(c) == 1 and c[0] < 1):
        determined = True

    # ---->start at max possible value (each paper has at least as many citations as the total number of papers)
    cites = len(c)
    matches = 0

    # ----> loop through list counting the times there are enough citations,
    # lowering citations needed until we find the highest h index
    while not determined:
        for num in c:
            if num >= cites:
                matches +=1
        if matches == cites:
            h = matches
            determined = True
        else:
            cites -= 1
            matches = 0

    return h


print('List 0: {}'.format([]))
print('h index: {}'.format(h_index([])))
print()
print('List 1: {}'.format(citation_list1))
print('h index: {}'.format(h_index(citation_list1)))
print()
print('List 2: {}'.format(citation_list2))
print('h index: {}'.format(h_index(citation_list2)))
print()
print('List 3: {}'.format(citation_list3))
print('h index: {}'.format(h_index(citation_list3)))

