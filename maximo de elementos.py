def tira(lista):
    return lista.pop()

#maximo de elementos é 5
def coloca(lista,v):

    if(len(lista) < 5):
        lista.append(v)
        return "FOI POSSIVEL COLOCAR"
    else:
        return "NAO FOI POSSIVEL COLOCAR"

def topo(lista):
    return lista[len(lista)-1]

def Vazia(lista):
    if(len(lista) == 0):
        return True
    return False


lista = [1,2,3,4,5]

print(coloca(lista,1))
