a=sorted([0]+[int(l.strip())for l in open("data/day10.txt").readlines()])
a+=[a[-1]+3]
d,b=a[-1],[y-x for x,y in zip(a,a[1:])]

# [0, 1, 2, 3, 6, 9, 10, 11, 12, 15, 16, 17, 20, 23, 26, 27, 28, 29, 30, 33, 34, 35, 36, 39, 40, 41, 42, 43, 46, 47, 48, 49, 52, 53, 54, 55, 58, 61, 62, 63, 64, 67, 68, 71, 72, 73, 74, 77, 78, 79, 80, 81, 84, 85, 86, 87, 88, 91, 92, 93, 96, 97, 98, 101, 102, 103, 104, 107, 108, 109, 110, 111, 114, 115, 116, 117, 120, 123, 126, 129, 132, 133, 134, 135, 136, 139, 142, 145, 146, 147, 148, 151, 154, 155, 156, 157, 158, 161]

from itertools import product
G,g={},[(x,y) for x,y in product(a,a) if 1<=(y-x)<=3]
for x,y in g: G.setdefault(x,[]).append(y)

# {0: [1, 2, 3], 1: [2, 3], 2: [3], 3: [6], 6: [9], 9: [10, 11, 12], 10: [11, 12], 11: [12], 12: [15], 15: [16, 17], 16: [17], 17: [20], 20: [23], 23: [26], 26: [27, 28, 29], 27: [28, 29, 30], 28: [29, 30], 29: [30], 30: [33], 33: [34, 35, 36], 34: [35, 36], 35: [36], 36: [39], 39: [40, 41, 42], 40: [41, 42, 43], 41: [42, 43], 42: [43], 43: [46], 46: [47, 48, 49], 47: [48, 49], 48: [49], 49: [52], 52: [53, 54, 55], 53: [54, 55], 54: [55], 55: [58], 58: [61], 61: [62, 63, 64], 62: [63, 64], 63: [64], 64: [67], 67: [68], 68: [71], 71: [72, 73, 74], 72: [73, 74], 73: [74], 74: [77], 77: [78, 79, 80], 78: [79, 80, 81], 79: [80, 81], 80: [81], 81: [84], 84: [85, 86, 87], 85: [86, 87, 88], 86: [87, 88], 87: [88], 88: [91], 91: [92, 93], 92: [93], 93: [96], 96: [97, 98], 97: [98], 98: [101], 101: [102, 103, 104], 102: [103, 104], 103: [104], 104: [107], 107: [108, 109, 110], 108: [109, 110, 111], 109: [110, 111], 110: [111], 111: [114], 114: [115, 116, 117], 115: [116, 117], 116: [117], 117: [120], 120: [123], 123: [126], 126: [129], 129: [132], 132: [133, 134, 135], 133: [134, 135, 136], 134: [135, 136], 135: [136], 136: [139], 139: [142], 142: [145], 145: [146, 147, 148], 146: [147, 148], 147: [148], 148: [151], 151: [154], 154: [155, 156, 157], 155: [156, 157, 158], 156: [157, 158], 157: [158], 158: [161]}

from functools import lru_cache
@lru_cache(maxsize=2**16)
def rec(x): return 1 if x==161 else sum(rec(y) for y in G[x])
print(b.count(1)*b.count(3), rec(0))
