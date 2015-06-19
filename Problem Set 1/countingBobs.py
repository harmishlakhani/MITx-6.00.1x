s = raw_input("Enter String. ")

length = len(s)
length =  length - 2
count = 0

for i in range(length ):
    j = i + 3 
    temp = s[i:j]
    if temp == 'bob':
        count = count + 1
print("Number of times bob occurs is: " + str(count))