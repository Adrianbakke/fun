import math

def swap(ix1,ix2,xs):
    xs = list(xs)
    x1,x2 = xs[ix1],xs[ix2]
    xs[ix1],xs[ix2] = x2,x1
    return ''.join(xs)

def getindw(sx):
    return sx.find('w')

def checksum(cs, c):
    return ((cs*243)+c) % 100000007

def calcCheckSum(sx):
    sx = list(sx)
    a = 0
    for s in sx: a = checksum(a, ord(s))
    return a 

def possibleMoves(v):
    dim = int(math.sqrt(len(v)))
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
    tmpQ = possibleMoves(start_v)
    results = []
    discovered = set()
    while not results:
        Q,tmpQ,disc = tmpQ,[],[]
        for q in Q:
            if q[0] == goal:
                results.append(q[1])
                continue
            newmoves = possibleMoves(q[0])
            for nm in newmoves:
                if not nm[0] in discovered:
                    disc.append(nm[0])
                    path = q[1] + nm[1]
                    tmpQ.append([nm[0], path])
        for d in disc: discovered.add(d)
    return results

dim = int(input(""))
a = []
b = []
for x in range(dim):
    a.append(input(""))
for x in range(dim):
    b.append(input(""))

a = ''.join(a)
b = ''.join(b)

#a = 'aaaaaaaabwbbbbbb'
#b = 'bbbbbwbbaaaaaaaa'
#a = "bbbbwrrrr"
#b = "rbrbwbrbr"

res = bfg(a.lower(),b.lower())
print(res)
print(sum([calcCheckSum(r) for r in res])%100000007)

