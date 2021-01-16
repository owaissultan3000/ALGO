# Function to find Levenshtein Distance between X and Y
# m and n are the number of characters in X and Y respectively
fileslist = [
    "1.txt",
    "2.txt",
    "3.txt",
]


def Distance(X, Y):

    (m, n) = (len(X), len(Y))

    # for all i and j, T[i,j] will hold the Levenshtein distance between
    # the first i characters of X and the first j characters of Y
    # note that T has (m+1)*(n+1) values
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]

    # source prefixes can be transformed into empty by
    # dropping all characters
    for i in range(1, m + 1):
        T[i][0] = i  # (case 1)

    # target prefixes can be reached from empty source prefix
    # by inserting every character
    for j in range(1, n + 1):
        T[0][j] = j  # (case 1)

    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):

        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # (case 2)
                cost = 0  # (case 2)
            else:
                cost = 1  # (case 3c)

            T[i][j] = min(
                T[i - 1][j] + 1,  # deletion (case 3b)
                T[i][j - 1] + 1,  # insertion (case 3a)
                T[i - 1][j - 1] + cost)  # replace (case 2 + 3c)

    return T[m][n]


def EditReader():
    lines = []
    for i in range(1, 4):
        file1 = open("../ProblemC/" + str(i) + ".txt", 'r')
        for line in file1:
            items = line.rstrip('\r\n').split('\t')
            items = [item.strip() for item in items
                     ]  # strip extra whitespace off data items
            lines.append(items)

    return lines


def Calculate(lines):

    Distance(lines[0], lines[1])
