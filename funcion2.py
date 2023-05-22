# 2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de 
# caracteres como primer parámetro, un carácter como segundo y otro carácter  como tercero, 
# la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver la cantidad 
# de veces que se reemplazo ese carácter  en la cadena

def reemplazarCaracteres(cadena:str,letra:str,letra_2:str)->int:
    cadena=cadena.replace(letra,letra_2)
    veces_remplazado=0

    for caracter in range(len(cadena)):
        if(cadena[caracter]==letra_2):
            veces_remplazado+=1

    return veces_remplazado     

cadena=input("Ingresar cadena :")
caracter=input("Ingresar caracter :")
caracter_2=input("Ingresar segundo caracter remplazador:")

cantidad=reemplazarCaracteres(cadena,caracter,caracter_2)
print(f"cantidad de veces reemplazado {cantidad}")