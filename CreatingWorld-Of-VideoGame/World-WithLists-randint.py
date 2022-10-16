#Generacion de listas vacias
import random
listafila=[]
listacolumna=[]
listaancho=[]
listalargo=[]
#Generacion de numeros aleatorios
for numero in range(4):
  num=random.randint(0,32)
  num2=random.randint(0,32)
  num3=random.randint(0,32)
  num4=random.randint(0,32)
  listafila.append(num)
  listacolumna.append(num2)
  listaancho.append(num3)
  listalargo.append(num4)
print("lista de filas:",listafila)
print("lista de columnas:",listacolumna)
print("lista de ancho:",listaancho)
print("lista de largo:",listalargo)

#Agrupar las listas dadas en tuplas
def lista(listafila, listacolumna, listaancho, listalargo): 
      
    merged_list = tuple(zip(listafila, listacolumna,listaancho,listalargo))  
    return merged_list 
print("Sus muros son:",lista(listafila, listacolumna, listaancho,listalargo))  

input()