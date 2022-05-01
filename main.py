N = 6
i = N

def Multipliers(N,i):
    if(i>0):
        print(N//i)
        i-=1
        Multipliers(N,i)

Multipliers(N,i)