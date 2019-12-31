def sevenish_number(num):
    pow = 1
    answer = 0
    while num:
        if num & 1:
            answer += pow
        num >>= 1 # if 0 stops the loop
        pow = pow*7 # next
    return answer
