T = int(input())

for t in range (T):
    var = [int(s) for s in input().split() if s.isdigit()]
    N = var[0]  # How many stacks of plates there are
    K = var[1]  # How many plates in each stack
    P = var[2]  # Number of plates needed

    stack = {}
    for n in range (N):
        stack["string{0}".format(n)] = [int(s) for s in input().split() if s.isdigit()]
        print(stack["string{0}".format(n)])
    
    # print ("Case #" + str(t + 1) + ": " + str(TODO))