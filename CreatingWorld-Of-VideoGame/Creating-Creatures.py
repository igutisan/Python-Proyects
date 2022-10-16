Pasiva="Lirarnys"
hostil= "Lecat"
Lirarnys = "#"
Lecat = "%"


from datetime import datetime
import random
listaFila_Pasivos=[]
listaColumna_Pasivos=[]
listafila_Hostiles=[]
listacolumna_Hostiles=[]
#Asignar los datos a las listas de pasivos  
for numero in range(1):
  num=random.randint(0,32)
  num2=random.randint(0,32)
  listaFila_Pasivos.append(num)
  listaColumna_Pasivos.append(num2)
  hora2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

 #Asignar los datos a las listas de hostiles 
for numero in range(1):
  num3=random.randint(0,32)
  num4=random.randint(0,32)
  listacolumna_Hostiles.append(num4)
  listafila_Hostiles.append(num3)
  hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
 
  



  #definir la posicion de las creaturas creadas en diccionarios
  aspectos= {
      "El nombre de los hostiles es:" : hostil,
      "Los pasivos tienen la forma de este caracter:" : Lecat,
      "La fila de los hostiles es:" : listafila_Hostiles,
      "La columna de los hostiles es:" : listacolumna_Hostiles,
      "La hora en la que apareceran los hostiles es:" :  hora ,  
      "La fila de los pasivos es:" : listaFila_Pasivos,
      "La columna de los pasivos es:" : listaColumna_Pasivos,
      "La Hora en la que apareceran los pasivos:" : hora2    
  
}
print(aspectos)
  