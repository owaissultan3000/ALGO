# Function to determine if can be segmented into a space-separated
# sequence of one or more dictionary words
def WordBreak(dict, stri, lookup):

    # n stores length of current substring
    n = len(stri)

    # return true if we have reached the end of the String
    if n == 0:
        return True

    # if sub-problem is seen for the first time
    if lookup[n] == -1:

        # mark sub-problem as seen (0 initially assuming String
        # can't be segmented)
        lookup[n] = 0

        for i in range(1, n + 1):
            # consider all prefixes of current String
            prefix = stri[:i]

            # if prefix is found in dictionary, then recur for suffix
            if prefix in dict and WordBreak(dict, stri[i:], lookup):
                # return true if the can be segmented
                lookup[n] = 1
                return True

    # return solution to current sub-problem
    return lookup[n] == 1


def WordBreakReader():
    lines = []
    for i in range(1, 4):
        file1 = open("../ProblemJ/" + str(i) + ".txt", 'r')
        for line in file1:
            items = line.rstrip('\r\n').split('\t')
            items = [item.strip() for item in items
                     ]  # strip extra whitespace off data items
            lines.append(items)

    return lines


def Calculate(lines, stri, lookup):

    WordBreak(lines, stri, lookup)