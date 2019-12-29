"""
Tipsie, a cookie store sells cookies in jars. Each jar has one cookie in them. The store gives a free cookie if
the customer returns enough cookie jars. For example, if a customer Alex has n=15 to spend on jars of cookie that
cost p=3 each. He can turn in c=2 cookie jars to receive another cookie.

Initially, he buys 5 cookies and has 5 jars after eating them. He turns in 4 of them, leaving him with 1, for 2 more
cookies. After eating those two, he has 3 cookie jars, turns in 2 leaving him with 1 cookie jar and his new cookie.
Once he eats that one, he has 2 cookie jars and turns them in for another cookie. After eating that one, he only has
1 cookie, and his shopping ends. Overall, he has eaten 5+2+1+1=9 cookies. The integers n, p and c represent money to
spend, cost of a cookie, and the number of cookie jars he can turn in for a free cookie respectively.

Implement a function cookieCount(n, p, c) to count the number of cookies Alex could buy.
"""


def cookie_count(n, p, c):
    """
    Returns the number of cookies it is possible to purchase, starting with n dollars, @ p dollars per cookie
    OR c jars per cookie returned, where each cookie is inside one jar when purchased

    :param n: a number representing the starting dollars
    :param p: a number representing the price per cookie in dollars
    :param c: a number representing the price per cookie in returned jars
    :return: the total number of cookies that could be purchased

    """
    jars = 0
    num_cookies = 0

    while (n >= p) or (jars >= c):
        # purchase max, trade in max for each round
        new_cookies = int(n / p + jars / c)
        num_cookies += new_cookies
        # dollars now equal to remainder after  purchase
        n = n % p
        # jars now equal to remainder after trade in
        jars = jars % c
        # increase jars by number of cookies purchased this round
        jars += new_cookies

    return num_cookies


print('Max cookies @ $2 or 5 jars each, starting with $10.: {}.'.format(cookie_count(10, 2, 5)))
#  6
print('Max cookies @ $4 or 4 jars each, starting with $12.: {}.'.format(cookie_count(12, 4, 4)))
#  3
print('Max cookies @ $3 or 2 jars each, starting with $15.: {}.'.format(cookie_count(15, 3, 2)))
#  9
