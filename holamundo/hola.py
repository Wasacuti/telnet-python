print("************************************")
print("*************Calculadora************")
print("************************************")
continuar="s";
while continuar == "s":
  menu = """
    1 - Suma
    2 - Resta
    3 - Multiplicación
    4 - División
    5 - Salir
    """
  print(menu)
  res=0;
  opc=int(input("Ingrese su opción: "))

  if opc == 1:
      print("SUMA")
      num1=int(input("Ingrese el número 1:"))
      num2=int(input("Ingrese el número 2:"))
      res=num1+num2
      print("La suma de los dos números es: ", res)
      continuar=input("Desea continuar S/N: ")
      continuar=continuar.lower()
  elif opc == 2:
      print("Resta")
      num1=int(input("Ingrese el número 1:"))
      num2=int(input("Ingrese el número 2:"))
      res=num1-num2
      print("La resta de los dos números es: ", res)
      continuar=input("Desea continuar S/N: ")
      continuar=continuar.lower()
  elif opc == 3:
      num1=int(input("Ingrese el número 1:"))
      num2=int(input("Ingrese el número 2:"))
      print("Multiplicación") 
      res=num1*num2
      print("La multiplicación de los dos números es: ", res)
      continuar=input("Desea continuar S/N: ")
      continuar=continuar.lower()
  elif opc == 4:
      num1=int(input("Ingrese el número 1:"))
      num2=int(input("Ingrese el número 2:"))
      print("División") 
      res=num1/num2
      print("La División de los dos números es: ", res)
      continuar=input("Desea continuar S/N: ")
      continuar=continuar.lower()
  elif opc == 5:
    continuar="N"
  else:
    print("opción invalida") 

print ("Hasta luego")
