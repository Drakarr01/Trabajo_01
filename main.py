def suma(a , b):
  return a+b

def resta(a , b):
  return a-b

def multiplicacion(a , b):
  return a*b

def potencia(a, b):
  return a**b
  
print("Bienvenidos, esta es una calculadora de 3 operaciones (suma, resta y multiplicación.)")
x = int(input("Digite el primer número: "))
y = int(input("Digite el segundo número: ")) 

m = True
while m ==True:
  print("""Del siguiente menú, indique que operación desea realizar:
  a) Suma
  b) Resta
  c) Multipicación
  d) Salir """)
  opcion= input("Ingrese la operación a realizar: ").lower()
  print("\n")
  while opcion not in ("a", "b", "c", "d","e"):
    print("ERROR! DATO INGRESADO INCORRECTO.\nSolo puedes ingresar : a, b, c o d.")
    print("""Del siguiente menú, indique que operación desea realizar:
    a) Suma
    b) Resta
    c) Multipicación
    d) Potencia
    e) Salir""")
    opcion= input("Ingrese la operación a realizar: ").lower()
  if opcion == 'a':
    print(f"La suma de {x} con {y} es: {suma(x,y)}")
  elif opcion == "b":
    print(f"La resta de {x} con {y} es: {resta(x,y)}")
  elif opcion == "c":
    print(f"La multiplicación de {x} con {y} es: {multiplicacion(x,y)}")
  elif opcion == "d":
    print(f"La multiplicación de {x} con {y} es: {potencia(x,y)}")
  elif opcion == "e":
    print("Gracias por usar el programa.")
    m = False
       

       
