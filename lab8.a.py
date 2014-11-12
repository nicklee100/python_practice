#Nicholas Lee
#11/10/14
#Lab 8

l =[1,2,2,3,4,4]

def makeGrid(n):
    l = list()
    for i in range(n):
        l.append([])
        for j in range(n):
            l[i].append(0)
    return l

print(makeGrid(3))

l = makeGrid(4)

def printGrid(n):
    for i in l:
        print(i)

printGrid(4)        


l =[1,2,2,3,4,4]


def allDifferent1D(l):
    for i in l:
        print(l.count(i))
        if l.count(i) > 1:
                return False
    return True        

print(allDifferent1D(l))


def alldifferent2D(l):
    for i in range(len(l)):
        y=[]
        x=i
        for j in l:
            y.append(j[x])
        if(allDifferent1D(y)==False):
            return False
    for i in l:
        y=i
        if(allDifferent1D(y)==False):
            return False
    print("fj")
    return True

l=[[1,2],[3,4]]
x=alldifferent2D(l)
print(x)

m = [[1,2],[1,0],[3,4],[4,3],[5,5],[0,9]]

def exploreTriplets():
    s=set()

    a=0
    b=[]

    for i in range(10):
        c=[i]
        for p in range(10):
            d=[i]
            e=c+d
            sume=0
            for j in t:
                sume+=j
                s.add(sume)
        print(sume)
        l.append(sume)
        i+=1
    x=dict()
    for i in s:
        x[i]=0
        for j in l:
            sumM=0
            for k in j:
                sumM+-k
        x=d[sumM]
    maxi1 = 0
    maxi2 = 0

    for i in s:
        if x[i]>maxi1:
                maxi2 = i
                maxi1 = x[i]
    for i in l:
        sum2=0
        for j in i:
            sum2+=j
        if sum2==maxi2:
            print(i)
                
