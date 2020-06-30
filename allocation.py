T = int(input())

for i in range (T):
    house = 0
    b = [int(s) for s in input().split() if s.isdigit()]
    c = [int(s) for s in input().split() if s.isdigit()]

    c.sort()

    for j in range (b[0]):
        b[1] -= c[j]
        if (b[1] >= 0):
            house += 1

    print ("Case #" + str(i + 1) + ": " + str(house))