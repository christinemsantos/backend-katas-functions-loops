#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    """Add two integers. Handles negative values."""
    sum = x + y
    return sum
print add(2,3)

def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    result = 0
    for a in range(abs(y)):
        result = add(x,result)
    if y < 0 :
        return -result
    else:
        return result
print multiply(6,-8)

def power(x, n):
    """Raise x to power n, where n >= 0"""
    result = 1
    for b in range(n):
        result = multiply(x,result)
    return result
print power(2,8)


def factorial(x):
    """Compute factorial of x, where x > 0"""
    result = 1
    for c in range(2,add(x,1)):
        result = multiply(c,result)
    return result
print factorial(4)


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    d, e = 0, 1
    for _ in range(1,n):
        d, e = e, add(d,e)
    return e
print fibonacci(8)

if __name__ == '__main__':
    # your code to call functions above
    pass
