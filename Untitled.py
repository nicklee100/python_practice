
def triangleUp(n):

    if n == 0:     #base case
        return
        
    else:
        triangleUp(n-1)
        print("triangleUp"+str(n))
        print(n*("*"))

triangleUp(5)
