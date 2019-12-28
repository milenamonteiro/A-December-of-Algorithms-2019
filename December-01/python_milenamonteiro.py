"""
A "sevenish" number is a natural number which is either a power of 7, or the sum of unique powers of 7
The first 5 sevenish numbers are: 1, 7, 8, 49, 50.
Now, implement an algorithm to find the nth sevenish number.
"""

def sevenish_number(num):
    pow = 1
    answer = 0
    while num:
        if num & 1:
            answer += pow
        num >>= 1 # if 0 stops the loop
        pow = pow*7 # next
    return answer
