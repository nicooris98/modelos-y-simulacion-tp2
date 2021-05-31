#Kolmogorov-Smirnov
num = [0.53,0.35,0.03,0.94,0.22]
print(num)
num.sort()
print(num)
dn = 0
dnMax = 0
for i in range(0,len(num)):
    dn = ((i+1)/len(num))-num[i]
    #print("dn: "+str(dn)+" - dnMax: "+str(dnMax))
    if dn>dnMax:
        dnMax = dn
print(dnMax)
#Si dnMax<d entonces no se puede rechazar la hipótesis de que 
#los números generados provienen de una distribución uniforme
#, osea, si se cumple que dnMax<d provienen de distribucion uniforme(se acepta)