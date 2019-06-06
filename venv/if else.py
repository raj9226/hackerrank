N=int(input())
j=N%2
if j!=0:
    print("weired")
elif N in range(2,6) and j ==0:
    print("not weired")
elif N in range(6,21) and j ==0:
    print("weired")
elif N in range(20,101) and j ==0:
    
    print("not weired")
