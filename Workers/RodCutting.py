# Function to find best way to cut a rod of length n
# where rod of length i has a cost price[i-1]
def RodCutting(price, n):

    # T[i] stores maximum profit achieved from rod of length i
    T = [0] * (n + 1)

    # consider rod of length i
    for i in range(1, n + 1):
        # divide the rod of length i into two rods of length j
        # and i-j each and take maximum
        for j in range(1, i + 1):
            T[i] = max(T[i], price[j - 1] + T[i - j])

    # T[n] stores maximum profit achieved from rod of length n
    return T[n]


def RodCuttingReader():
    lines = []
    mainlines = []
    for i in range(1, 3):
        file1 = open("../ProblemH/" + str(i) + ".txt", 'r')
        for line in file1:
            items = line.rstrip('\r\n').split('\t')
            items = [item.strip() for item in items
                     ]  # strip extra whitespace off data items
            lines.append(items)
        mainlines.append(lines)
        lines = []
    return mainlines


def Calculate(price, n):

    RodCutting(price, n)