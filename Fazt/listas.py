lista= [1,2,3,"cuatro","cinco"]
number_list=[1,2,3,4,5,6]
colores=["rojo","verde","amarillo"]
rand_list=list(range(1,10))

print("lista:",lista)

print (number_list)

#print (dir(number_list))

print(rand_list)
#el metodo len(list) obtiene el tamaño del la lista 
print (len(lista))

#El método lista[#] obtiene el valor del elemento del indice # 

print(lista[1])

print("El numero 6 esta en la lista: ",6 in lista)

print("El numero dos esta en la lista: ",2 in lista)

print(colores)
#El metodo append agrega un elemento al final de la lista
colores.append("azul")
colores.append("celeste")
colores.remove("rojo")

#El metodo extend puede agragar varios elementos de una vez
#usando ["","",""]
colores.extend(["cafe","blanco","negro"])
print(colores)
print(len(colores))

#El metodo insert() ingresa un valor en determinado indice
colores.insert(0,"purpura")
print(colores)
colores.pop(2)
print(colores)

#sort lo ordena alfabeticamente
colores.sort()
print(colores) 
colores.sort(reverse=True)
print(colores)
#index obtiene el indice del elemento 
print(colores.index("negro"))
colores.append("verde")
print(lista.count('verde'))
print(colores) 