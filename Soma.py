def tira(lista):
    return lista.pop()

def coloca(lista,v):
    return lista.append(v)

def topo(lista):
    return lista[len(lista)-1]

def Vazia(lista):
    if(len(lista) == 0):
        return True
    return False

def soma(lista):

    soma = 0

    while(not Vazia(lista)):
        soma += topo(lista)
        tira(lista)

    return soma

lista = [1,2,3,4,5]

#soma e tira os elementos
print(soma(lista))

print(Vazia(lista))
