inputString = raw_input("Enter String. ")

count = 0
for char in inputString:
    if (char in 'aeiou'):
        count = count + 1
print("Number of vowels: " + str(count))