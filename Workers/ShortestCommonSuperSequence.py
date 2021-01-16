import sys

fileslist = [
    "1.txt",
    "2.txt",
    "3.txt",
]


def ShortestCommonSequence(str1, str2):
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


def ShortestCommonSequenceReader():
    lines = []
    for i in range(1, 4):
        file1 = open("../ProblemB/" + str(i) + ".txt", 'r')
        for line in file1:
            items = line.rstrip('\r\n').split('\t')
            items = [item.strip() for item in items
                     ]  # strip extra whitespace off data items
            lines.append(items)

    return lines


def Calculate(lines):

    ShortestCommonSequence(lines[0], lines[1])