import sys


# Function to find lcs_algo
def LongestCommonSubsequence(S1, S2, m, n):
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Building the mtrix in bottom-up way
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index = L[m][n]

    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i - 1] == S2[j - 1]:
            lcs_algo[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Printing the sub sequences

    print("S1 : " + S1 + "\nS2 : " + S2)
    print("Lenght Of Longest Common SubSequence:", len(lcs_algo) - 1)
    print("Longest Common SubSequence: " + "".join(lcs_algo))

    #storing file data in a list


lines = []

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

file1 = open("3.txt", 'r')
for line in file1:
    items = line.rstrip('\r\n').split('\t')
    items = [item.strip()
             for item in items]  # strip extra whitespace off data items
    lines.append(items)

for i in range(0, len(lines)):
    data = lines[i][0].split()
    S1 = data[0]
    S2 = data[1]
    m = len(S1)
    n = len(S2)
    LongestCommonSubsequence(S1, S2, m, n)
