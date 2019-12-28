"""
Luhn Algorithm
"""

def luhn_test(card):
    def get_digits(n):
        return [int(d) for d in str(n)]
    digits = get_digits(card)
    odd = digits[-1::-2]
    even = digits[-2::-2]
    print
    checksum = 0
    checksum += sum(odd)
    for digit in even:
        checksum += sum(get_digits(digit * 2))
    if checksum % 10 == 0:
        return card + "is valid"
    else:
        return card + "isn't valid"
