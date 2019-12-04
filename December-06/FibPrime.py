# ----> Find the Nth Fibonacci Prime number

# This code is based on code by Saket Modi
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        return -1
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

    # Driver Program


print(Fibonacci(9))

# Program to check if a number is prime or not
# based on code found here: https://www.programiz.com/python-programming/examples/prime-number
# num = 407
# To take input from the user
# num = int(input("Enter a number: "))
# prime numbers are greater than 1

def prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # print(num, "is not a prime number")
                # print(i, "times", num // i, "is", num)
                return False
        else:
            print(num, "is a prime number")
        return True

    # if input number is less than
    # or equal to 1, it is not prime
    # print(num, "is not a prime number")
    return False

user_input = int(input("What Fib Prime do you want to find?"))
num_primes = 0
nth_fib = 1

while num_primes < user_input:
    x = Fibonacci(nth_fib)
    if prime(x):
        num_primes += 1
    nth_fib += 1

print("{} is the Nth prime fib when N = {}.".format(x, user_input))



