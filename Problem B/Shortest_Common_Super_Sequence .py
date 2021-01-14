import sys


def shortestCommonSuperDP(str1, str2):
    dp = [[None for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if not i:
                dp[i][j] = j
            elif not j:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    sc_len = dp[len(str1)][len(str2)]
    # for printing purpose
    scstr = [None for _ in range(sc_len)]
    i, j = len(str1), len(str2)

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            scstr[sc_len - 1] = str1[i - 1]
            i -= 1
            j -= 1
            sc_len -= 1

        elif dp[i][j - 1] < dp[i - 1][j]:
            scstr[sc_len - 1] = str2[j - 1]
            j -= 1
            sc_len -= 1
        else:
            scstr[sc_len - 1] = str1[i - 1]
            i -= 1
            sc_len -= 1
    while i > 0:
        scstr[sc_len - 1] = str1[i - 1]
        i -= 1
        sc_len -= 1
    while j > 0:
        scstr[sc_len - 1] = str2[j - 1]
        j -= 1
        sc_len -= 1

    scstr = "".join(map(str, scstr))
    return scstr


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
    result = shortestCommonSuperDP(S1, S2)
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("Lenght Of Shortest Common SuperSequence:", len(result))
    print("Shortest Common Super Sequence: ", result)
