
'''
Homework 3.1  COEN 279
Using exhaustive search to count substrings starting and ending with "A"
We check the starting and ending character of each possible substring.
'''

string = input('Enter your strings here: ')
result = 0
n = len(string)

for i in range(n):
    for j in range(i, n):
        if string[i] == 'A' and string[j] == 'A':
            result += 1
print (result)
