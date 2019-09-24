#if type(s) != str:
    #raise TypeError, "s debe ser del tipo str"

#if not hasattr(s,"__str__"):
    #raise TypeError, "No es string"

#si es numerico

def es_numero(w):
    try:
        w=int(w)
        if w>0 and w<31:
            return True
        else:
            return False
    except ValueError:
        print('Error, tiene que ingresar el numero de la casa que desea ingresar')
#si es entero
def es_numero2(w):
    try:
        w=int(w)
        if w>0:
            return True
        else:
            return False
    except ValueError:
        print('Error, tiene que ingresar un numero valido')

#while not variable.isdigit():

#validar contraseña
def clave(password):

    validar=False #que se vayan cumpliendo los requisitos uno a uno.
    long=len(password) #Calcula la longitud de la contraseña
    espacio=False  #variable para identificar espacios
    mayuscula=False #variable para identificar letras mayúsculas
    minuscula=False #variable para contar identificar letras minúsculas
    numeros=False #variable para identificar números
    y=password.isalnum()#si es alfanumérica retona True
    correcto=True #verifica que hayan mayuscula, minuscula, numeros y no alfanuméricos
        
    for carac in password: #ciclo for que recorre caracter por caracter en la contraseña

        if carac.isspace()==True: #Saber si el caracter es un espacio
            espacio=True #si encuentra un espacio se cambia el valor user

        if carac.isupper()== True: #saber si hay mayuscula
            mayuscula=True #acumulador o contador de mayusculas
                
        if carac.islower()== True: #saber si hay minúsculas
            minuscula=True #acumulador o contador de minúsculas
                
        if carac.isdigit()== True: #saber si hay números
            numeros=True #acumulador o contador de numeros
                            
    if espacio==True: #hay espacios en blanco
            print("La contraseña no puede contener espacios")
    else:
        validar=True #se cumple el primer requisito que no hayan espacios
                       
    if long <8 and validar==True:
        print("Mínimo 8 caracteres")
        validar=False #cambia a Flase si no se cumple el requisito móinimo de caracteres

    if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
        validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
    else:
        correcto=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
           
    if validar == True and correcto==False:
        print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

    if validar == True and correcto ==True:
        return True

#nombre de usuario
def nickname(nombre_usuario):

        long=len(nombre_usuario) #Calcular la longitud del nomre de usuario
        y=nombre_usuario.isalnum() #Calcula que la cadena contenga valores alfanuméricos
        
        if y== False: # La cadena contiene valores no alfanuméricos
            print("El nombre de usuario puede contener solo letras y números")
            
        if long < 6: 
            print("El nombre de usuario debe contener al menos 6 caracteres")
            
        if long > 12: 
            print("El nombre de usuario no puede contener más de 12 caracteres")
            
        if long >5 and long <13 and y ==True:
            return True #Verdadero si el tamaño es mayor a 5 y menor a 13
"""
#iniciar sesion
import usuario
import passw

correcto=False
while correcto==False:
        nombre=input("Ingrese nombre de usuario: ")
        if usuario.nickname(nombre) == True:
            print("Usuario creado exitosamente")
            correcto=True

while correcto==True:
    contrasenia=input("Ingrese su Password: ")
    if passw.clave(contrasenia)==True:
        print("Contraseña creada exitosamente")
        correcto=False
"""
