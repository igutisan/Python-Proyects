import os
def menu():
  while(True):
    os.system('clear')
    
    print("----------- Menu principal -----------")
    print('')
    print('')
    print('Seleccione alguna opcion')
    print('')
    print('1. Seleccionar pelo')
    print('2. Seleccionar ojos')
    print('3. Seleccionar orejas-nariz')
    print('4. Seleccionar boca')
    print('5. Seleccionar cuello')
    print('6. Seleccione para vizualizar el diseno')
    print('7. Seleccione para salir')
    print('---------------------------------------')
    oprime = input('Digite la seccion a la que desea entrar: ')
    try:
      oprime=int(oprime)
      if oprime >= 1 and oprime <=7:
       return oprime
      else:
        print('Digite un numero dentro del rango: ')
      input()
    
    except:
       print('Digite segun las especificaciones ')


