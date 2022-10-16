import cabello
import menu
import os


nombre=input('Digite el nombre del personaje: ')
archivo = nombre +'.txt'
file=open(archivo,'w')
obj1 = ''
obj2 = ''
obj3 = ''
obj4 = ''
obj5 = ''

while(True):
  oprime = menu.menu()
  os.system('clear')
 
 
    
  if oprime == 1:    
   
      opcion = cabello.pelo()
      if opcion == 1:
        obj1=("WWWWWWWWW \n")
       
      if  opcion == 2:
         obj1=('||||||||| \n')
         
      if  opcion == 3:
         obj1=('""""""""" \n')
        
      if  opcion == 4:
         obj1=('\\\////// \n')
         
      
       
      
  if oprime == 2:
    
    
      opcion = cabello.ojos()
      if opcion == 1:
        obj2= '|-(o o)-| \n'
      if opcion == 2:
        obj2=('|  \ /  | \n')
      if opcion == 3:
        obj2=('|-(. .)-| \n')
      if opcion == 4:
        obj2=('|  0 0  | \n')
        
    
      
  if oprime == 3:
    
   
    opcion = cabello.orejas_nariz()
    if opcion == 1:
      obj3 = '@   J   @ \n'
    if opcion == 2:
      obj3 =('{   "   } \n')
    if opcion == 3:
      obj3 =('[   j   ] \n')
    if opcion == 4:
      obj3 =('<   -   > \n')
   

  
  if oprime == 4:
    
   
    opcion = cabello.boca()
    if opcion == 1:
      obj4 =('|  ---  | \n')
    if opcion == 2:
      obj4 =('|   -   | \n')
    if opcion == 3:
      obj4 =('|   v   | \n')
    if opcion == 4:
      obj4 =('|  ===  | \n')
    
     
   

  if oprime == 5:
    
    opcion = cabello.cuello()
    if opcion == 1:
      obj5 =(' \_____/ \n')
    if opcion == 2:
      obj5 =(' \WWWWw/ \n')
      
  
      
  if oprime == 6:
     
    for i in range(6):
      file = open(archivo, 'a')
      if i == 1:
        file.write(obj1)
      if i == 2:
        file.write(obj2)
      if i == 3:
        file.write(obj3)
      if i == 4:
        file.write(obj4)
      if i == 5:
        file.write(obj5)
    file.close()    
    file = open(archivo, 'a')
    file.write(nombre,)
    file.write('\n')
    file = open(archivo, 'r')
    
    print(' ')
    print(file.read())
    file.close()
    opcion=cabello.eleccion()
    if opcion == 2:
      os.system('clear')
      break
    else:
      True
      
  if oprime == 7:
      break
      os.system('clear')
      
    
 
        
file.close()
    
      
nombre_criatura=input('Digite el nombre de la criatura: ')
nombre_arc = nombre_criatura +'.txt'
file2 = open(nombre_arc,'w')
obje1 = ''
obje2 = ''
obje3 = ''
obje4 = ''
obje5 = ''

while(True):
  oprime2 = menu.menu()
  os.system('clear')  

  if oprime2 == 1:    
   
      opcion = cabello.pelo_creatura()
      if opcion == 1:
        obje1=("MMMMMMMMM \n")
        
       
      if  opcion == 2:
         obje1=('^^^^^^^^^ \n')
         
      if  opcion == 3:
         obje1=('````````` \n')
        
      if  opcion == 4:
         obje1=('///////// \n')
         
      
       
      
  if oprime2 == 2:
    
    
      opcion = cabello.ojos_creatura()
      if opcion == 1:
        obje2= ('|-(0 0)-| \n')
      if opcion == 2:
        obje2=('|  - -  | \n')
      if opcion == 3:
        obje2=('|- . . -| \n')
      if opcion == 4:
        obje2=('|  o o  | \n')

   
  if oprime2 == 3:
    
   
    opcion = cabello.orejas_nariz_creaturas()
    if opcion == 1:
      obje3 = '""  J  "" \n'
    if opcion == 2:
      obje3 =('{   j   } \n')
    if opcion == 3:
      obje3 =('[   "   ] \n')
    if opcion == 4:
      obje3 =('@   -   @ \n')
   

  
  if oprime2 == 4:
    
   
    opcion = cabello.boca_creaturas()
    if opcion == 1:
      obje4 =('|   w   | \n')
    if opcion == 2:
      obje4 =('|   ~   | \n')
    if opcion == 3:
      obje4 =('|  ===  | \n')
    if opcion == 4:
      obje4 =('|   s   | \n')
    
     
   

  if oprime2 == 5:
    
    opcion = cabello.cuello_criatura()
    if opcion == 1:
      obje5 =(' \_____/ \n')
    if opcion == 2:
      obje5 =(' \...../ \n') 
   
  if oprime2 == 6:
     
    for i in range(6):
      file2 = open(nombre_arc, 'a')
      if i == 1:
        file2.write(obje1)
      if i == 2:
        file2.write(obje2)
      if i == 3:
        file2.write(obje3)
      if i == 4:
        file2.write(obje4)
      if i == 5:
        file2.write(obje5)
    file2.close()    
    file2 = open(nombre_arc, 'a')
    file2.write(nombre_criatura)
    file2.write('\n')
    file2 = open(nombre_arc, 'r') 
    print(file2.read())
    file2.close()
    opcion=cabello.eleccion_criaturas()
    if opcion == 2:
      os.system('clear')
      break
    else:
      True
  
  if oprime2 == 7:
      break
