# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:56:32 2021

@author: Marina
"""



#creamos unas listas
numlist = []
moleclist = []
smilelist = []
disolvlist = []
absorlist = []
emilist = []
stokeslist = []
rendlist = []
timelist = []
kflist = []
knrlist = []
molarlist = []

exactolist = []
rangolist = []


nombre_archivo = "MOLECULAS.txt"
archivo = open(nombre_archivo, 'r', encoding="utf8")
archivo.readline() 


for linea in archivo:        

    linea = linea.rstrip()
    #con esto quitamos el salto de linea
    
    separador = ';'
    lista = linea.split(';') #pon ;
    #con esto tenemos una lista
    
    
    numlist.append(lista[0])
    moleclist.append(lista[1])
    smilelist.append(lista[2])
    disolvlist.append(lista[3])
    absorlist.append(lista[4])
    emilist.append(lista[5])
    stokeslist.append(lista[6])
    rendlist.append(lista[7])
    timelist.append(lista[8])
    kflist.append(lista[9])
    knrlist.append(lista[10])
    molarlist.append(lista[11])

archivo.close()

columna = input("Dependiendo del dato que se vaya a querer introducir, escoge un número: *1* para longiud de onda de absorción (nm), *2* para longitud de onda de emisión (nm), *3* para el desplazamiento de Stokes (cm\u207B\u00B9), *4* para el rendimiento cuántico, *5* para el tiempo de vida de la fluorescencia (ns), *6* para la constante de tasa fluorescente (10\u2078 s\u207B\u00B9), *7* para la constante de tasa no radiativa (10\u2078 s\u207B\u00B9) y *8* para la absortividad molar (10\u2074 M\u207B\u00B9 cm\u207B\u00B9): ")
columna = int(columna)



if columna == 1:
    a=input("Introduce el valor correspondiente a la selección anterior: ")
    
    a1 = float(a) - 5.0
    a2 = float(a) + 5.0
    grupo_exacto = False
    grupo_rango = False
    
    for i in range(len(absorlist)): 
        
        if a==absorlist[i]:
           exactolist.append(i)
           grupo_exacto = True
                     
            
        if grupo_exacto == False:
            
            if absorlist[i]>=str(a1) and absorlist[i]<=str(a2):
                grupo_rango = True
                rangolist.append(i)
    
    if grupo_exacto == True:
        for h in range(len(exactolist)):
            print("El S.M.I.L.E. correspondiente a la longitud de onda", absorlist[exactolist[h]], "nm es", smilelist[exactolist[h]],". Disolvente: ", disolvlist[exactolist[h]],". Nombre de la molécula: ", moleclist[exactolist[h]],".")


    elif grupo_rango == True:
        for h in range (len(rangolist)):
            print("El S.M.I.L.E. correspondiente a los valores entre", a1,"nm y", a2,"nm es", smilelist[rangolist[h]], "y la longitud de onda tiene el valor de", absorlist[rangolist[h]],"nm. Disolvente: ", disolvlist[rangolist[h]],". Nombre de la molécula: ", moleclist[rangolist[h]],".")

    elif grupo_exacto == False and grupo_rango == False:
        print("El número introducido no posee ningún S.M.I.L.E. asociado.")
                

elif columna == 2:
    a=input("Introduce el valor correspondiente a la selección anterior: ")
    
    a1 = float(a) - 5.0
    a2 = float(a) + 5.0
    grupo_exacto = False
    grupo_rango = False
    
    for i in range(len(emilist)): 
        
        if a==emilist[i]:
            exactolist.append(i)
            grupo_exacto = True
                     
            
        if grupo_exacto == False:
            
            if emilist[i]>=str(a1) and emilist[i]<=str(a2):
                grupo_rango = True
                rangolist.append(i)
    
    if grupo_exacto == True:
        for h in range(len(exactolist)):
            print("El S.M.I.L.E. correspondiente a la longitud de onda", emilist[exactolist[h]],"nm","es", smilelist[exactolist[h]],". Disolvente: ", disolvlist[exactolist[h]],". Nombre de la molécula: ", moleclist[exactolist[h]],".")


    elif grupo_rango == True:
        for h in range (len(rangolist)):
            print("El S.M.I.L.E. correspondiente a los valores entre", a1, "nm y", a2, "nm es", smilelist[rangolist[h]], "y la longitud de onda tiene el valor de", emilist[rangolist[h]],"nm. Disolvente: ", disolvlist[rangolist[h]],". Nombre de la molécula: ", moleclist[rangolist[h]],".")

    elif grupo_exacto == False and grupo_rango == False:
        print("El número introducido no posee ningún S.M.I.L.E. asociado.")
                
        
    
elif columna == 3:
    a=input("Introduce el valor correspondiente a la selección anterior: ")
    
    
    a1 = float(a) - 5.0
    a2 = float(a) + 5.0
    grupo_exacto = False
    grupo_rango = False
    
    for i in range(len(stokeslist)): 
        
        if a==stokeslist[i]:
            exactolist.append(i)
            grupo_exacto = True
                     
            
        if grupo_exacto == False:
            
            if stokeslist[i]>=str(a1) and stokeslist[i]<=str(a2):
                grupo_rango = True
                rangolist.append(i)
    
    if grupo_exacto == True:
        for h in range(len(exactolist)):
            print("El S.M.I.L.E. correspondiente al desplazamiento de Stokes", stokeslist[exactolist[h]],"cm\u207B\u00B9 es", smilelist[exactolist[h]],". Disolvente: ", disolvlist[exactolist[h]],". Nombre de la molécula: ", moleclist[exactolist[h]],".")


    elif grupo_rango == True:
        for h in range (len(rangolist)):
          
            print("El S.M.I.L.E. correspondiente a los valores entre", a1, "cm\u207B\u00B9 y", a2, "cm\u207B\u00B9 es", smilelist[rangolist[h]], "y el valor del desplazamiento de Stokes", stokeslist[rangolist[h]],"cm^-1. Disolvente: ", disolvlist[rangolist[h]],". Nombre de la molécula: ", moleclist[rangolist[h]],".")

    elif grupo_exacto == False and grupo_rango == False:
        print("El número introducido no posee ningún S.M.I.L.E. asociado.")
   
    
elif columna == 4:
    a=input("Introduce el valor correspondiente a la selección anterior: ")
    
    a1 = float(a) - 0.05
    a2 = float(a) + 0.05
    grupo_exacto = False
    grupo_rango = False
    
    for i in range(len(rendlist)): 
        
        if a==rendlist[i]:
            exactolist.append(i)
            grupo_exacto = True
                     
            
        if grupo_exacto == False:
            
            if rendlist[i]>=str(a1) and rendlist[i]<=str(a2):
                grupo_rango = True
                rangolist.append(i)
    
    if grupo_exacto == True:
        for h in range(len(exactolist)):
            print("El S.M.I.L.E. correspondiente al rendimiento cuántico", rendlist[exactolist[h]], "es", smilelist[exactolist[h]],". Disolvente: ", disolvlist[exactolist[h]],". Nombre de la molécula: ", moleclist[exactolist[h]],".")


    elif grupo_rango == True:
        for h in range (len(rangolist)):
            
            print("El S.M.I.L.E. correspondiente a los valores entre", a1, "y", a2, "es", smilelist[rangolist[h]], "y el rendimiento cuántico tiene el valor de", rendlist[rangolist[h]],". Disolvente: ", disolvlist[rangolist[h]],". Nombre de la molécula: ", moleclist[rangolist[h]],".")

    elif grupo_exacto == False and grupo_rango == False:
        print("El número introducido no posee ningún S.M.I.L.E. asociado.")

elif columna == 5:
    a=input("Introduce el valor correspondiente a la selección anterior: ")
    
    a1 = float(a) - 1.0
    a2 = float(a) + 1.0
    grupo_exacto = False
    grupo_rango = False
    
    for i in range(len(timelist)): 
        
        if a==timelist[i]:
            exactolist.append(i)
            grupo_exacto = True
                     
            
        if grupo_exacto == False:
            
            if timelist[i]>=str(a1) and timelist[i]<=str(a2):
                grupo_rango = True
                rangolist.append(i)
    
    if grupo_exacto == True:
        for h in range(len(exactolist)):
            print("El S.M.I.L.E. correspondiente al tiempo de vida de la fluorescencia", timelist[exactolist[h]],"ns", "es", smilelist[exactolist[h]],". Disolvente: ", disolvlist[exactolist[h]],". Nombre de la molécula: ", moleclist[exactolist[h]],".")


    elif grupo_rango == True:
        for h in range (len(rangolist)):
            
            print("El S.M.I.L.E. correspondiente a los valores entre", a1,"ns y", a2,"ns es", smilelist[rangolist[h]], "para el tiempo de vida de la fluorescencia de", timelist[rangolist[h]],"ns. Disolvente: ", disolvlist[rangolist[h]],". Nombre de la molécula: ", moleclist[rangolist[h]],".")

    elif grupo_exacto == False and grupo_rango == False:
        print("El número introducido no posee ningún S.M.I.L.E. asociado.")

elif columna == 6:
    a=input("Introduce el valor correspondiente a la selección anterior: ")
    
    a1 = float(a) - 1.0
    a2 = float(a) + 1.0
    grupo_exacto = False
    grupo_rango = False
    
    for i in range(len(kflist)): 
        
        if a==kflist[i]:
            exactolist.append(i)
            grupo_exacto = True
                     
            
        if grupo_exacto == False:
            
            if kflist[i]>=str(a1) and kflist[i]<=str(a2):
                grupo_rango = True
                rangolist.append(i)
    
    if grupo_exacto == True:
        for h in range(len(exactolist)):
            print("El S.M.I.L.E. correspondiente a la constante de tasa fluorescente", kflist[exactolist[h]], "10\u2078 s\u207B\u00B9 es", smilelist[exactolist[h]],". Disolvente: ", disolvlist[exactolist[h]],". Nombre de la molécula: ", moleclist[exactolist[h]],".")


    elif grupo_rango == True:
        for h in range (len(rangolist)):
            
            print("El S.M.I.L.E. correspondiente a los valores entre", a1, "10\u2078 s\u207B\u00B9 y", a2, "10\u2078 s\u207B\u00B9 es", smilelist[rangolist[h]], "y la constante de tasa fluorescente tiene el valor de", kflist[rangolist[h]],"10^8 s^-1. Disolvente: ", disolvlist[rangolist[h]],". Nombre de la molécula: ", moleclist[rangolist[h]],".")

    elif grupo_exacto == False and grupo_rango == False:
        print("El número introducido no posee ningún S.M.I.L.E. asociado.")
                
elif columna == 7:
    a=input("Introduce el valor correspondiente a la selección anterior: ")
    
    a1 = float(a) - 0.5
    a2 = float(a) + 0.5
    grupo_exacto = False
    grupo_rango = False
    
    for i in range(len(knrlist)): 
        
        if a==knrlist[i]:
            exactolist.append(i)
            grupo_exacto = True
                     
            
        if grupo_exacto == False:
            
            if knrlist[i]>=str(a1) and knrlist[i]<=str(a2):
                grupo_rango = True
                rangolist.append(i)
    
    if grupo_exacto == True:
        for h in range(len(exactolist)):
            print("El S.M.I.L.E. correspondiente a la constante de tasa no radiativa", knrlist[exactolist[h]], "10\u2078 s\u207B\u00B9 es", smilelist[exactolist[h]],". Disolvente: ", disolvlist[exactolist[h]],". Nombre de la molécula: ", moleclist[exactolist[h]],".")


    elif grupo_rango == True:
        for h in range (len(rangolist)):
            
            print("El S.M.I.L.E. correspondiente a los valores entre", a1, "10\u2078 s\u207B\u00B9 y", a2, "10\u2078 s\u207B\u00B9 es", smilelist[rangolist[h]], "y la constante de tasa no radiativa tiene el valor de", knrlist[rangolist[h]],"10^8 s^-1. Disolvente: ", disolvlist[rangolist[h]],". Nombre de la molécula: ", moleclist[rangolist[h]],".")

    elif grupo_exacto == False and grupo_rango == False:
        print("El número introducido no posee ningún S.M.I.L.E. asociado.")


elif columna == 8:
    a=input("Introduce el valor correspondiente a la selección anterior: ")
    
    a1 = float(a) - 1.0
    a2 = float(a) + 1.0
    print(str(a1))
    grupo_exacto = False
    grupo_rango = False
    
    for i in range(len(molarlist)): 
        
        if a==molarlist[i]:
            exactolist.append(i)
            grupo_exacto = True
                     
            
        if grupo_exacto == False:
            
            if molarlist[i]>=str(a1) and molarlist[i]<=str(a2):
                grupo_rango = True
                rangolist.append(i)
    
    if grupo_exacto == True:
        for h in range(len(exactolist)):
            print("El S.M.I.L.E. correspondiente a la absortividad molar", molarlist[exactolist[h]], "10\u2074 M\u207B\u00B9 cm\u207B\u00B9 es", smilelist[exactolist[h]],". Disolvente: ", disolvlist[exactolist[h]],". Nombre de la molécula: ", moleclist[exactolist[h]],".")


    elif grupo_rango == True:
        for h in range (len(rangolist)):
            
            print("El S.M.I.L.E. correspondiente a los valores entre", a1, "y", a2, "10\u2074 M\u207B\u00B9 cm\u207B\u00B9 es", smilelist[rangolist[h]], "y la absortividad molar tiene el valor de", molarlist[rangolist[h]],"10\u2074 M\u207B\u00B9 cm\u207B\u00B9. Disolvente: ", disolvlist[rangolist[h]],". Nombre de la molécula: ", moleclist[rangolist[h]],".")

    elif grupo_exacto == False and grupo_rango == False:
        print("El número introducido no posee ningún S.M.I.L.E. asociado.")
                
                
elif columna > 8:
   
    print("No se puede obtener información de los datos dados por el usuario.")                   
    
   
    
    

    
    
        