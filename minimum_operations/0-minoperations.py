#!/usr/bin/python3

"""
Given number n, writing a method that calculates the fewest num of operations.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    if n <= 1:
        return 0

    i = 2
    while i * i <= n:
        if n % i == 0:
            return i + minOperations(n // i)
        i += 1

    return n
