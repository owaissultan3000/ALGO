import sys
# Function to return a SCS of substrings X[0..m-1], Y[0..n-1]
def ShortestCommonSuperSequence(X, Y, m, n, T):
 
    # if we have reached the end of first string,
    # return second string
    if m == 0:
        return Y[:n]
 
    # if we have reached the end of second string,
    # return first string
    if n == 0:
        return X[:m]
 
    # if last character of X and Y matches, then include it in SSC
    # and recur to find SCS of substring X[0..m-2], Y[0..n-1]
    if X[m - 1] == Y[n - 1]:
        return ShortestCommonSuperSequence(X, Y, m - 1, n - 1, T) + X[m - 1]
    else:
        # if the last character of X and Y don't match
 
        # if top cell of current cell has less value than the left
        # cell, then include current character of X in SCS
        # and find SCS of substring X[0..m-2], Y[0..n-2]
 
        if T[m - 1][n] < T[m][n - 1]:
            return ShortestCommonSuperSequence(X, Y, m - 1, n, T) + X[m - 1]
 
        # if left cell of current cell has less value than the top
        # cell, then include current character of Y in SCS
        # and find SCS of substring X[0..m-1], Y[0..n-2]
        else:
            return ShortestCommonSuperSequence(X, Y, m, n - 1, T) + Y[n - 1]
 
 
# Function to fill lookup table by finding length of SCS of
# sequences X[0..m-1] and Y[0..n-1]
def SCSLength(X, Y, m, n, T):
 
    # initialize first column of the lookup table
    for i in range(m + 1):
        T[i][0] = i
 
    # initialize first row of the lookup table
    for j in range(n + 1):
        T[0][j] = j
 
    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # else if current character of X and Y don't match
            else:
                T[i][j] = min(T[i - 1][j] + 1, T[i][j - 1] + 1)
 
 

lines=[]
fname=sys.argv[1]
file1=open(fname,'r')
for line in file1:
    line = line.strip()
    lines.append(line)

for i in range(0,len(lines),2):
    S1=lines[i]
    S2=lines[i+1]
    m = len(S1)
    n = len(S2)

    # lookup table stores solution to already computed sub-problems
    # T[i][j] stores the length of SCS of substring X[0..i-1], Y[0..j-1]
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
 
    # fill lookup table in bottom-up manner
    SCSLength(S1, S2, m, n, T)
    print("\n")
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("Shortest Common Super Sequence: " + ShortestCommonSuperSequence(S1,S2, m, n, T))
    
