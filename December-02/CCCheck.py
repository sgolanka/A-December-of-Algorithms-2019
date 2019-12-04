# --->  Check for valid Credit Card Number <--- #
"""
Algorithm:
Reverse the order of the digits in the number.

Take the first, third, ... and every other odd digit in the reversed digits and sum them to form the partial sum s1

Taking the second, fourth ... and every other even digit in the reversed digits:
    Multiply each digit by two and sum the digits if the answer
    is greater than nine to form partial sums for the even digits
    Sum the partial sums of the even digits to form s2

If s1 + s2 ends in zero then the original number is in the form of a
valid credit card number as verified by the Luhn test.
"""

# ----> get number as string
card_str = input('Please enter your Credit Card Number')
credit_num_list = []

# ---> convert string to list of integers
for chr_num in card_str:
    credit_num_list.append(int(chr_num))

    # ---> reverse the digits
    credit_num_rev_list = credit_num_list[-1::-1]

# ---> sum the "odd" digits (odd if we started counting with 1, but we don't)
odd_sum = 0
for i in range(len(credit_num_rev_list)):
    if i % 2 == 0:  # <---- even index nums for odd digits
        odd_sum += credit_num_rev_list[i]

# ----> double the "even" digits
even_list = []
even_sum = 0
for i in range(len(credit_num_rev_list)):
    if i % 2 != 0:  # <---- odd index nums for even digits
        even_list.append(2 * credit_num_rev_list[i])

# ----> sum digits of doubled evens
for i in range(len(even_list)):
    if even_list[i] > 9:
        first_digit = int(even_list[i] / 10)
        second_digit = even_list[i] % 10
        even_list[i] = first_digit + second_digit

# ----> get total of (doubled) even list
for num in even_list:
    even_sum += num

# ----> sum of 2 totals should end in 0:
if (odd_sum + even_sum) % 10 == 0:
    print('{} is a valid number.'.format(card_str))
else:
    print('{} is fake!!!'.format(card_str))
