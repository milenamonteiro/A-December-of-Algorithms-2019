def queue(n = int(input("Enter N: "))):
    n 
    queue_list = dict()
    print('Enter token, id: ')
    for i in range(n):
        data = input()
        temp = data.split(', ')
        queue_list[int(temp[0])] = temp[1]
        
    k = int(input("Enter K: "))
    
    print('({}, {})'.format(k, queue_list.get(k)))
    for key, value in queue_list.items():
        if key != k:
            print('{}, {}'.format(key, value))

queue()

"""
Sample input:
    Enter N: 5
    Enter token, id:
    1, a
    2, b
    3, c
    4, d
    5, e
    Enter K: 4
    
Sample output:
    4, d
    1, a
    2, b
    3, c
    5, e
"""