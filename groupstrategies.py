# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING
import random
    

# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split,steal"),("split,split"),("steal,split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 
"""
So we always steal on the first round in an attempt to get some early points.
then based on their results change up our strategy.
if more steals then we we have a 70% chance of stealing, 
if the other is true then we have 70% chance of splitting.
if they are equao then its a 50% chance.
"""
def hereticalharbringersstrat1(history):
    if len(history) == 1:
        return "steal"
    countsteal = 0
    countsplit = 0
    for i in history:
        (me, them)  = i
        if them == "split":
            countsplit += 1 
        elif them == "steal":
            countsteal += 1
    if countsteal > countsplit:
        roll = random.randint(1, 10)
        if roll <= 7:
            return "steal"
        else:
            return "split"
    elif countsplit > countsteal:
        roll = random.randint(1,10)
        if roll <= 7:
            return "split"
        else:
            return "steal"
    else:
        roll = random.choice(["split", "steal"])
        return(roll)


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# We split the first three times
# after the first three wegenerate the fib sequence
# if the number of times we've done this is equal a number in the fibonachi sequence
# then we steal
def hereticalharbringersstrat3(history):
    if len(history) <= 3:
        return "split"
    fibnums = []
    for n in range(200):
        num1 = 0
        num2 = 1
        next_num = num2
        num1, num2 = num2, next_num
        next_num = num1 + num2
        fibnums.append(next_num)
    for i in history:
        num1 = 0
        num2 = 1
        fibnums.append(next_num)
        if i in fibnums:
            return("steal")
        else:
            roll = random.randint(1, 10)
            if roll <= 8:
                return "steal"
            else:
                return "split"
print(hereticalharbringersstrat3(hist4))