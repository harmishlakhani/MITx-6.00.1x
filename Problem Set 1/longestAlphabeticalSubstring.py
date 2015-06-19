s = raw_input("Enter String. ")

length = len(s) - 1
count = 0
maxStart = 0
maxEnd = 0

for i in range(length):
    j = i
    while (j < length and s[j] <= s[j + 1]):
        j = j + 1
    if (i != j):
        if ((j - i) > (maxEnd - maxStart)):
            maxStart = i
            maxEnd = j
        i = j + 1

print("Longest substring in alphabetical order is: " + s[maxStart:maxEnd + 1])