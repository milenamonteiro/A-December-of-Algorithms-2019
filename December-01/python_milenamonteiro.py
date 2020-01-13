def sevenish_number(num):
    pow = 1
    answer = 0
    while num:
        if num & 1:
            answer += pow
        num >>= 1 # if 0 stops the loop
        pow = pow*7 # next
    print(answer)

# inputs
sevenish_number(1)
sevenish_number(5)
sevenish_number(10)
