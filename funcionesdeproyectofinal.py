#Funciones que nos ayudaran a hacer procesos más automaticos

def mostrar_casas (): #Muestra las casas que hay en el condominio, muestran numeros del 1 al 30 y´se utilizara para cada vez que se tenga que ingresar una casa
    numero_casa=0
    numero_casa2=15
    for i in range (15):
        numero_casa=numero_casa+1
        numero_casa2=numero_casa2+1
        casa=('casa ', numero_casa)
        
        print('{:^10}{:^10}'.format (numero_casa, numero_casa2))
        

    return 'Estas son las casas que hay actualmente en el condominio'




def menu_opciones(lista_de_acciones):
    for h in range (5):
        print (lista_de_acciones[h])


