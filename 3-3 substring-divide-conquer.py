def subString(str, lo, hi):
    if (lo==hi and str[lo] != 'A') or lo>hi:
        return 0.0
    if lo==hi and str[lo] == 'A':
        return 1.0
    mid = (lo+hi)//2
    return subString(str, lo, mid) + subString(str, mid+1, hi) 


string = input('Enter your strings here: ')
n = len(string)
visited = set()
result = subString(string, 0, n-1)
print((result*(result+1))/2)