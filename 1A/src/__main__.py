import math
import sys

n, m, a = (int(x) for x in sys.stdin.readline().split(' '))
npl = math.ceil(n / a)
mpl = math.ceil(m / a)
print(npl * mpl)
