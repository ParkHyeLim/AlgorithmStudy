i=0
while(True):
    L, P, V = map(int, input().split())
    if(L==0):
        break
    i += 1
    maxDay = (V//P)*L + V%P
    print("Case " +str(i)+":", str(maxDay))
