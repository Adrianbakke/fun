import numpy as np

up,down,left,right=[ord(x) for x in ['U','D','L','R']]

def swap(ix1,ix2,xs):
    xs = list(xs)
    x1,x2 = xs[ix1],xs[ix2]
    xs[ix1],xs[ix2] = x2,x1
    return ''.join(xs)

def getindw(sx):
    return sx.find('w')

def checksum(checksum, c):
    return (checksum*243+c) % 100000007

def calcCheckSum(sx):
    sx = list(sx)
    a = 0
    for s in sx: a += checksum(a, s)
    return a

def move(cond, swap, indw, v, direct, moves):
    if cond:
        # check = calcCheckSum(swap(indw,indw+dim,v))
        moves.append([swap(indw,indw+swap,v), direct])
    return moves

def possibleMoves(v):
    dim = int(np.sqrt(len(v)))
    indw = getindw(v)
    wcoord = (indw//dim, indw%dim)
    moves = []
    if wcoord[0] < (dim-1):
        moves.append([swap(indw,indw+dim,v), 'U'])
    if wcoord[0] > 0:
        moves.append([swap(indw,indw-dim,v), 'D'])
    if wcoord[1] < (dim-1):
        moves.append([swap(indw,indw+1,v), 'L'])
    if wcoord[1] > 0:
        moves.append([swap(indw,indw-1,v), 'R'])
    return moves

def bfg(start_v, goal):
    Q = possibleMoves(start_v)
    q = Q
    results = []
    discovered = set()
    while Q:
        Q = q
        q = []
        for v in Q:
            if v[0] == goal:
                results.append(v)
                continue
            newmoves = possibleMoves(v[0])
            for nm in newmoves:
                if not nm[0] in discovered:
                    discovered.add(nm[0])
                    path = v[1] + nm[1]
                    q.append([nm[0], path])
        if results: return results

#dim = int(input(""))
#a = []
#b = []
#for x in range(dim):
#    a.append(list(input("")))
#for x in range(dim):
#    b.append(list(input("")))
#
#print(bfg(a,b))

a = "aaaaaaaabwbbbbbb"
b = "bbbbbwbbaaaaaaaa"

#a = "awbb"
#b= "abwb"

#goal = calcCheckSum(b)
print(bfg(a,b))
