def thanos(things):
    if things == list(set(things)):
        print(things)
    else:
        del things[0:(len(things)//2)] # removing the last items
        print(things)

# inputs - removing the first half
thanos([1, 2, 3, 4, 5])
thanos([1, 2, 3, 4, 3])
thanos([3, 4, 3])
thanos([4, 3])
thanos([3])
