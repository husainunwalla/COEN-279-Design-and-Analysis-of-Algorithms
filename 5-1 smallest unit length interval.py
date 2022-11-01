from cgitb import small
from cmath import inf


def smallest_unit_interval(points):
    points.sort()

    smallest_Set = set()
    end_of_last_interval = float(-inf)
    for p in points:
        if end_of_last_interval <= p:
            interval = (p, p+1)
            smallest_Set.add(interval)
            end_of_last_interval = p + 1

    return smallest_Set

points = input('Enter the points: ').split()
points = [float(x) for x in points]

ans = smallest_unit_interval(points)

print('The smallest unit interval containing the points is: ', ans)