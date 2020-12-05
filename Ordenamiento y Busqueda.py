##########################################################################
#################### TP 1 ORDENAMIENTO Y BUSQUEDA ########################
##########################################################################

############################ KENER SEBASTIAN #############################
############################ COLQUHOUN NOELIA ############################



import numpy as np

v64 = np.random.randint(1, 51, 10)        #vector de 10 enteros con números del 1 al 50

#########################################################
################ ORDENAMIENTO DE BURBUJA ################
#########################################################

'''def ordBurb(vector, i, cantDeElementos): PARÁMETROS: el vector a ordenar, el índice de inicio y el de fin.'''

def ordBurb(vector, i, cantDeElementos):  
  if cantDeElementos == 1:                #Planteamos el caso Base: si cantDeElementos es 1 ha finalizado el recorrido
    return vector                         #Retorna el vector ordenado
  else:                                   #Si no llegó al caso base, empieza a recorrer
    for q in range(cantDeElementos):      #Pasa por cada índice
      if vector[i] > vector[i+1]:                           #Si el ítem del primer índice es mayor que el siguiente...
        vector[i], vector[i+1] = vector[i+1], vector[i]     #Intercambiamos sus valores
      else:                                                 #Si no es mayor, la función vuelve a llamarse a si misma 
        ordBurb(vector, i+1, cantDeElementos-1)             #Pero esta vez comenzando un índice a la derecha y achicando el rango en 1 posición
  return vector                                             #Retorna el vector ordenado

#########################################################
############## BUSQUEDA BINARIA RECURSIVA ###############
#########################################################

'''def busquedaBinariaRec(vector, item, izquierda, derecha): Recibe la posición donde 
queremos comenzar la busqueda, posición del final'''

def busquedaBinariaRec(vector, item, izquierda, derecha): 
    
    indiceMedio = (izquierda + derecha) // 2              #Esta variable guarda el indice del medio del vector
    elementoDelMedio = vector[indiceMedio]                #Esta variable guarda el valor de ese índice

    if izquierda > derecha:                               #Si la lista esta vacia, significa que el item no  encuentra en el vector y retorna False
        return -1
    if elementoDelMedio == item:                          #Si el indice del medio contiene el item, termina la busqueda retornando la posicion del mismo
        return indiceMedio 
    if item < elementoDelMedio:                           #Si no estaba allí y el valor del ítem es MENOR que el valor encontrado...
      return busquedaBinariaRec(vector, item, izquierda, indiceMedio - 1)    #Volvemos a llamar la función pero esta vez el FINAL de la búsqueda será 
                                                                             #uno antes que el índice medio ya revisado.   
    else:                                                                    #Si no estaba allí y el valor del ítem es MAYOR que el valor encontrado...
      return busquedaBinariaRec(vector, item, indiceMedio + 1, derecha)      #volvemos a llamar la función pero esta vez el PRINCIPIO de la búsqueda será 
                                                                             #uno después que el índice medio ya revisado.


'''def armarVc(cant): Función que arma un vector provisorio de ceros con la cantidad de elementos dada'''

def armarVc(cant):
  v1 = np.zeros((cant), int)
  return v1

'''def reemplazarIndice(vector, indice, item): Función que reemplaza el valor de un índice 
de un vector con un item pasado como argumento.'''

def reemplazarIndice(vector, indice, item):
  vector[indice] = item
  return vector

'''def usuarioArmaVector(): Función que reemplaza cada cero del vector provisorio con los valores ingresados por el usuario'''

def usuarioArmaVector():
  submenu = int(input("¿Cuántos números desea ingresar?: "))
  v1 = armarVc(submenu)
  for i in range(submenu):
    valores = int(input("Ingrese un valor: "))
    reemplazarIndice(v1, i, valores)
  return v1

'''FUNCION MENU: Originalmente hecha en colab, donde anda perfectamente. Al pasarlo al editor
				 no se modifico completamente'''

'''def tpUno(): Funcion final con menu interactivo'''

def tpUno():
  menu = 1
  while menu != 4:
  	menu = int(input("Elija una opción: \n 1- Ingresar Datos: \n 2- Ordenar \n 3- Buscar \n 4- Salir "))
  	if menu == 1:#Si el usuario elige 1, arma el vector personalizado
  		v1 = usuarioArmaVector()
  		print(v1)
  	elif menu == 2: #Si elige 2, ordenamos el vector realizado
  		ordBurb(v1, 0, len(v1))
  		print(v1)
  	elif menu == 3:                               #Si elige 3 y está ordenado, busca el elemento solicitado.  
  		ordBurb(v1, 0, len(v1))                     #Si no está ordenado por usuario, 1ro lo ordena y luego realiza la búsqueda
  		busqueda = int(input("Ingrese el valor que desea buscar dentro del vector: "))
  		resultado = busquedaBinariaRec(v1, busqueda, 0, len(v1)-1)
  		print(v1)
  		if resultado >= 0:                          #Imprime por pantalla la posición del elemento si está
  			print("El elemento buscado se encuentra en la posición " + str(resultado) + " del vector.")
  		else:
  			print("El elemento no se encuentra dentro de este vector")    #Imprime esto si no está
  	elif menu <= 0 or menu > 4:
  		raise Exception("ERROR: Las opciones válidas de menú van de 1 a 4") #Marca error si se coloca un número fuera del rango del menú

tpUno()