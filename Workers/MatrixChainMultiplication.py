# Function to find the most efficient way to multiply
# given sequence of matrices
def MatrixChainMultiplication(dims):

    n = len(dims)

    # c[i,j] = minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix M[i]M[i+1]...M[j] = M[i..j]
    # The cost is zero when multiplying one matrix
    c = [[0 for x in range(n + 1)] for y in range((n + 1))]

    for length in range(2, n + 1):  # Subsequence lengths

        for i in range(1, n - length + 2):

            j = i + length - 1
            c[i][j] = float('inf')

            k = i
            while j < n and k <= j - 1:
                cost = c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j]

                if cost < c[i][j]:
                    c[i][j] = cost

                k = k + 1

    return c[1][n - 1]


# Driver program to test above function
def MatrixChainMultiplicationReader():
    lines = []
    for i in range(1, 3):
        file1 = open("../ProblemE/" + str(i) + ".txt", 'r')
        for line in file1:
            items = line.rstrip('\r\n').split('\t')
            items = [item.strip() for item in items
                     ]  # strip extra whitespace off data items
            lines.append(items)

    return lines


def Calculate(lines):

    MatrixChainMultiplication(lines)