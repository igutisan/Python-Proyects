#Creando variables para las validaciones
cdia=input("digite su CDIA: ")
cdia_upper=cdia.upper()
repeticion=cdia_upper.count("K")
posicion= (cdia[5])
poci1=(cdia[0])
poci10=(cdia[9])
MAS=cdia.find("+")
IGUAL=cdia.find("=")
CARACTER=cdia.find("&")
INTERROGANTE=cdia.find("?")


import sys
#Validacion del CDIA(Id) ingresado
def juego():
  tieneCaracter=0
  if len(cdia_upper) > 11:
    print("excede el limite de caracteres")
    sys.exit("CDIA invalido")
  if type(cdia)==str:
    print("es str")
  else:
    print("Solo caracteres")
    sys.exit("CDIA invalido")
  if (posicion=="@"):
    print("Si tiene el @")
  else:
    print("No tiene el @")
    sys.exit("CDIA invalido")
  
  if (poci1 != poci10):
    print("esta bien")
  else:
    print("cambie su cdia")
    sys.exit("CDIA invalido")
  if (repeticion>3):
    print("excede el limite de uso de la letra k ")
    sys.exit("CDIA invalido")
  else:
    print("es valido")

  if ( MAS >= 0):
    print("tiene el +")
  else:
    print("no tiene el +")
    sys.exit("CDIA invalido")
  if ( IGUAL > 0):
    tieneCaracter = 1
    print("Tiene el =")
  if ( CARACTER > 0 ):
    tieneCaracter = 1
    print("tiene el &")
  if (INTERROGANTE > 0):
    tieneCaracter = 1
    print("tiene el ?")
  if tieneCaracter < 1:
    print("Le hace falta un caracter")
    sys.exit("CDIA invalido")


juego()
#Validar que el CDIA ingresado este registrado
import GameRepository as asc
def leer_cdia():
  se_encuentra=asc.buscar_cdia(cdia)
  if (se_encuentra==0):
    print("Su CDIA no esta registrado")
   
  else:
    print("Su CDIA ya esta resgistrado")
    sys.exit("Su CDIA ya se encuentra registrado")
   

        

leer_cdia()
#Calculando la edad del usuario teniendo en cuenta su fecha de nacimiento
def calcular_edad():
    import datetime
    from datetime import date
    hoy=datetime.date.today()
    
    anioc=int(input("\nsu año de nacimiento: "))
    mesc=int(input("su mes de nacimiento: "))
    diac=int(input("su dia de nacimiento: "))
    fechaAct=date.today()
    
    calculando = (fechaAct.year) - (anioc)
    #Para saber si ya cumplio anos 
    calculando2 = calculando - 1
    edadFinal = 0
    if mesc > fechaAct.month:
      edadFinal = calculando2
    elif mesc == fechaAct.month:
       if diac >= fechaAct.day:
           edadFinal = calculando2
       else:
            edadFinal = calculando
    else: 
          edadFinal = calculando
        
    
    return edadFinal
#Definiendole la categoria de nivel que tiene
def mundo(respuesta1, edad, nivel):
   if edad>11 and edad<21:
    if respuesta1=="NO":
       print("Su mundo es el 1")
    elif respuesta1=="SI":
      if nivel < 50:
        print("Su mundo es el 2")
      elif nivel >= 50:
        print("Su mundo es el 3")
        
   if  edad>20:
    if respuesta1=="NO":
       print("Su mundo es el 4")
    elif respuesta1=="SI":
      if nivel < 50:
        print("Su mundo es el 5")
      elif nivel >= 50:
        print("Su mundo es el 6")
        


def remover_espacio(cadena):
  #Quitando espacios
  return cadena.replace(' ','')
        


#Asignando los respectivos niveles teneindo en cuenta la edad y la experienecia
def edades():
  edad=calcular_edad()
  if edad>=12:
      alias=input("Alias del jugador: ")
      if len(remover_espacio(alias)) > 4:
        experiencia=input("ya has jugado WorldCraft ASCII? (Si, No): ")
      else:
        print("No cumple con el limite minimo de caracteres")
        sys.exit("Alias invalido")
      respuesta1_upper= experiencia.upper()
    
      nivel=0
      if respuesta1_upper=="SI":
        nivel=int(input("¿Hasta que nivel llegaste? (el nivel va desde 1 hasta 100): "))
        nivel2 = nivel+2 
          
      if edad<16 and respuesta1_upper=="NO":
        print("Sera dirigido al nivel 2 del juego")
      elif edad<16 and respuesta1_upper=="SI":
        print("Sera dirigido al nivel", nivel)
      elif edad>=16 and respuesta1_upper=="SI":
          print("Sera dirigido al nivel", nivel2)
      elif edad>=16 and respuesta1_upper=="NO":
          print("Sera dirigido al nivel 1")
  
      mundo(respuesta1_upper, edad, nivel)
   #Descartando al usuario por su edad 
  else:
    print("No tiene edad suficiente")
    sys.exit("No posee con la edad necesaria")
edades()
    

input()