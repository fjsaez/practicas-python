# programa que calcula si un año es bisiesto o no:

import os

def menu():
  opcion=''
  print()
  while not opcion in ['1','2']:
    opcion=input('Pulse 1 para continuar, 2 para salir: ')
  return opcion

def esbisiesto(anio):
  cond1 = anio % 4 == 0 and anio % 100 != 0
  cond2 = anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0
  return cond1 or cond2

# el cuerpo del programa:

accion='1'
while accion!='2':
  os.system('cls')
  if accion=='1':
    print()
    anio_b=int(input('Introduzca un año: '))
    print()
    if esbisiesto(anio_b):
      print('El año {0} es bisiesto'.format(anio_b))
    else:
      print('El año {0} NO es bisiesto'.format(anio_b))
  accion=menu()
print()
print('Bella ciao...')
