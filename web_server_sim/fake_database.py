import time
# CACHE = {}

def russian_alg(num1, num2):
    # key = (num1,num2) # this is for the cache
    # if key in CACHE: # checking if we have the argument cached already
    #     sum_list = CACHE[key] # if it's in the CACHE we just pull it without calcuating it
    #     return sum_list
    # else:
        print("...calculating...")
        counter_num1 = []
        counter_num2 = []
        sum_list = []
        while int(num1) >=1:
            num1 = num1 / 2
            if num1 < 1:
                pass
            else:
                counter_num1.append(int(num1))
        c = len(counter_num1)
        while c > 0:
            num2 = num2 * 2
            counter_num2.append(num2)
            c -= 1
        for i in counter_num1:
            if int(i) % 2 == 1:
                cn1 = counter_num1.index(i)
                sum_list.append(counter_num2[cn1])
                z = sum(sum_list)
                # CACHE[key] = z
                # print(z)
        return z

def test_russian_perf():
    start_time = time.time()
    print(russian_alg(24,16))
    print("My Russian Peasant took: %f seconds to calculate" % (time.time()-start_time))

if __name__ == "__main__":
    test_russian_perf()