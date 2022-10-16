def merge_two(a, b):
    (m, n) = (len(a), len(b))
    i = j = 0
 
    # Result Array
    d = []
 
    # Merge the two
    while i < m and j < n:
        if a[i] <= b[j]:
            d.append(a[i])
            i += 1
        else:
            d.append(b[j])
            j += 1
 
    # Add a if b is shorter
    while i < m:
        d.append(a[i])
        i += 1
 
    # Add b if a is shorter
    while j < n:
        d.append(b[j])
        j += 1
 
    return d
 
 
def merge(a, b, c):
    # Merge first two, then third
    t = merge_two(a, b)
    return merge_two(t, c)

a = [10, 11, 12, 1, 3, 5, 2, 7, 8]
lo, i, j, hi = 0, 3, 6, 8
print(merge(a[lo:i], a[i:j], a[j:hi+1]))