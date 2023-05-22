# Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro  y 
# su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. Ejemplo si le pasamos
# "algoritmo" la deja como "agilmoort"

def ordenarCaracteres(cadena):
    lista=[]
    for caracter in cadena:
        lista.append(caracter)
    tam=len(lista)
    for i in range(tam-1):
        for j in range(i+1,tam):
            if(lista[i]>lista[j]):
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    cadena_reordenada="".join(lista)
    return cadena_reordenada


cadena=input("Cadena -> :")
orden_ascendente=ordenarCaracteres(cadena)
print(orden_ascendente)