def thanos(things):
    if things == list(set(things)):
        return things
    else:
        del things[0:(len(things)//2)] # removing the last items
        return things
