# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio 
# de un producto y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicarAumento(producto:int)->int:
    aumento=producto*0.5
    return producto + aumento

aumento=int(input("Numero aumento 5% :"))
resultado=aplicarAumento(aumento)
print(resultado)