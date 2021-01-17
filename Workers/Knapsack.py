# Input:
# Values (stored in list v)
# Weights (stored in list w)
# Number of distinct items (n)
# Knapsack capacity (W)
def KnapSack(v, w, W):

    # T[i][j] stores the maximum value of knapsack having weight less
    # than equal to j with only first i items considered.
    T = [[0 for x in range(W + 1)] for y in range(len(v) + 1)]

    # do for ith item
    for i in range(1, len(v) + 1):

        # consider all weights from 0 to maximum capacity W
        for j in range(W + 1):

            # don't include ith element if j-w[i-1] is negative
            if w[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                # find maximum value we get by excluding or including the ith item
                T[i][j] = max(T[i - 1][j], T[i - 1][j - w[i - 1]] + v[i - 1])

    # return maximum value
    return T[len(v)][W]


def KnapSackReader():
    lines = []
    mainlines = []
    for i in range(1, 11):
        file1 = open("../ProblemF/" + str(i) + ".txt", 'r')
        for line in file1:
            items = line.rstrip('\r\n').split('\t')
            items = [item.strip() for item in items
                     ]  # strip extra whitespace off data items
            lines.append(items)
        mainlines.append(lines)
        lines = []
    return mainlines


def Calculate(v, w, W):

    KnapSack(v, w, W)