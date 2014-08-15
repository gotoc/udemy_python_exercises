from web_server_sim import fake_database

CACHE = {}
def printName():
    print(str(__name__))

def lastMultipledHandler():
    if CACHE:

        return CACHE

def multiplyHandler(num1,num2):
    key = (num1,num2) # this is for the cache
    if key in CACHE: # checking if we have the argument cached already
        print("...found in cache...")
        # sum_list = CACHE[key] # if it's in the CACHE we just pull it without calcuating it
        return CACHE[key]
    else:
        result = fake_database.russian_alg(num1,num2)
        CACHE[key] = result
        return result

# print(multiplyHandler(24,16))
# print(multiplyHandler(99,16))
# print(multiplyHandler(42,16))
# print(multiplyHandler(24,16))
# print(multiplyHandler(2,16))
# print(multiplyHandler(43,16))
# print(multiplyHandler(23,16))
# print(multiplyHandler(76,16))
#
# print(lastMultipledHandler())