def h_index(n, citations):
    return max([min(n - i, c) for i, c in enumerate(sorted(citations))])
