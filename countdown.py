T = int(input())

for t in range (T):
    countdowns = 0
    kcd = False
    var = [int(s) for s in input().split() if s.isdigit()]
    array = [int(s) for s in input().split() if s.isdigit()]
    N = var[0]  # Numbers in the array
    K = var[1]  # K-countdowns
    for n in range (N):
        if (array[n] == K):
            kcd = True
            for k in range (K):
                if (array[n + k] != (K - k)):
                    kcd = False
                elif (array[n + k] == 1):
                    countdowns += 1
                    kcd = False


    print ("Case #" + str(t + 1) + ": " + str(countdowns))