a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

if a != 0:
  x = -b/a
  print 'Solucion: ', x
elif b == 0:
  print 'Tiene infinitas soluciones'
else:
  print 'La ecuacion no tiene solucion'