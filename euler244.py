import numpy as np

def swap(ix1,ix2,xs):
    xs = list(xs)
    x1 = xs[ix1]
    x2 = xs[ix2]
    xs[ix1] = x2
    xs[ix2] = x1
    print(str(xs))
    return str(xs)

def getindw(sx):
    return sx.find('w')

def checksum(checksum, c):
    return (checksum*243+c) % 100000007

def calcCheckSum(sx):
    sx = list(sx)
    a = 0
    for s in sx: a += checksum(a, s)
    return a

def possibleMoves(v):
    dim = int(np.sqrt(len(v)))
    indw = getindw(v)
    wcoord = (indw//dim, indw%dim)
    moves = []
    if wcoord[0] < (dim-1):
        check = calcCheckSum(swap(indw,indw+dim,v))
        moves.append([check, 'U'])
    if wcoord[0] > 0:
        check = calcCheckSum(swap(indw,indw-dim,v))
        moves.append([check, 'D'])
    if wcoord[1] < (dim-1):
        check = calcCheckSum(swap(indw,indw+1,v))
        moves.append([check, 'L'])
    if wcoord[1] > 0:
        check = calcCheckSum(swap(indw,indw-1,v))
        moves.append([check, 'R'])
    return moves

def bfg(start_v, goal):
    Q = possibleMoves(start_v)
    discovered = set()
    while Q:
        v = Q.pop(0)
        if (v[0] == goal):
            return v
        adjEdges = possibleMoves(v[0])
        for o in adjEdges:
            if not o[0] in discovered:
                discovered.add(o[0])
                path = v[1] + o[1]
                Q.append([o[0], path])

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

bfg(a,b)
