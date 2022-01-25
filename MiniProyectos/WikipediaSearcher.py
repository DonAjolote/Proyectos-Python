import wikipedia

x = [1,2,3]
wikipedia.set_lang("es")

while True:
    opcion = input("\nIngrese una opcion \n1.-Buscar un tema \n2.-Cambiar el lenguaje \n3.-Buscar sugerencias\n4.-Salir \nOpcion: ")
    print("\n") 
    if opcion == "1":
        a = input("Ingrese el tema que quiere buscar: ")
        print("\n")
        print(wikipedia.summary(a))
    elif opcion == "2":
        b = input("Ingrese el lenguaje:")
        print("\n")
        wikipedia.set_lang(b)
    elif opcion == "3":
        c = input("Ingrese una palabra:")
        print("\n")
        print(wikipedia.search(c, results = 5, suggestion = True))
    elif opcion == "4": 
        break    
    elif opcion is not x:
        print("\nOpcion inválida\n")
        
 