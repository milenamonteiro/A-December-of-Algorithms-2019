def h_index(n, citations):
    print(max([min(n - i, c) for i, c in enumerate(sorted(citations))]))

# inputs
h_index(5, [4,3,0,1,5])
h_index(6, [4,5,2,0,6,4])
