def wordplay(s):
    score_a = 0
    score_b = 0
    for x in range(len(s)):
        for i in range(len(s)+1):
            if s[x:i]:
                if s[x:i][0] in "aeiou":
                    score_a += 1
                else:
                    score_b += 1
    if score_b > score_a:
        print("The winner is B with {} points!".format(score_b))
    else:
        print("The winner is A with {} points!".format(score_a))
