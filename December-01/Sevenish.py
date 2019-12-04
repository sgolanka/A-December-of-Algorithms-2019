# ---> Find a sevenish (power of 7 or sum of powers of 7) number <--- #
import json
sums = []
powers_of_seven = []
ishes = []
# Prints sums of all subsets of arr[l..r]
def subsetSums(arr, start, end, sum=0):

    # Print current subset
    if start > end:
        #print(sum, end=" ")
        sums.append(sum)
        return

    # Subset including arr[l]
    subsetSums(arr, start + 1, end, sum + arr[start])

    # Subset excluding arr[l]
    subsetSums(arr, start + 1, end, sum)

def find_sevenish(index):
    # ishes = [1, 7, 8, 49, 50, 56]
    #powers_of_seven = []
    if len(ishes) > index:
        return ishes[index -1]
    else:
        if index > len(powers_of_seven):
            for i in range(len(powers_of_seven), index):
                powers_of_seven.append(pow(7, i))
            # return powers_of_seven
            subsetSums(powers_of_seven, 0, len(powers_of_seven) - 1)

    for num in sums:
        if num > 0 and num not in ishes:
            ishes.append(num)
    ishes.sort()
    return ishes[index - 1]

# pws = [1, 7, 49]
# with open('txt/power_file.txt', 'w') as sums_file:
#     json.dump(pws, sums_file)

# load previously created lists
with open('txt/sums_file.txt', 'r') as sums_file:
    sums = json.load(sums_file)

with open('txt/power_file.txt', 'r') as powers_file:
    powers_of_seven = json.load(powers_file)

with open('txt/ishes.txt', 'r') as ishes_file:
    ishes = json.load(ishes_file)

#make sure ishes is updated
if len(ishes) < len(powers_of_seven) + len(sums):
    for num in powers_of_seven:
        if num not in ishes:
            ishes.append(num)
    for num in sums:
        if num not in ishes:
            ishes.append(num)
    ishes.sort()
    with open('txt/ishes.txt', 'w') as ishes_file:
        json.dump(ishes, ishes_file)




user_input = int(input('Which sevenish number are you interested in?'))
ish = find_sevenish(user_input)
print('{} is the sevenish number at the {} position.'.format(ish, user_input))
