'''
Count the number of ways to reach the nth stair starting from the bottom given that you can take only 1, 2 or 3 steps at a time.
Before moving on to the solution, please try to think about the question practically and make sure you understand the problem well.


           _4_
        _2_|
     _1_|
 _1_|

COMMON AMAZON QUESTION

'''
def stairCase(stepNum):
    #at the 0th step there is only one way to get there which is to step on it so there is 1 way to get there
    numOfWaysAtStep=[1]
    if stepNum == 0 :
        return 1
    currentStepValue=0
    for x in range(1,stepNum):
        '''
        to get to each step we can get there from the last three steps, 
        so the total is how many ways can we get from the last 3 steps added together 
        '''
        currentStepValue=0
        if (x - 2) >= 0:
            currentStepValue+=numOfWaysAtStep[x-2]
        if (x - 3) >= 0:
            currentStepValue+=numOfWaysAtStep[x-3]
        currentStepValue+=numOfWaysAtStep[x-1]
        numOfWaysAtStep.append(currentStepValue)

    return numOfWaysAtStep

#change as you like
stairCase(0)
