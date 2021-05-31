k = 10
n = 100
x2 = 0
num = [8,8,10,9,12,8,10,14,10,11]
for i in range(0, k):
    x2 += (num[i] - n/k)**2
x2 = k/n * x2
print(x2)
#el x2 hay que compararlo con otro x2 con k-1 gl
#si x2>x2(k-1) entonces se rechaza, o sea, no provienen de una distribucion uniforme
#si x2(k-1)>x2 entonces si provienen de una distribucion uniforme