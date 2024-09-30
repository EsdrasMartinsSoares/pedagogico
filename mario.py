def Maior_Valor(vetor):
    if (len(vetor) == 0):
        return None

    maior= vetor[0]

    for i in range (1, len(vetor)):
        if vetor[i]> maior :
            maior = vetor[i] 
        
    return maior 

bosta = [1,15,8,16]

print (Maior_Valor(bosta))
