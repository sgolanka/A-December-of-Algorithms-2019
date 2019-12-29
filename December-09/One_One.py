"""In mathematics a one to one function is that which has a unique element in the range for every corresponding
domain. Let there be a function f: X->Y such that if a,b belong to X and if f(a)=f(b) then a=b. This proves the one
to one property of a function. If there exists more than one "X's" for the same "Y's" then the function is not one to
one. Your task is to write a program that accepts two sets of numbers and the relationship between them and evaluate
if they are indeed a one-one function. """

import operator


def get_operator_fn(o):
    """
    Convert a String to a mathematical operator (could extend this
    to all operators in the "operator" library)
    :param o: a string contanining a mathematical operator
    :return: the operator in the form 'operator.xxx" where xxx is the operator
    """
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.mul,
        '%': operator.mod
    }[o]


def one_one_function(set_1, set_2, relationship):
    """
    Determine if 'relationship' is a one-one function between set_1 and set_2
    :param set_1: A list of numbers
    :param set_2: A list of numbers represenging the output of a function applied to the elements of set_1
    :param relationship: A String representation of the mathematical operator
    :return: True if one-one function, False otherwise
    """
    one_1 = True
    op = get_operator_fn(relationship)

    # list(set(list_parameter)) <--- this nested function call converts list_parameter
    # to a set which can only contain unique elements, then converts back to a list
    uniq_list = (list(set(set_2)))
    uniq_list.sort()
    results = set_2[:]
    results.sort()
    if len(set_1) == len(set_2) and uniq_list == results:
        # check that each element in set_2 is the result of the function applied to each element in set_1
        for i in range(len(set_1)):
            if op(set_1[i], set_1[i]) != set_2[i]:
                one_1 = False
                break
    else:  # if the two sets are unequal or each element in set_2 is not unique
        one_1 = False

    return one_1


# s_1 = [1, 2, 3, 4]
s_1 = [1, -1, 2, -2, 3, -3, 4, -4]
# s_2 = [1, 4, 9,16]
s_2 = [2, -2, 4, -4, 6, -6, 8, -8]
# f = '**'
f = "+"

if one_one_function(s_1, s_2, f):
    print('{} is a one-one function between {} and {}.'.format(f, s_1, s_2))
else:
    print('{} is NOT a one-one function between {} and {}.'.format(f, s_1, s_2))
