from itertools import product
from functools import lru_cache
m=[[None if c == "." else False for c in line.strip()] for line in open("data/day11.txt").readlines()]
mx,my=len(m[0]),len(m)
def M(m): return "\n".join("".join("." if c==None else "#" if c else "L" for c in l) for l in m)
@lru_cache(maxsize=mx*my)
def neighbouring(x,y): return tuple([(x+i,y+j) for i,j in product((-1,0,1),(-1,0,1)) if 0<=x+i<mx and 0<=y+j<my and (i,j)!=(0,0)])
def neighbours(x,y): return [p[yj][xi] for xi,yj in neighbouring(x,y)]
@lru_cache(maxsize=mx*my)
def firsts_from(x,y):
  return [t for t in map(lambda g: next(g,None), [((xi,y) for xi in range(x+1,mx) if p[y][xi] != None), ((xi,y) for xi in reversed(range(x)) if p[y][xi] != None), ((x,yj) for yj in range(y+1,my) if p[yj][x] != None), ((x,yj) for yj in reversed(range(y)) if p[yj][x] != None), ((xi,yi) for xi,yi in zip(range(x+1,mx),range(y+1,my)) if p[yi][xi] != None), ((xi,yi) for xi,yi in zip(reversed(range(x)),reversed(range(y))) if p[yi][xi] != None), ((xi,yi) for xi,yi in zip(range(x+1,mx),reversed(range(y))) if p[yi][xi] != None), ((xi,yi) for xi,yi in zip(reversed(range(x)),range(y+1,my)) if p[yi][xi] != None)]) if t!=None]
def sees(x,y): return [p[yi][xi] for xi,yi in firsts_from(x,y)]
from copy import deepcopy
P,p=deepcopy(m),None
while m!=p:
  p=deepcopy(m)
  for y,row in enumerate(m):
    for x,s in enumerate(row):
      if s==False and neighbours(x,y).count(True)==0:
        m[y][x]=True
      elif s and neighbours(x,y).count(True)>=4:
        m[y][x]=False
m,P,p=P,m,None
while m!=p:
  p=deepcopy(m)
  for y,row in enumerate(m):
    for x,s in enumerate(row):
      if s==False and sees(x,y).count(True)==0:
        m[y][x]=True
      elif s and sees(x,y).count(True)>=5:
        m[y][x]=False
print(M(P).count("#"), M(m).count("#"))