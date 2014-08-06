counter_num1 = []
counter_num2 = []
sum_list = []
def russian_alg(num1, num2):
    while int(num1) >=1:
        num1 = num1 / 2
        if num1 < 1:
            pass
        else:
            counter_num1.append(int(num1))
    c = len(counter_num1)
    print(c)
    while c > 0:
        num2 = num2 * 2
        counter_num2.append(num2)
        c -= 1
    print(counter_num2)
    for i in counter_num1:
        if int(i) % 2 == 1:
            print(int(i))
            cn1 = counter_num1.index(i)
            sum_list.append(counter_num2[cn1])
    return sum(sum_list)
print(russian_alg(238,13))

print(238*13)