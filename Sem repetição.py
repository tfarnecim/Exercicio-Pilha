def tira(lista):
    return lista.pop()

def coloca(lista,v):

    for i in range(len(lista)):
        if(lista[i] == v):
            return "NAO FOI POSSIVEL COLOCAR"

    return lista.append(v)

def topo(lista):
    return lista[len(lista)-1]

def Vazia(lista):
    if(len(lista) == 0):
        return True
    return False


lista = [1]

print(coloca(lista,1))
