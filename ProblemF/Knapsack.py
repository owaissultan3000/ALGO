# Input:
# Values (stored in list v)
# Weights (stored in list w)
# Number of distinct items (n)
# Knapsack capacity (W)
def knapSack(v, w, W):

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


fileslist = [
    "1.txt",
    "2.txt",
    "3.txt",
]
lines = []
for i in range(0, 2):

    file1 = open(fileslist[i], 'r')
    for line in file1:
        items = line.rstrip('\r\n').split('\t')
        items = [item.strip()
                 for item in items]  # strip extra whitespace off data items
        lines.append(items)
print(lines)

# print("Knapsack value is", knapSack(v, w, W))