#Codigo para saber si 2 numeros son primos relativos
#Primos relativos son 2 numeros que no tienen nigun factor 
#en comun aparte del 1 o -1
#Ej: 15 y 28 son coprimos
#los factores de 15 (1,3,5,15), y los de 28 (1,2,4,7,14,28) 
#no tienen nada en común (excepto el 1).
def coprimo(num1, num2):
    anum1=[1]
    anum2=[1]
    for i in range (2, num1+1):
        #print("i num 1: "+str(i))
        if num1%i==0:
            anum1.append(i)
    for i in range (2, num2+1):
        #print("i num 2: "+str(i))
        if num2%i==0:
            anum2.append(i)
    print("Factores del numero 1")
    print(anum1)
    print("Factores del numero 2")
    print(anum2)
    repetido=False
    for i in range(1, len(anum1)):
        for j in range(1, len(anum2)):
            #print("anum1: "+str(anum1[i]))
            #print("anum2: "+str(anum2[j]))
            if anum1[i]==anum2[j]:
                repetido=True
    if repetido:
        print("El numero "+str(num1)+" y el numero "+str(num2)+" NO son coprimos")
    else:
        print("El numero "+str(num1)+" y el numero "+str(num2)+" SI son coprimos")

coprimo(21, 22)    