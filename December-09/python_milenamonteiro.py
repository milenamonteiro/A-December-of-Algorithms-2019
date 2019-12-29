def one_one(s1, s2):
    def p(x):
        return x*2 # function

    if all(s2[i] == p(x) for i, x in enumerate(s1)):
        print("It's one-one")
    else:
        print("It's not one-one")
