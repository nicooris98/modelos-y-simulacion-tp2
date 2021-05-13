def gen_congruencial(a, m, x0, c=0):# En multiplicativo c=0
    #mostrara 20 numeros
    if c==0:
        print("Generador Multiplicativo")
    else:
        print("Generador Mixto")
    for i in range(1,21):
        x=(a*x0+c)%m
        print("Num"+str(i)+": "+str(x))
        x0=x

gen_congruencial(5, 8, 4, 7)
gen_congruencial(3, 100, 51)