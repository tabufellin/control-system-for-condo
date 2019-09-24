#programa principal
#Mes en el que se esta

import pymongo

conexion=pymongo.MongoClient()
oh_la_garra=conexion['condominio']['datos_casas']
####hacer conexion
listado=list(oh_la_garra.find())
datos_casas=listado
import datetime

from funcionesdeproyectofinal import *
from funcionesyessy import *
fecha=datetime.date.today()
lista_de_acciones=['Datos generales','Requerimientos de pago',
                  'Contadores de agua','Ingresos','Reportes','Notificacion de pagos','Subir foto']#Lista de las cosas que se pueden usar, se usa con funcion menu_opciones


h=0

monto_metro_agua=15

print('---------BIENVENIDOS AL PROGRAMA REGISTRO PAGO CONDOMINIOS RCP---------')
print('OBJETIVOS: El  objetivo  principal  del  programa es poder ayudar a los')
print('tesoreros o administradores de los condominios que manejen el dinero de')
print('una forma mas organizada, para llevar un mejor control de los pagos que')
print('los  residentes realizan en las fechas ya establecida.')
print('')
print('INSTRUCCIONES: Debe ingresar el número de opción a la cual desea ingresar')

print('------------------------------------------------------------------------')
print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print('                        REGISTRO PAGO CONDOMINIOS RPC                   ')
print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print('------------------------------------------------------------------------')



casas=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
casa='Numero de casa'
nombre= 'Nombre del propietario'
cuota_or='Cuota ordinaria'
cuota_ex='Cuota extraordinaria'
con_agua='Consumo de agua (m^3)'
fecha_lec='fecha de lectura'
num_tel='Numero de telefono'
num_cel='Numero de celular propietario: '
coe='Correo electronico'
num_cont='Numero de contador de agua'
fecha_lect='fecha de lectura'

monto_con_agua='Monto consumo de agua'
forma_realizar=[casa,nombre,cuota_or,cuota_ex,con_agua]
forma_realizar2=[casa,nombre,cuota_or,cuota_ex,monto_con_agua]
forma_realizar3=[casa,nombre,cuota_or,cuota_ex,con_agua,num_tel,num_cel,coe]
forma_realizar4=[casa,nombre,num_cont,fecha_lect]





    
empezar=input('¿Quieres iniciar el programa?(Si/No)' )#Con esto se define si el programa va a empezar o no


while empezar !='Si' and empezar != 'si' and empezar != 'no' and empezar != 'No': #Validación de que si se quiere inciar el programa, programacion defensiva
    print('Usted esta ingresando un dato incorrecto')
    empezar=input('¿Quieres iniciar el programa?(Si/No)' )

