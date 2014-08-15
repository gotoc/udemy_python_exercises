import itertools
from web_server_sim import computer1, computer2, computer3
#
# s = ['APP1','APP2','APP3','APP4','APP5','APP6','APP7']
n = -1
SERVERS = [computer1, computer2, computer3]
cycle = itertools.cycle(SERVERS)
def get_server():
    global n
    n += 1
    return SERVERS[n % len(SERVERS)]
    # global cycle
    # return next(cycle)

if __name__ == '__main__':
    from random import randint
    for i in range(10):
        z = randint(1,3)
        num1 = [44,85,123][z%3]  #this picks a random num from 1-3 and grabs the spec val
        num2 = [54,15,32][z%3]
        # print(get_server())
        print("Num1: " + str(num1) +" Num2: "+ str(num2))
        server = get_server()
        print(server.printName())
        server.multiplyHandler(num1,num2)
        print(server.multiplyHandler(num1,num2))
        print(server.lastMultipledHandler())
        print(" ")

