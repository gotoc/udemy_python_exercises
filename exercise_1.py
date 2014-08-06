'''
Part 1 of Udemy's course on Intermediate Python is to create an algorithm to calculate the result of two
numbers being multiplied together without a times table.  In this code exercise I was given the following information:
1. if we have two numbers
2. the first is divided by 2 until we reach the number 1
3. the second number is multiplied by 2 for the same number of times it took to get to 1 in step #2
4. If we compare our number lists from step #2 and step #3, and omit the even numbered items from list in
step #2.
5. Then remove the corresponding index from the list in step #3.
6. Then we sum the results of the list in step #3
At that point we get the same result as if we multiplied two numbers together.

Example:
238 x 13 = 3094
Results from step 2:      Results from step 3:
119                         26
59                          52
29                          104
14 **                         208 **
7                           416
3                           832
1                           1664
                            -----
Sum (omitting ** values):   3094

Here is my Python solution to accomplish this:
'''
# Moved the 3 lists inside the function. While outside the function if the
# function is called multiple times, it appends results to the
# list.  To avoid this, the lists were moved to the function, so each time the function
# is called the lists are empty from the start.

def russian_alg(num1, num2):
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
    return sum(sum_list)

def test_russian():
    assert russian_alg(24,16) == (24*16)
    assert russian_alg(16,24) == (24*16)
    assert russian_alg(2,50) == (2*50)
    return "All tests have passed for russian_alg()"

print(test_russian())


'''
INSTRUCTORS CODE IS BELOW:  The Udemy course instructor had a much better method of achieving the same result.
He (Jason Elbourne) wrote the following code:
def russian(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1
print(russian(357,16)

His solution is pretty cool.  Very short and sweet and makes use of some features like binary shifting.  He didn't need to use any lists.
Instead he created a while loop. In the loop he checks if X is a odd number.  If it is he sets z = z + his second number.  Then he uses binary shifting
to multiple and divide by 2.  y << 1 being the multiplication by 2 and x >> 1 being the division by 2.  So as x gets smaller (towards 0)
the loop runs and adds z to y (as long as x is an odd number.)

'''