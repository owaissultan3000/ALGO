# Dynamic programming Python implementation
# of LIS problem


# lis returns length of the longest
# increasing subsequence in arr of size n
def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Initialize maximum to 0 to get
    # the maximum of all LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


# end of lis function

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
file1 = open("3.txt", 'r')
for line in file1:
    items = line.rstrip('\r\n').split('\t')
    items = [item.strip()
             for item in items]  # strip extra whitespace off data items
    lines.append(items)

for i in range(0, len(lines)):

    data = lines[i][0].split()
    for i in range(0, len(data)):
        data[i] = int(data[i])
    print(data)
    print("Length of Longest Increasing SubSequence Is", lis(data))
    print("\n")
