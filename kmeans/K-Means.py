import random
import math

K = []
kx = []
ky = []

file = open('TrainsetTugas2.txt','r')
trainset =  file.readlines()
print(len(trainset))

def determineK(value):
    for k in range (value):
        rand = random.randint(1,688)
        print('hasil random:',rand)
        tmp = trainset[rand].split()
        print(trainset[rand])
        K.append(tmp)

n = 4
determineK(n)

for x in range (n):
    print('x:',x)
    kx.append(K[x][0])
    ky.append(K[x][1])
    print('kx',kx[x],'\tky',ky[x],'\n')

centA = [kx[0],ky[0]]
centB = [kx[1],ky[1]]
centC = [kx[2],ky[2]]
centD = [kx[3],ky[3]]

def euclideDist(x,y,x1,y1):
    x = float(x)
    y = float(y)
    x1 = float(x1)
    y1 = float(y1)
    dist = math.sqrt((math.pow((x-x1),2) + math.pow((y-y1),2)))
    return dist

clusA = []
clusB = []
clusC = []
clusD = []

iteration = True
iterValue = 1
while (iteration == True):
    clusA = []
    clusB = []
    clusC = []
    clusD = []
    print('iterasi:',iterValue)
    for m in range (len(trainset)):
        d = trainset[m].split()
        x1 = d[0]
        y1 = d[1]

        #print('vector:',x1,y1)

        x=centA[0]
        y=centA[1]

        tmA = euclideDist(x, y, x1, y1)
        #print('distance ClustA',tmA)

        x = centB[0]
        y = centB[1]

        tmB = euclideDist(x, y, x1, y1)
        #print('distance ClustB', tmB)

        x = centC[0]
        y = centC[1]

        tmC = euclideDist(x, y, x1, y1)
        #print('distance ClustC', tmC)

        x = centD[0]
        y = centD[1]

        tmD = euclideDist(x, y, x1, y1)
        # print('distance ClustC', tmC)

        if tmA<tmB and tmA<tmC and tmA < tmD:
            clusA.append(d)
        if tmB<tmA and tmB<tmC and tmB < tmD:
            clusB.append(d)
        if tmC<tmB and tmC<tmA and tmC < tmD:
            clusC.append(d)
        if tmD<tmB and tmD<tmA and tmD < tmC:
            clusD.append(d)

    print('total:',len(clusA),len(clusB),len(clusC),len(clusD))

    #update centroid
    px,qx,rx,sx = 0,0,0,0
    py,qy,ry,sy = 0,0,0,0
    for x in range (len(clusA)):
        px += float(clusA[x][0])
        py += float(clusA[x][1])

    for x in range (len(clusB)):
        qx += float(clusB[x][0])
        qy += float(clusB[x][1])

    for x in range (len(clusC)):
        rx += float(clusC[x][0])
        ry += float(clusC[x][1])

    for x in range (len(clusD)):
        sx += float(clusD[x][0])
        sy += float(clusD[x][1])

    pxS = px/len(clusA)
    pxS = round(pxS, 3)
    pyS = py/len(clusA)
    pyS = round(pyS, 3)

    qxS = qx/len(clusB)
    qxS = round(qxS, 3)
    qyS = qy/len(clusB)
    qyS = round(qyS, 3)

    rxS = rx/len(clusC)
    rxS = round(rxS, 3)
    ryS = ry/len(clusC)
    ryS = round(ryS, 3)

    sxS = sx / len(clusD)
    sxS = round(sxS, 3)
    syS = sy / len(clusD)
    syS = round(syS, 3)

    newcentA = [pxS, pyS]
    newcentB = [qxS, qyS]
    newcentC = [rxS, ryS]
    newcentD = [sxS, syS]


    print('old centA', centA)
    print('old centB', centB)
    print('old centC', centC)

    print('new centA',newcentA)
    print('new centB',newcentB)
    print('new centC',newcentC)

    print('total:',len(clusA)+len(clusB)+len(clusC)+len(clusD))


    if (newcentA == centA) & (newcentB == centB) & (newcentC == centC):
        iteration = False
    else:
        centA = newcentA
        centB = newcentB
        centC = newcentC
        centD = newcentD
        iterValue +=1


print('---Final---\n centroid A:',centA,'centroid B:',centB,'centrod C:',centC,'centrod D:',centD)

file = open('TestsetTugas2.txt','r')
testSet =  file.readlines()
rfile = open('Result Testset.txt','w')

memberA, memberB, memberC, memberD = 0,0,0,0

for s in range (len(testSet)):
    t = trainset[s].split()
    x1 = t[0]
    y1 = t[1]

    # print('vector:',x1,y1)

    x = centA[0]
    y = centA[1]

    tmA = euclideDist(x, y, x1, y1)
    # print('distance ClustA',tmA)

    x = centB[0]
    y = centB[1]

    tmB = euclideDist(x, y, x1, y1)
    # print('distance ClustB', tmB)

    x = centC[0]
    y = centC[1]

    tmC = euclideDist(x, y, x1, y1)
    # print('distance ClustC', tmC)

    if tmA < tmB and tmA < tmC and tmA < tmD:
        memberA += 1
        rfile.write(str(x1)+'\t' + str(y1)+'\t'+'Cluster Code: X021')
    if tmB < tmA and tmB < tmC and tmB < tmD:
        memberB += 1
        rfile.write(str(x1) + '\t' + str(y1) + '\t' + 'Cluster Code: G750')
    if tmC < tmB and tmC < tmA and tmC < tmD:
        memberC += 1
        rfile.write(str(x1) + '\t' + str(y1) + '\t' + 'Cluster Code: F10K')
    if tmD < tmB and tmD < tmA and tmD < tmC:
        memberD +=1
        rfile.write(str(x1) + '\t' + str(y1) + '\t' + 'Cluster Code: R309')
    rfile.write('\n')

print('member A:',memberA,'\n','member B:',memberB,'\n','member C',memberC,'\n','member D',memberD)