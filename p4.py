def gen_mixto(a, c, x0, m):
    #mostrara 20 numeros
    print("Generador Mixto")
    for i in range(1,21):
        x=(a*x0+c)%m
        print("Num"+str(i)+": "+str(x))
        x0=x

def gen_mult(a, x0, m):# En el multiplicativo c=0
    #mostrara 20 numeros
    print("Generador Multiplicativo")
    for i in range(1,21):
        x=(a*x0)%m
        print("Num"+str(i)+": "+str(x))
        x0=x

gen_mixto(5, 7, 4, 8)
gen_mult(3, 51, 100)
