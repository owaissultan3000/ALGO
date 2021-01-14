# Function to find Levenshtein Distance between X and Y
# m and n are the number of characters in X and Y respectively
def dist(X, m, Y, n):

    # base case: empty strings (case 1)
    if m == 0:
        return n

    if n == 0:
        return m

    # if last characters of the strings match (case 2)
    cost = 0 if (X[m - 1] == Y[n - 1]) else 1

    return min(
        dist(X, m - 1, Y, n) + 1,  # deletion (case 3a))
        dist(X, m, Y, n - 1) + 1,  # insertion (case 3b))
        dist(X, m - 1, Y, n - 1) + cost)  # substitution (case 2 + 3c)


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

    print("S1 : " + S1 + "\nS2 : " + S2)
    print("The Levenshtein Distance (Edit-Distance) Is:", dist(S1, m, S2, n))
