import re

from functools import reduce
from itertools import product


def diffs(a, b):
    return (p[0] - p[1] for p in zip(a, b))


def distance_sq(a, b):
    return sum(d**2 for d in diffs(a, b))


def distance(a, b):
    return distance_sq(a, b)**0.5


def ints(line):
    pattern = re.compile(r'-?\d+')

    return [int(val) for val in re.findall(pattern, line) if val]


def manhattan(a, b):
    return sum(abs(d) for d in diffs(a, b))


def neighs(y, x):
    return ((y-1,x), (y+1,x), (y,x-1), (y,x+1))


def neighs_bounded(y, x, rmin, rmax, cmin, cmax):
    return tuple([n for n in neighs(y, x) if rmin <= n[0] <= rmax and cmin <= n[1] <= cmax])


def eight_neighs(y, x):
    return tuple([(y+dy, x+dx) for dy in range(-1, 2) for dx in range(-1, 2) if dy != 0 or dx != 0])


def eight_neighs_bounded(y, x, rmin, rmax, cmin, cmax):
    return tuple([n for n in eight_neighs(y, x) if rmin <= n[0] <= rmax and cmin <= n[1] <= cmax])


def grouped_lines(lines):
    groups = []
    group = []

    for line in lines:
        if not line.strip():
            groups.append(group)
            group = []
        else:
            group.append(line.rstrip())

    if group:
        groups.append(group)

    return groups


def n_neighs(point):
    n = len(point)

    for delta in product(range(-1, 2), repeat=n):
        if any(val != 0 for val in delta):
            yield tuple((point[i] + delta[i] for i in range(n)))


def multall(nums):
    return reduce(lambda a,b: a*b, nums)


def hexneighs(r, c):
    neighs = { (r, c+1), (r, c-1), (r-1, c), (r+1, c) }

    if r % 2:
        neighs |= { (r+1, c-1), (r-1, c-1) }
    else:
        neighs |= { (r+1, c+1), (r-1, c+1) }

    return neighs


def columns(matrix):
    return [[line[x] for line in matrix] for x in range(len(matrix[0]))]


def digits(line):
    pattern = re.compile(r'\d?')

    return [int(val) for val in re.findall(pattern, line) if val]


def chunks(l, n):
    for x in range(0, len(l), n):
        yield l[x:x+n]


def chunks_with_overlap(l, n):
    for x in range(n, len(l)+1):
        yield l[x-n:x]


def positives(line):
    return list(map(abs, ints(line)))


def rays(grid, y, x):
    return [
     [grid[y][dx] for dx in range(x)],
     [grid[y][dx] for dx in range(x+1, len(grid[0]))],
     [grid[dy][x] for dy in range(y)],
     [grid[dy][x] for dy in range(y+1, len(grid))]
    ]


def rays_from_inside(grid, y, x):
    return [
     [grid[y][dx] for dx in range(x)][::-1],
     [grid[y][dx] for dx in range(x+1, len(grid[0]))],
     [grid[dy][x] for dy in range(y)][::-1],
     [grid[dy][x] for dy in range(y+1, len(grid))]
    ]


def adjacent(a, b):
    return manhattan(a, b) == 1


def words(line):
    pattern = re.compile(r'[a-zA-Z]+')

    return [word for word in re.findall(pattern, line)]


def between(point, a, b, strictly_different=True):
    if strictly_different:
        return a < point < b or b < point < a
    
    return a <= point <= b or b <= point <= a


def overlap(a, b):
    return between(a[0], *b, False) or between(a[1], *b, False) or between(b[0], *a, False) or between(b[1], *a, False)


def dimensions(grid):
    return len(grid), len(grid[0])


def sum_of_differences(l):
    return sum((l[i] - l[i-1]) * (len(l) - i) * i for i in range(1, len(l)))