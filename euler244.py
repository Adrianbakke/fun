import numpy as np

up,down,left,right=[ord(x) for x in ['U','D','L','R']]

def swap(ix1,ix2,xs):
    xs = list(xs)
    x1,x2 = xs[ix1],xs[ix2]
    xs[ix1],xs[ix2] = x2,x1
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

def move(cond, dim, indw, v, direct, moves):
    if cond:
        check = calcCheckSum(swap(indw,indw+dim,v))
        moves.append([check, ])
    return moves

def possibleMoves(v):
    dim = int(np.sqrt(len(v)))
    indw = getindw(v)
    wcoord = (indw//dim, indw%dim)
    moves = []
    moves = move(wcoord[0] < (dim-1), dim, indw, v, up, moves) #up
    moves = move(wcoord[0] > 0, dim, indw, v, down, moves) #down
    moves = move(wcoord[1] < (dim-1), dim, indw, v, left, moves) #left
    moves = move(wcoord[1] > 0, dim, indw, v, right, moves) #right
    return moves

def bfg(start_v, goal):
    Q = possibleMoves(start_v)
    discovered = set()
    while Q:
        if (v[0] == goal):
            return v
        for v in vert:
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

goal = calcCheckSum(b)
bfg(a,b)
