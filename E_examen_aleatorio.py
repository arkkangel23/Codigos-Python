import random
from pathlib import Path
from os import remove

ruta_examenes = "examenes.txt" # Contiene la ruta del fichero donde se encuentran las preguntas de los exámenes

def obtener_pregunta (ruta,num): # Devuelve la pregunta de la línea num
    
    num_linea = 1
    fichero = open (ruta, "r")

    for linea in fichero:
       
        if num_linea == num:

            fichero.close()
            return linea

        else:
            num_linea +=1

def grabar_examen (ruta, lista_preguntas): # Graba un examen en un fichero, si el fichero existe lo borra
    
    if Path(ruta).exists(): # Si eol fichero ya esxiste lo borra
        remove(ruta)
    

    fichero = open (ruta, "x")

    for pregunta in lista_preguntas: # Recorre la lista de preguntas y las va insertando en el fichero

        fichero.write (pregunta) # Ojo, importante poner el \n para que haga el salto de línea en el fichero

    fichero.close()

def calcular_preguntas_totales (ruta): # Calcula cual és el número de preguntas que hay en el fichero examenes.txt y lo devuelve
    
    fichero = open (ruta, "r")
    num_preguntas = 0

    for linea in fichero:
       
       num_preguntas +=1
        
    fichero.close()
    return num_preguntas

def generar_examenes (num_e, num_p):   

    preguntas_extraidas = [] # Se almacenan las preguntas que ya han sido extraídas del fichero
    contador_examenes = 1 # Almacena el número de exámenes generados

    while contador_examenes <= num_e: # Mientras el número de exámenes generados sea menor que num_e vamos generando exámenes

        print ("----------------------- EXAMEN NÚMERO ", contador_examenes)
        contador_preguntas = 1
        lista_preguntas = [] # Inicializa la lista de preguntas para cada exámen nuevo

        while contador_preguntas <= num_p: # Se generan 5 preguntas para cada examen
    
            num_pregunta = random.randint(1,calcular_preguntas_totales(ruta_examenes)) # Se obtiene el número de línea para obtener la pregunta
            
            if num_pregunta not in preguntas_extraidas: # Si la pregunta aún no ha sido extraída se obtiene y se graba en la lista como extraída

                
                contador_preguntas +=1
                preguntas_extraidas.append(num_pregunta) # Agrega la pregunta a la lista de extraídas para éste exámen
                lista_preguntas.append(obtener_pregunta(ruta_examenes,num_pregunta))
        
        ruta_examen = "Examen_" + str(contador_examenes) + ".txt" # Crea la ruta del nuevo examen N
        grabar_examen(ruta_examen,lista_preguntas) # Graba el examen en la ruta especificada
        contador_examenes +=1
        preguntas_extraidas = [] # Reinicia la lista de preguntas extraídas para comenzar un nuevo exámen

print("  ********************************************************* \n",
      " *       GENERADOR DE EXÁMENES ALEATORIOS                * \n",
      " ********************************************************* \n",
      "\n",
      " Instrucciones: el archivo que contiene las preguntas debe ser un fichero de texto con el nombre ---> examenes.txt <---\n",
      " situado en la misma carpeta o directorio que este script. Puede contener el número de preguntas que desee,\n",
      " pero debe de haber una pregunta por línea, sin espacios entre cada pregunta. El resultado serán tantos archivos\n",
      " con extensión txt como número de exámenes se deseen generar.\n",
      " Un ejemplo correcto del contenido fichero examenes.txt sería el siguiente:\n",
      " Pregunta xxxxxxxxxxxxxxxxxx.\n",
      " Pregunta nnnnnnnnnnnnnnnnnn.\n",
      " Pregunta yyyyyyyyyyyyyyyyyy.\n")

num_examenes = int(input(" \n Introduzca cuántos exámenes desea generar: "))
num_preguntas = int(input(" \n Introduzca cuántas preguntas desea en cada examen: "))

print (" \n El número de preguntas que contiene el archivo examenes.txt es de: ", calcular_preguntas_totales(ruta_examenes))
print ("\n ------------------->>>>>>>> Generando exámenes...\n ")
generar_examenes(num_examenes,num_preguntas)

print(" \n Exámenes generados con éxito!\n")

input("\nPresiona ENTER para finalizar")