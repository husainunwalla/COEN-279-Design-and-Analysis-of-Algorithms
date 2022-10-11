def subString(str,i,j):

    if (i>j):
        return 0 
 
    res = subString(str, i + 1, j) + subString(str, i, j - 1)   
    
    if (str[i] == 'A' and str[j] == 'A' and (i,j) not in visited):
        print(string[i:j+1])
        visited.add((i,j))
        res += 1
 
    return res

string = input('Enter your strings here: ')
n = len(string)
visited = set()

print(subString(string, 0, n-1))

