# Function to find the most efficient way to multiply
# given sequence of matrices
def MatrixChainMultiplication(dims, i, j):

    # base case: one matrix
    if j <= i + 1:
        return 0

    # stores minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix M[i+1]...M[j] = M[i..j]
    min = float('inf')

    # take the minimum over each possible position at which the
    # sequence of matrices can be split
    """
        (M[i+1]) x (M[i+2]..................M[j])
        (M[i+1]M[i+2]) x (M[i+3.............M[j])
        ...
        ...
        (M[i+1]M[i+2]............M[j-1]) x (M[j])
    """

    for k in range(i + 1, j):

        # recur for M[i+1]..M[k] to get an i x k matrix
        cost = MatrixChainMultiplication(dims, i, k)

        # recur for M[k+1]..M[j] to get a k x j matrix
        cost += MatrixChainMultiplication(dims, k, j)

        # cost to multiply two (i x k) and (k x j) matrix
        cost += dims[i] * dims[k] * dims[j]

        if cost < min:
            min = cost

    # return min cost to multiply M[j+1]..M[j]
    return min


# Driver program to test above function
lines = []
input_array = []
file1 = open("1.txt", 'r')
for line in file1:
    items = line.rstrip('\r\n').split('\t')
    items = [item.strip()
             for item in items]  # strip extra whitespace off data items
    lines.append(items)
file1 = open("2.txt", 'r')
for line in file1:
    items = line.rstrip('\r\n').split('\t')
    items = [item.strip()
             for item in items]  # strip extra whitespace off data items
    lines.append(items)
# file1 = open("3.txt", 'r')
# for line in file1:
#     items = line.rstrip('\r\n').split('\t')
#     items = [item.strip()
#              for item in items]  # strip extra whitespace off data items
#     lines.append(items)

for i in range(0, len(lines)):

    data = lines[i][0].split()
    for i in range(0, len(data)):
        data[i] = int(data[i])
    print("\n")
    print(data)
    print("Minimum Cost Of Multiplication Is",
          MatrixChainMultiplication(data, 0,
                                    len(data) - 1))
