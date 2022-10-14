def subString(str,i):

    if i == n:
        return
  
    for j in range(i, n):
        if (str[i] == 'A' and str[j] == 'A' ):
            global result
            result += 1

    return subString(str, i+1)


string = input('Enter your strings here: ')
n = len(string)
visited = set()
result = 0
subString(string,0)
print(result)