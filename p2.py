def calcular_cuad_med(semilla):#calcula 20 numeros aleatorios
    print("Numeros aleatorios")
    for i in range(1,21):
        if i!=1:
            semilla=int(num)
        num=semilla**2
        num=str(num)
        if(len(num)<8):
            if(len(num)<7):
                num="00"+num
            else:
                num="0"+num
        num=num[2]+num[3]+num[4]+num[5]
        num01=int(num)/10000
        print("Num"+str(i)+": "+str(num01))

calcular_cuad_med(3708)
