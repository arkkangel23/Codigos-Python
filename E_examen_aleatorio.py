import random
from pathlib import Path
from os import remove

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

        fichero.write (pregunta+"\n") # Ojo, importante poner el \n para que haga el salto de línea en el fichero

    fichero.close()


    

preguntas_extraidas = [] # Se almacenan las preguntas que ya han sido extraídas del fichero
contador_examenes = 1 # Almacena el número de exámenes generados

while contador_examenes <=5: # Mientras el número de exámenes generados sea menor que 5 vamos generando exámenes

    print ("----------------------- EXAMEN NÚMERO ", contador_examenes)
    contador_preguntas = 1
    lista_preguntas = [] # Inicializa la lista de preguntas para cada exámen nuevo

    while contador_preguntas <= 5: # Se generan 5 preguntas para cada examen
 
        num_pregunta = random.randint(1,25) # Se obtiene el número de línea para obtener la pregunta
        
        if num_pregunta not in preguntas_extraidas: # Si la pregunta aún no ha sido extraída se obtiene y se graba en la lista como extraída

            print(obtener_pregunta("Medios/examenes.txt",num_pregunta))
            contador_preguntas +=1
            preguntas_extraidas.append(num_pregunta) # Agrega la pregunta a la lista de extraídas para éste exámen
            lista_preguntas.append(obtener_pregunta("Medios/examenes.txt",num_pregunta))
    
    ruta_examen = "Medios/examen_" + str(contador_examenes) + ".txt" # Crea la ruta del nuevo examen N
    grabar_examen(ruta_examen,lista_preguntas) # Graba el examen en la ruta especificada
    contador_examenes +=1
    preguntas_extraidas = [] # Reinicia la lista de preguntas extraídas para comenzar un nuevo exámen