while empezar == 'Si' or empezar == 'si' :     #Todo lo que hagamos tiene que ir dentro de este while

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('                             -OPCIONES- ')
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('Estas son las acciones que usted puede realizar')
    print ('Ingresar a los datos generales (Palabra clave: 1)')
    print('Ingresar a las cuentas por cobrar (Palabra clave: 2)')
    print('Ingresar a los contadores de agua (Palabra clave: 3)')
    print('Funcion de agregar pago fijo a todas las casas (Palabra clave: 4)') 
    print('Salir (Palabra clave: 5)')
    

    ##########################################################################################
    accion=input('¿Que acción desea realizar?')
    if accion == '1':
        show=mostrar_casas()
        print(show)
        casa_mostrar=input('Los datos de que casa desea visualizar')
        w=casa_mostrar
        validar_numero=es_numero(w)
        if validar_numero==True:
            filtro={casa : w}
            cursor=oh_la_garra.find_one(filtro)
            h=0
            for impresion in forma_realizar3:
                print(forma_realizar3[h],': ',cursor[impresion])
                h=h+1

    
            
            
            edicion=input('¿Desea editar algun dato o solamente regresar al menu principal? (Palabra clave: 1,2 respectivamente)')
                
            while edicion != '1' and edicion != '2':
                print('Usted ingreso un dato erroneo, vuelva a intentarlo')
                edicion=input('¿Desea editar algun dato o solamente regresar al menu principal? (Palabra clave: 1,2 respectivamente)')
            if edicion=='1':
                
                print('El numero de casa es ineditable')
                print('A continuacion los que si se pueden editar: ')
                print('Nombre del propietario')
                print('Numero de telefono')
                print('Numero de celular propietario')
                print('Correo electronico')
                print('Numero de contador de agua')
                
                
                que_dato=input('¿Qué dato desea editar?(Escribalo tal y cual se encuentra arriba)')
                while que_dato !='Nombre del propietario' and que_dato !='Numero de telefono' and que_dato !='Numero de celular propietario' and que_dato !='Correo electronico' and que_dato !='Numero de contador de agua':
                    print('Usted ingreso un dato erroneo')
                    que_dato=input('¿Qué dato desea editar?(Escribalo tal y cual se encuentra arriba)')
                filtro=casa_mostrar
                mensaje=input('Escriba que quiere poner en su lugar')
                adjunto={casa:filtro}
                adjunto2={que_dato : mensaje}
                oh_la_garra.update(adjunto,{'$set': adjunto2})
      #          diccionario_editar=datos_casas[w]
        #        mensaje=input('Escriba que quiere poner en su lugar')
          #      diccionario_editar[que_dato]=mensaje
            
    
 ###########################################################################################           ############################################################################

    elif accion=='2':
        show=mostrar_casas()
        print(show)
        casa_mostrar=input('Los datos de que casa desea visualizar')
        w=casa_mostrar
        validar_numero=es_numero(w)
        if validar_numero==True:
            filtro={casa : w}
            cursor=oh_la_garra.find_one(filtro)
            h=0

            
            calculo_agua=int(cursor[con_agua])
            calculo_agua=calculo_agua*15
            adjunto1={casa: casa_mostrar}
            adjunto2={monto_con_agua : calculo_agua}
            print(adjunto1)
            print(adjunto2)
            oh_la_garra.update(adjunto1,{'$set': adjunto2})
          
            for impresion in forma_realizar2:
                print(forma_realizar2[h],': ',cursor[impresion])
                h=h+1
            
            accion_pago=input('Desea realizar algun pago o solo regresar al menu inicial (Clave: 1,2 respectivamente)')
            while accion_pago != '1' and accion_pago != '2':
               accion_pago=input('Usted debe ingresar solamente, (1) o (2)')
               

            
                
            if accion_pago=='1':
                print('Cuota ordinaria')
                print('Cuota extraordinaria')
                print('Monto consumo de agua')
                pago_en=input('¿En que rama desea realizar el pago? Escriba literalmente el area (Ej. Si quiere pagar el consumo de agua escriba "Monto consumo de agua"')
                while pago_en != 'Monto consumo de agua' and pago_en != 'Cuota extraordinaria' and pago_en != 'Cuota ordinaria':
                   pago_en=input('Usted debe ingresar solamente, (1),(2) o (3)')
                pago_cuota=input('¿Cuanto desea pagar en la cuota ordinaria?')
                w=pago_cuota
                probar=es_numero2(w)
                while probar != True:
                    w=input('¿Cuanto desea pagar en la cuota ordinaria?')
                    probar=es_numero2(w)

                

                pago_cuota=float(pago_cuota)
                dato_pagado=float(cursor[pago_en])
                dato_pagado=dato_pagado-pago_cuota
                print(dato_pagado)

                if pago_en == monto_con_agua:
                    adjunto1={casa: casa_mostrar}
                    adjunto2={pago_en : dato_pagado}
                    print(adjunto1)
                    print(adjunto2)
                    oh_la_garra.update(adjunto1,{'$set': adjunto2})
                    cambio_en_agua=dato_pagado/15
                
                    adjunto2={con_agua : cambio_en_agua }
                    oh_la_garra.update(adjunto1,{'$set': adjunto2})
                else:
                    adjunto1={casa: casa_mostrar}
                    adjunto2={pago_en : dato_pagado}
                    print(adjunto1)
                    print(adjunto2)
                    oh_la_garra.update(adjunto1,{'$set': adjunto2})
                
           

                    
                    
                


            elif accion_pago=='2':
                
                accion=input('¿Que acción desea realizar ahora?')
                    
                
  
                        
                        
                    
                    
                    
                




########################################################################################################################################################

    elif accion=='3':
        show=mostrar_casas()
        print(show)
        casa_mostrar=input('Los datos de que casa desea visualizar')
        w=casa_mostrar
        validar_numero=es_numero(w)
        if validar_numero==True:
            filtro={casa : w}
            cursor=oh_la_garra.find_one(filtro)
            h=0
            for impresion in forma_realizar4:
                print(forma_realizar4[h],': ',cursor[impresion])
                h=h+1

            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('                             -OPCIONES- ')
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('Estas son las acciones que usted puede realizar')
            print ('Ingresar a los datos generales (Palabra clave: 1)')
            print('Ingresar a las cuentas por cobrar (Palabra clave: 2)')
            print('Ingresar a los contadores de agua (Palabra clave: 3)')
            print('Salir (Palabra clave: 4)')
            

            accion=input('¿Que acción desea realizar ahora?')
            
##################################################################################################################




    elif accion=='4':
        
        seguro=input('¿Esta seguro que desea agregar un pago de 400 a todas las casas?(Escriba "Si'')')
        if seguro=='Si' or seguro=='si':
            h=1
            
            for casa_elegida in casas :
                     filtro={'Numero de casa' : str(h)}
                     cursor=oh_la_garra.find_one(filtro)
                     agrego_pago=int(cursor[cuota_or])
                     agrego_pago=agrego_pago+400
                     adjunto1={ casa   :str(casa_elegida)}
                     adjunto2={cuota_or : agrego_pago}
                     print(adjunto1)
                     print(adjunto2)
                     oh_la_garra.update(adjunto1,{'$set': adjunto2})
                     h=h+1
                     
                     
        

    
                
        
    elif accion=='5':
                
                break
                  
        
        



print('Bye')












