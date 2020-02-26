def uniqueStairs(num_steps):#Can be done recursively FIBONACHI SEQUENCE
    unique_ways = 0
    if num_steps == 1:
        return 1
    if num_steps == 2:
        return 2
    n1_step = 1
    n_step = 2
    for unique_ways in range(num_steps-2):
        unique_ways = n1_step + n_step
        n1_step = n_step
        n_step = unique_ways
    return unique_ways


def multipleSteps(num_steps, X):
    temp_steps = num_steps
    for step in x:




step_array = [1,3,5]
multipleSteps(5, step_array)
for x in range(7):
    print("" +str(x)+" UNIQUE WAYS STEPS: "+str(uniqueStairs(x)))



