#ingresar datos
x=True
x=0
x=1
def datos():
    x=True
    while x <1000:
        x=x+1
        print(x)
        if x==100:
            if x==200:
            continuar=input("desea seguir con el conteo:")
            if continuar.lower()=="si":
               datos()
            elif continuar.lower()=="no":
               x=False
               print("****************************")
               print("finalizar programa")
datos()
  
