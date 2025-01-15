def busca_binaria(lista, valor):

    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:

        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return meio
          
        elif lista[meio] > valor:
            fim = meio - 1  

        else:
            inicio = meio + 1 
            
    return -1 

def busca_binaria_recursiva(lista, valor, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
        
    if inicio > fim:
        return -1 
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == valor:
        return meio
    elif lista[meio] > valor:
        return busca_binaria_recursiva(lista, valor, inicio, meio - 1)
    else:
        return busca_binaria_recursiva(lista, valor, meio + 1, fim)

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
valor = 7

resultado_iterativo = busca_binaria(lista, valor)
if resultado_iterativo != -1:
    print(f"Valor {valor} encontrado no índice {resultado_iterativo} (Iterativa).")
else:
    print(f"Valor {valor} não encontrado (Iterativa).")

valor_recursivo = 7
resultado_recursivo = busca_binaria_recursiva(lista, valor_recursivo)
if resultado_recursivo != -1:
    print(f"Valor {valor_recursivo} encontrado no índice {resultado_recursivo} (Recursiva).")
else:
    print(f"Valor {valor_recursivo} não encontrado (Recursiva).")

lista2 = [2, 4, 6, 8, 10, 12, 14, 16]
valor2 = 10

resultado_iterativo2 = busca_binaria(lista2, valor2)
print(f"Resultado da busca Iterativa: {resultado_iterativo2}")  

resultado_recursivo2 = busca_binaria_recursiva(lista2, valor2)
print(f"Resultado da busca Recursiva: {resultado_recursivo2}")  

valor_inexistente = 15
resultado_iterativo_inexistente = busca_binaria(lista2, valor_inexistente)
print(f"Resultado da busca Iterativa para valor inexistente: {resultado_iterativo_inexistente}") 

resultado_recursivo_inexistente = busca_binaria_recursiva(lista2, valor_inexistente)
print(f"Resultado da busca Recursiva para valor inexistente: {resultado_recursivo_inexistente}")  

#:V