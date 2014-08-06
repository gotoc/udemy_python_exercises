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
# Initial steps: create empty arrays to hold the two lists
counter_num1 = []
counter_num2 = []
# Build a function to take two numbers as arguments
def russian_alg(num1, num2):
    # Since we care for whole numbers, I set the num1 value as an int() and
    # loop through it as long as it's 1 or greater.
    while int(num1) >=1:
        # This is step 2 above, it is the division by 2
        num1 = num1 / 2
        # if we go below 1, we ignore the result
        if num1 < 1:
            pass
        else:
        # we add teh result to the first list (counter_num1)
            counter_num1.append(int(num1))
    # very important we get the length of that list above. That is how many times we multiply
    # the second value:
    c = len(counter_num1)
    while c > 0:
        # while c is greater then 0 we multiple the value (num2) by 2
        # then I add it to our second list (counter_num2)
        # and subtract the value of c by 1 after reach calculation
        num2 = num2 * 2
        counter_num2.append(num2)
        c -= 1
    # Next we need to know the index of any even number in list 1 (counter_num1)
    for i in counter_num1:
        # I check if it's divisible by 2
        if int(i) % 2 == 0:
            # I grab the index of that number that's divisible by 2 (even number)
            cn1 = counter_num1.index(i)
            # Since our list's have matching lengths, I can delete the same index on the other list
            del counter_num2[cn1]
    # Finally, I print the result of summing each index in our second list (counter_num2)
    print(sum(counter_num2))
# Supplying numbers into the algorithm:
russian_alg(238,13)

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