def switches(n):
    bulbs = ["off" for i in range(n)]
    
    count = 1
    for x in range(n):
        print(bulbs)
        for i in range(n):
            if i % count == 0:
                if bulbs[i] == "off": bulbs[i] = "on"
                else: bulbs[i] = "off"
        count += 1

switches(5)