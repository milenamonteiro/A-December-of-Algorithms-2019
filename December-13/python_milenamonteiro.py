from math import sqrt

def switches(n):
    bulbs = ["off"]*n
    count = 1
    
    def toggle(bulbs=bulbs):
        if bulbs[count - 1] == "off": bulbs[count - 1] = "on"
        else: bulbs[count - 1] = "off"
    
    def on_switches(n):
        return int(sqrt(n))
    
    for x in range(n + 1):
        print("Interaction {} = {}".format(x, bulbs))
        if count == n:
            toggle()
        else:
            for i in range(count - 1, n, count):
                toggle()
            count += 1
            
    print("No of switches in the 'on' state at the end: {}".format(on_switches(n)))
