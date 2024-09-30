import random

nAleatorio = int(random.randint(0,100))
Palpites = []

while (True):
    nUsuario = int(input("Buta um número de 0 a 100: "))
    Palpites.append(nUsuario)

    if (nUsuario == nAleatorio):
        print("Acertou miseravi !!!")
        break
    elif (nUsuario>nAleatorio):
        print ("Vc colocou um número Maior ! Sua Anta ")
        continue
    print ("Vc colocou um número Menor ! Sua Anta")

print (len (Palpites))

    

