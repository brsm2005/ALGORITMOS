#Bryan Salvador
import os
import random
import time
from collections import deque 
archivoUsuarios="usuarios.txt"
archivoNinjas="ninjas.txt"
archivoCombates="combates.txt" 
usuarios=[]
ninjas=[]
habilidadesNinjas={"Habilidades Ofensivas":{"Kenjutsu (corto alcance)":("Estocada","Lluvia de cortes","Navajas", "Puños de hierro","Katana","Porras","Nunchaku"),
                                            "Sojutsu (Arma Lanzable)":("Bumeran","Estrellas", "Kunai","Dagas","Segador de almas"),
                                            "Taijutsu (cuerpo a cuerpo)":("Suplex","Lluvia de patadas","Llaves","Patada tornado","Codazo","Barrido doble", "Gancho"),
                                            "Ninjutsu (Habilidades magicas)":("Esfera de fuego", "Esfera de energía", "Estallido obscuro", "Fragmento de hielo eterno", "Hechizo adbsorción de almas", "Destello negro")},
                    "Habilidades Defensivas":{"Kumai (Escudo)":("Escudo de protección", "Campo de energía", "Angel guardian"),
                                              "Hichy (camuflaje)":("Invisibilidad", "Cortina de humo", "Cortina de almas en pena","Muro de hielo","Pared de fuego"),
                                              "Blink (bloqueo)":("Bloqueo", "Espejismo defensivo","Alucinación", "Campo de fuerza","Despliegue de energía")},
                   }

def cargarusuarios(archivousuarios):
    if not os.path.exists(archivousuarios):
        return
    with open(archivousuarios, "r") as archivo:
        for linea in archivo:
            try:
                usuario = eval(linea.strip())
                if isinstance(usuario, dict):
                    usuarios.append(usuario)
                else:
                    print("⚠️ Línea ignorada (no es un diccionario):", linea.strip())
            except:
                print("⚠️ Error al evaluar línea:", linea.strip())
        
def registrarse(archivoUsuarios):
    if not os.path.exists(archivoUsuarios):
        try:
            nombreUsuario = input("Ingrese su nombre y apellido: ").strip()
            palabras = nombreUsuario.split()
            if len(palabras) != 2:
                print("Debe ingresar solo nombre y apellido")
                return registrarse(archivoUsuarios)
            else:
                if all(palabra.isalpha() for palabra in palabras):
                    usuario = f"{palabras[0].lower()}.{palabras[1].lower()}@gmail.com"
                else:
                    print("Solo se permiten letras en el nombre y apellido.")
                    return registrarse(archivoUsuarios)
        except:
            print("Ocurrió un error")
        try:
            identificacion=input("Ingrese su cédula: ")
            if all(identificacion.isdigit() for identificacion in identificacion):
                pass
            else:
                print("Solo se permiten números en la cédula. Saliendo del sistema")
                return registrarse(archivoUsuarios)
        except:
            print("Ocurrió un error")
        edad= input("Ingrese su edad: ")
        contraseña=input("Ingrese su contraseña (debe ser de 8 caracteres o más, incluir una mayúscula y un número): ")
        while len(contraseña) < 8 or not any(char.isupper() for char in contraseña) or not any(char.isdigit() for char in contraseña):
            print("La contraseña no cumple lo solicitado")
            contraseña=input("Ingrese su contraseña: ")
        usuarioNuevo={"nombre": nombreUsuario,"identificacion":identificacion,"edad":edad,"contraseña":contraseña,"usuario":usuario}
        usuarios.append(usuarioNuevo)
        with open(archivoUsuarios,"w") as archivo:
            archivo.write(str(usuarioNuevo))
        print(f'''Su usuario es: {usuario} y su contraseña es: {contraseña}''')
        print("Registrado con éxito")
        return
    with open(archivoUsuarios,"r") as archivo:
        for linea in archivo:
            User=eval(linea.strip())
            usuarios.append(User)
        try:
            nombreUsuario = input("Ingrese su nombre y apellido: ").strip()
            palabras = nombreUsuario.split()
            if len(palabras) != 2:
                print("Debe ingresar solo nombre y apellido")
            else:
                if all(palabra.isalpha() for palabra in palabras):
                    pass
                else:
                    print("Solo se permiten letras en el nombre y apellido.")
                    return registrarse(archivoUsuarios)
        except:
            print("Ocurrió un error")
        usuario=nombreUsuario.split(" ")[0].lower()+"."+nombreUsuario.split(" ")[1].lower()+"@gmail.com"
        try:
            identificacion=input("Ingrese su cédula: ")
            if all(identificacion.isdigit() for identificacion in identificacion):
                pass
            else:
                print("Solo se permiten números en la cédula. Saliendo del sistema")
                return registrarse(archivoUsuarios)
        except:
            print("Ocurrió un error")
        for u in usuarios:
            if u["usuario"].lower() == usuario.lower() or u["identificacion"] == identificacion:
                print("❌ El usuario o la cédula ya están registrados.")
                return
        edad= int(input("Ingrese su edad: "))
        contraseña=input("Ingrese su contraseña (debe ser de 8 caracteres o más, incluir una mayúscula y un número): ")
        while len(contraseña) < 8 or not any(char.isupper() for char in contraseña) or not any(char.isdigit() for char in contraseña):
            print("La contraseña no cumple lo solicitado")
            contraseña=input("Ingrese su contraseña: ")
        usuarioNuevo={"nombre": nombreUsuario,"identificacion":identificacion,"edad":edad,"contraseña":contraseña,"usuario":usuario}
        usuarios.append(usuarioNuevo)
        with open(archivoUsuarios,"w") as archivo:
            archivo.write(str(usuarioNuevo))
        print(f'''Su usuario es: {usuario} y su contraseña es: {contraseña}''')
        print("Registrado con éxito")

def cargarNinjas(archivoNinjas):
    if not os.path.exists(archivoNinjas):
        pass
    else:
        with open(archivoNinjas, "r") as archivo:
            for linea in archivo:
                try:
                    ninja_dict = eval(linea.strip())
                    for ninja in ninja_dict.values():
                        if isinstance(ninja, dict):
                            ninjas.append(ninja)
                        else:
                            print("⚠️ Línea ignorada (no es un diccionario):", linea.strip())
                except:
                    print("⚠️ Error al evaluar línea:", linea.strip())

def habilidadesOfensivas(habilidadesNinjas,puntos):
    puntos=puntos
    habilidadNinja = []
    habilidades = habilidadesNinjas["Habilidades Ofensivas"]
    contador=1
    claves = list(habilidades.keys())
    print("\n--------------------------------------------------------\n")
    print("PUEDES ELEGIR 2 TIPOS DE HABILIDADES OFENSIVAS")
    while contador<=2:
        print("HABILIDAD OFENSIVA ",contador," DE ",2)
        while True:
            print("\nTipos de habilidades ofensivas:")
            for i, clave in enumerate(claves, start=1):
                print(f"{i}. {clave}")
            
            opcion = input("Ingrese una opción para el tipo de habilidad ofensiva: ")
            
            if opcion.isdigit():
                indice = int(opcion) - 1
                if indice==0:
                    puntos+=2.00
                elif indice==1:
                    puntos+=1.25
                elif indice==2:
                    puntos+=2.50
                elif indice==3:
                    puntos+=1.00

                if 0 <= indice < len(claves):
                    habilidadElegida = claves[indice]
                    break
            
            print("Opción no válida. Inténtelo de nuevo.")
        
        opciones = habilidades[habilidadElegida]
        
        randomHabilidad=random.sample(opciones, 2)
        habilidadNinja.extend(randomHabilidad)

        print(f"\nHas elegido el tipo de habilidad ofensiva: {habilidadElegida}")
        print("Tus habilidades son:")
        for h in randomHabilidad:
            print(f"- {h}")
        contador+=1
        print("\n--------------------------------------------------------\n")
    return habilidadNinja, puntos

def habilidadesDefensivas(habilidadesNinjas,puntos):
    habilidadNinja = []
    habilidades = habilidadesNinjas["Habilidades Defensivas"]
    contador=1
    claves = list(habilidades.keys())
    print("\n--------------------------------------------------------\n")
    print("PUEDES ELEGIR 2 TIPOS DE HABILIDADES DEFENSIVAS")
    while contador<=2:
        print("HABILIDAD DEFENSIVA ",contador," DE ",2)
        while True:
            print("\nTipos de habilidades defensivas:")
            for i, clave in enumerate(claves, start=1):
                print(f"{i}. {clave}")
            
            opcion = input("Ingrese una opción para el tipo de habilidad ofensiva: ")
            
            if opcion.isdigit():
                indice = int(opcion) - 1
                if indice==0:
                    puntos+=2.00
                elif indice==1:
                    puntos+=1.25
                elif indice==2:
                    puntos+=2.50
                if 0 <= indice < len(claves):
                    habilidadElegida = claves[indice]
                    break
            
            print("Opción no válida. Inténtelo de nuevo.")
        
        opciones = habilidades[habilidadElegida]
        randomHabilidad=random.sample(opciones, 2)
        habilidadNinja.extend(randomHabilidad)

        print(f"\nHas elegido el tipo de habilidad defensiva: {habilidadElegida}")
        print("Tus habilidades son:")
        for h in randomHabilidad:
            print(f"- {h}")
        print("\n--------------------------------------------------------\n") 
        contador+=1
    
    return habilidadNinja, puntos

def habilidadesMixtas(habilidadesNinjas,puntos):
    habilidadNinja = []
    habilidadesDefensivas = habilidadesNinjas["Habilidades Defensivas"]
    habilidadesOfensivas = habilidadesNinjas["Habilidades Ofensivas"]
    contador=1
    clavesDefensivas = list(habilidadesDefensivas.keys())
    clavesOfensivas = list(habilidadesOfensivas.keys())
    #--------------------DEFENSIVO
    print("\n--------------------------------------------------------\n")
    print("PUEDES ELEGIR 1 TIPO DE HABILIDAD DEFENSIVA")
    print("HABILIDAD DEFENSIVA ",contador," DE ",1)
    while True:
        print("\nTipos de habilidades defensivas:")
        for i, clave in enumerate(clavesDefensivas, start=1):
            print(f"{i}. {clave}")
        
        opcion = input("Ingrese una opción para el tipo de habilidad defensiva: ")
        
        if opcion.isdigit():
            indice = int(opcion) - 1
            if indice==0:
                puntos+=2.00
            elif indice==1:
                puntos+=1.5
            elif indice==2:
                puntos+=2.5
            if 0 <= indice < len(clavesDefensivas):
                habilidadElegidaDefensiva = clavesDefensivas[indice]
                break
        
        print("Opción no válida. Inténtelo de nuevo.")
    
    opcionesDefensivas = habilidadesDefensivas[habilidadElegidaDefensiva]
    randomHabilidadDefensiva=random.sample(opcionesDefensivas, 2)
    habilidadNinja.extend(randomHabilidadDefensiva)
    #-----------OFENSIVO
    print("\n--------------------------------------------------------\n")
    print("PUEDES ELEGIR 1 TIPO DE HABILIDAD OFENSIVA")
    print("HABILIDAD OFENSIVA ",contador," DE ",1)
    while True:
        print("\nTipos de habilidades ofensivas:")
        for i, clave in enumerate(clavesOfensivas, start=1):
            print(f"{i}. {clave}")
        
        opcion = input("Ingrese una opción para el tipo de habilidad ofensiva: ")
        
        if opcion.isdigit():
            indice = int(opcion) - 1
            if indice==0:
                puntos+=2.00
            elif indice==1:
                puntos+=1.50
            elif indice==2:
                puntos+=2.50
            elif indice==3:
                puntos+=1.00
            if 0 <= indice < len(clavesOfensivas):
                habilidadElegidaOfensiva = clavesOfensivas[indice]
                break
        
        print("Opción no válida. Inténtelo de nuevo.")
    
    opcionesOfensivas = habilidadesOfensivas[habilidadElegidaOfensiva]
    randomHabilidadOfensiva=random.sample(opcionesOfensivas, 2)
    habilidadNinja.extend(randomHabilidadOfensiva)

    print("\n---------------------HABILIDADES--------------------------\n")

    print(f"\nHas elegido el tipo de habilidad defensiva: {habilidadElegidaDefensiva}")
    print("Tus habilidades defensivas son:")
    for h in randomHabilidadDefensiva:
        print(f"- {h}")

    print(f"\nHas elegido el tipo de habilidad ofensiva: {habilidadElegidaOfensiva}")
    print("Tus habilidades ofensivas son:")
    for h in randomHabilidadOfensiva:
        print(f"- {h}")
    print("\n--------------------------------------------------------\n")
    return habilidadNinja, puntos

def Preorder(arbol):
    
    if isinstance(arbol, dict):
        lista = []
        
        
        valor = arbol.get("valor")
        if isinstance(valor, str) and not valor.isupper():
            lista.append(valor)
        
        
        lista += Preorder(arbol.get("izquierda"))
        lista += Preorder(arbol.get("derecha"))
        return lista
    
    return []

def Inorder(arbol):
    if isinstance(arbol, dict):
        lista = []
        lista += Inorder(arbol.get("izquierda"))
        
        valor = arbol.get("valor")
        if isinstance(valor, str) and not valor.isupper():
            lista.append(valor)
            
        lista += Inorder(arbol.get("derecha"))
        return lista
    return []

def Posorder(arbol):
    if isinstance(arbol, dict):
        lista = []
        lista += Posorder(arbol.get("izquierda"))
        lista += Posorder(arbol.get("derecha"))
        
        valor = arbol.get("valor")
        if isinstance(valor, str) and not valor.isupper():
            lista.append(valor)
            
        return lista
    return []
    
def agregarNinjas(archivoNinjas):
    intentos = 0
    while intentos < 3:
        nombreNinja = input("Ingrese el nombre del ninja: ").strip()
        if not nombreNinja.isalpha():
            print("Ingrese un solo nombre sin letras ni espacios.")
            intentos += 1
            continue

        nombreExiste = False
        if len(ninjas) != 0:
            for ninja in ninjas:
                if ninja["nombre"].lower() == nombreNinja.lower():
                    print("El ninja ya existe")
                    nombreExiste = True
                    break

        if nombreExiste:
            intentos += 1
            continue
        else:
            break  

    if intentos == 3:
        print("Demasiados intentos fallidos. Intente más tarde.")
        return

    while True:
        puntos = 0
        fuerza = input("Ingrese la fuerza del ninja (1-100): ")
        agilidad = input("Ingrese la velocidad de ataque del ninja (1-100): ")
        if (not agilidad.isdigit() or not 1 <= int(agilidad) <= 100) or (not fuerza.isdigit() or not 1 <= int(fuerza) <= 100):
            print("La agilidad y fuerza del ninja debe ser un número entre 1 y 100")
            continue
        else:
            if int(agilidad) > 50:
                puntos += 4
            else:
                puntos += 2

            if int(fuerza) > 50:
                puntos += 4
            else:
                puntos += 2
        break

    while True:
        print(f'''Ingrese la resistencia del ninja:
        1. Alta (+5 puntos)
        2. Media (+4 puntos)
        3. Baja (+3 puntos)''')
        resistencia = int(input("Ingrese el número de la opción: "))
        if resistencia == 1:
            resistencia = "Alta"
            puntos += 5
            break
        elif resistencia == 2:
            resistencia = "Media"
            puntos += 4
            break
        elif resistencia == 3:
            resistencia = "Baja"
            puntos += 3
            break
        else:
            print("Opción no válida")
            continue

    while True:
        print(f'''Elige el estilo de batalla del Ninja
        1. Ofensivo (50% probabilidad de ganar)
        2. Defensivo (40% probabilidad de ganar)
        3. Mixto (75% probabilidad de ganar)''')
        estilo = int(input("Ingrese el número de la opción: "))
        if estilo == 1:
            estilo = "Ofensivo"
            puntos += 1.5
            habilidades, puntos = habilidadesOfensivas(habilidadesNinjas, puntos)
            break
        elif estilo == 2:
            estilo = "Defensivo"
            puntos += 2
            habilidades, puntos = habilidadesDefensivas(habilidadesNinjas, puntos)
            break
        elif estilo == 3:
            estilo = "Mixto"
            puntos += 1
            habilidades, puntos = habilidadesMixtas(habilidadesNinjas, puntos)
            break
        else:
            print("Opción no válida")
            continue

    h1 = habilidades[0]
    h2 = habilidades[1]
    h3 = habilidades[2]
    h4 = habilidades[3]

    arbolHabilidades = {
        "valor": nombreNinja.upper(),
        "izquierda": {
            "valor": 1,
            "izquierda": {
                "valor": h1,
                "izquierda": None,
                "derecha": None
            },
            "derecha": {
                "valor": h2,
                "izquierda": None,
                "derecha": None
            }
        },
        "derecha": {
            "valor": 2,
            "izquierda": {
                "valor": h3,
                "izquierda": None,
                "derecha": None
            },
            "derecha": {
                "valor": h4,
                "izquierda": None,
                "derecha": None
            }
        }
    }

    ninjaNuevo = {
        "nombre": nombreNinja.upper(),
        "fuerza": fuerza,
        "agilidad": agilidad,
        "resistencia": resistencia,
        "estilo": estilo,
        "habilidades": arbolHabilidades,
        "puntos": puntos,
        "vida": 100,
        "victorias": 0,
        "derrotas": 0,
        "posicion": "8vos de final"
    }
    ninjas.append(ninjaNuevo)

    print(f'''El ninja {nombreNinja} ha sido creado con éxito''')

    with open(archivoNinjas, "w") as archivo:
        for ninja in ninjas:
            formato = str({ninja["nombre"]: ninja}) + "\n"
            archivo.write(formato)
def verNinjas():
    if len(ninjas)==0:
        print("No hay ninjas creados")
        return
    while True:
        print(f'''Elija la foma de listar los ninjas:
            1. Orden de inscripción
            2. Puntos
            3. Nombre''')
        forma=input("Ingrese el número de la opción: ")
        if forma.isdigit():
            if forma == "1":
                for i, ninja in enumerate(ninjas):
                    arbol= ninja["habilidades"]
                    listaHabilidades=Preorder(arbol)
                    print(f'''--------------------Ninja {i+1}--------------------:
                        Nombre: {ninja["nombre"]}
                        Fuerza: {ninja["fuerza"]}
                        Agilidad: {ninja["agilidad"]}
                        Resistencia: {ninja["resistencia"]}
                        Habilidades: {listaHabilidades}
                        Posicion: {ninja["posicion"]}''')
                    print("--------------------------------------------------------\n")
            elif forma == "2":
                lista_ninjas = ninjas.copy()
                n = len(lista_ninjas)

                for i in range(n):
                    for j in range(0, n - i - 1):
                        if lista_ninjas[j]["puntos"] < lista_ninjas[j + 1]["puntos"]:
                            lista_ninjas[j], lista_ninjas[j + 1] = lista_ninjas[j + 1], lista_ninjas[j]

                print("Puntos de los ninjas ordenados de mayor a menor:")
                for ninja in lista_ninjas:
                    arbol = ninja["habilidades"]
                    listaHabilidades = Preorder(arbol)
                    print(f'''--------------------Ninjas con {ninja["puntos"]} puntos--------------------:
                    Nombre: {ninja["nombre"]}
                    Fuerza: {ninja["fuerza"]}
                    Agilidad: {ninja["agilidad"]}
                    Resistencia: {ninja["resistencia"]}
                    Habilidades: {listaHabilidades}
                    Posicion: {ninja["posicion"]}
                    --------------------------------------------------------------------------------\n''')
            elif forma == "3":
                lista_ninjas = ninjas.copy()
                n = len(lista_ninjas)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if lista_ninjas[j]["nombre"].lower() > lista_ninjas[j + 1]["nombre"].lower():
                            lista_ninjas[j], lista_ninjas[j + 1] = lista_ninjas[j + 1], lista_ninjas[j]

                    print("Ninjas ordenados por nombre (alfabéticamente):")
                    for ninja in lista_ninjas:
                        arbol= ninja["habilidades"]
                        listaHabilidades=Preorder(arbol)
                        print(f'''-------------------- Ninja: {ninja["nombre"]} --------------------:
                    Puntos: {ninja["puntos"]}
                    Fuerza: {ninja["fuerza"]}
                    Agilidad: {ninja["agilidad"]}
                    Resistencia: {ninja["resistencia"]}
                    Habilidades: {listaHabilidades}
                    Posicion: {ninja["posicion"]}
                    --------------------------------------------------------------------------------\n''')
            else:
                print("Opción no válida.")
            return
        else:
            print("Opción no válida, Solo números.")
            continue

def buscarNinja():
    if len(ninjas)==0:
        print("No hay ninjas")
        return
    nombre = input("Ingrese el nombre del ninja que desea buscar: ")
    encontrado=False
    for ninja in ninjas:
        if ninja["nombre"].lower() == nombre.lower():
            arbol= ninja["habilidades"]
            listaHabilidades=Preorder(arbol)
            print(f'''-------------------- Ninja: {ninja["nombre"]} --------------------:
                    Puntos: {ninja["puntos"]}
                    Fuerza: {ninja["fuerza"]}
                    Agilidad: {ninja["agilidad"]}
                    Resistencia: {ninja["resistencia"]}
                    Estilo: {ninja["estilo"]}
                    Habilidades: {listaHabilidades}
                    Victorias: {ninja["victorias"]}
                    Derrotas: {ninja["derrotas"]}
                    Posición: {ninja["posicion"]}
                    --------------------------------------------------------------------------------\n''')
            encontrado=True
            break
    if not encontrado:
        print("Ninja no encontrado")
        return
            
def actualizarNinja(archivoNinjas):
    if len(ninjas) == 0:
        print("No hay ninjas registrados.")
        return
    nombre = input("Ingrese el nombre del ninja que desea actualizar: ").strip()
    encontrado = False

    for i, ninja in enumerate(ninjas):
        if ninja["nombre"].lower() == nombre.lower():
            print(f"----------- Ninja encontrado: {ninja['nombre']} -----------")
            encontrado = True
            if ninja["victorias"]>0 or ninja["derrotas"] > 0:
                print("El ninja tiene partidas jugadas, no puede ser actualizado. Esto podría afectar la clasificación del ninja.")
                return

            nombreNinja = input("Ingrese el nuevo nombre del ninja: ").strip()
            if not nombreNinja.isalpha():
                print("Solo se permiten letras en el nombre del ninja.")
                return

            while True:
                fuerza=0
                puntos=0
                fuerza=input("Ingrese la nueva fuerza del ninja (1-100): ")
                agilidad=input("Ingrese la velocidad de ataque del ninja (1-100): ")
                if (not agilidad.isdigit() or not 1 <=int(agilidad)<= 100) or (not fuerza.isdigit() or not 1 <=int(fuerza)<= 100):
                    print("La agilidad y fuerza del ninja debe ser un número entre 1 y 100")
                    continue
                else:
                    if int(agilidad)>50:
                        puntos+=4
                    else:
                        puntos+=2
                    
                    if int(fuerza)>50:
                        puntos+=4
                    else:
                        puntos+=2
                break
            
            while True:
                print(f'''Ingrese la resistencia del ninja:
                    1. Alta (+5 puntos)
                    2. Media (+4 puntos)
                    3. Baja (+3 puntos)''')
                resistencia=int(input("Ingrese el número de la opción: "))
                if resistencia == 1:
                    resistencia = "Alta"
                    puntos+=5
                    break
                elif resistencia == 2:
                    resistencia = "Media"
                    puntos+=4
                    break
                elif resistencia == 3:
                    resistencia = "Baja"
                    puntos+=3
                    break
                else:
                    print("Opción no válida")
                    continue
            
            while True:
                print(f'''Elige el estilo de batalla del Ninja
                    1. Ofensivo (50% probabilidad de ganar)
                    2. Defensivo (40% probabilidad de ganar)
                    3. Mixto (75% probabilidad de ganar)''')
                estilo=int(input("Ingrese el número de la opción: "))
                if estilo == 1:
                    estilo = "Ofensivo"
                    puntos+=1.5
                    habilidades, puntos=habilidadesOfensivas(habilidadesNinjas,puntos)
                    break
                elif estilo == 2:
                    estilo = "Defensivo"
                    puntos+=2
                    habilidades,puntos=habilidadesDefensivas(habilidadesNinjas,puntos)
                    break
                elif estilo == 3:
                    estilo = "Mixto"
                    puntos+=1
                    habilidades,puntos=habilidadesMixtas(habilidadesNinjas,puntos)
                    break
                else:
                    print("Opción no válida")
                    continue 
            h1= habilidades[0]
            h2= habilidades[1]
            h3= habilidades[2]
            h4= habilidades[3]
            arbolHabilidades={"valor":nombreNinja.upper(),
                            "izquierda":{"valor":1,
                                        "izquierda":{
                                            "valor":h1,
                                            "izquierda":None,
                                            "derecha":None
                                        },
                                        "derecha":{
                                            "valor":h2,
                                            "izquierda":None,
                                            "derecha": None
                                        }},
                            "derecha":{"valor": 2,
                                        "izquierda":{
                                            "valor":h3,
                                            "izquierda":None,
                                            "derecha":None
                                        },
                                        "derecha":{
                                            "valor":h4,
                                            "izquierda":None,
                                            "derecha": None
                                        }}}
            ninjaNuevo = {
                "nombre": nombreNinja.upper(),
                "fuerza": fuerza,
                "agilidad": agilidad,
                "resistencia": resistencia,
                "estilo": estilo,
                "habilidades": arbolHabilidades,
                "puntos": puntos,
                "vida":100,
                "victorias":0,
                "derrotas":0,
                "posicion":"8vos de final"
            }

            ninjas[i] = ninjaNuevo
            print(f"El ninja {nombreNinja} ha sido actualizado con éxito.")
            break

    if not encontrado:
        print("Ninja no encontrado.")
        return

    with open(archivoNinjas, "w") as archivo:
        for ninja in ninjas:
            archivo.write(str({ninja["nombre"]: ninja}) + "\n")

def eliminarNinja(archivoNinjas):
    nombreNinja = input("Ingrese el nombre del ninja a eliminar: ")
    encontrado = False
    for i in range(len(ninjas)):
        if ninjas[i]["nombre"].lower() == nombreNinja.lower():
            del ninjas[i]
            print("ELIMINADO CON ÉXITO")
            encontrado = True
            break
    with open(archivoNinjas, "w") as archivo:
        for ninja in ninjas:
            archivo.write(str({ninja["nombre"]: ninja}) + "\n")
    if not encontrado:
        print("Ninja no encontrado.")
        return

def menuAdministrador(usuario,contraseña):
    if usuario=="admin" and contraseña=="admin":
        while True:
            print("Bienvenido al menú de administrador")
            print("1. Agregar Ninjas")
            print("2. Ver Ninjas")
            print("3. Buscar Ninjas")
            print("4. Actualizar Ninja")
            print("5. Eliminar Ninja")
            print("6. Salir")
            opcion = input("Ingrese la opción que desee: ")
            match opcion:
                case "1":
                    agregarNinjas(archivoNinjas)
                case "2":
                    verNinjas()
                case "3":
                    buscarNinja()
                case "4":
                    actualizarNinja(archivoNinjas)
                case "5":
                    eliminarNinja(archivoNinjas)
                case "6":
                    print("Hasta luego")
                    return
                case _:
                    print("Opción no válida")
                    continue
    else:
        print("Contraseña o usuario incorrectos. Acceso denegado")
        return

def puntajes(habilidad):
    
    puntaje =0
    if habilidad in habilidadesNinjas["Habilidades Ofensivas"]["Kenjutsu (corto alcance)"]:
        puntaje=20
    elif habilidad in habilidadesNinjas["Habilidades Ofensivas"]["Sojutsu (Arma Lanzable)"]:
        puntaje=30
    elif habilidad in habilidadesNinjas["Habilidades Ofensivas"]["Taijutsu (cuerpo a cuerpo)"]:
        puntaje=34
    elif habilidad in habilidadesNinjas["Habilidades Ofensivas"]["Ninjutsu (Habilidades magicas)"]:
        puntaje=50
    elif habilidad in habilidadesNinjas["Habilidades Defensivas"]["Kumai (Escudo)"]:
        puntaje=0.4
    elif habilidad in habilidadesNinjas["Habilidades Defensivas"]["Hichy (camuflaje)"]:
        puntaje=1
    elif habilidad in habilidadesNinjas["Habilidades Defensivas"]["Blink (bloqueo)"]:
        puntaje=0.6
    
    return puntaje

def combate():
    print("Puedes simular un combate de única batalla")
    print("Este combate es solo de práctica no afecta tu clasificación general del torneo")
    print("Selecciona tu Ninja preferido")
    verNinjas()
    nombreNinjaUsuario = input("Ingrese el nombre del ninja que desee: ")
    
    if nombreNinjaUsuario.isalpha():
        for ninja in ninjas:
            if nombreNinjaUsuario.upper() == ninja["nombre"]:
                habilidadesNinjaElegido = ninja["habilidades"]
                print("Ninja seleccionado: ", nombreNinjaUsuario.upper())
                
                while True:
                    print(f'''¿Qué tipo de ataque deseas que tenga tu Ninja?
                        1. Defensivo
                        2. Ofensivo
                        3. Equilibrado''')
                    opcion = input("Ingrese la opción que desee: ")
                    
                    if opcion.isdigit():
                        match opcion:
                            case "1":
                                ataque = Posorder(habilidadesNinjaElegido)
                                print("Ataque Defensivo: ", ataque)
                                break
                            case "2":
                                ataque = Preorder(habilidadesNinjaElegido)
                                print("Ataque Ofensivo: ", ataque)
                                break
                            case "3":
                                ataque = Inorder(habilidadesNinjaElegido)
                                print("Ataque Equilibrado: ", ataque)
                                break
                            case _:
                                print("Opción no válida")
                    else:
                        print("Opción no válida")

                print("Selecciona tu rival:")
                verNinjas()
                nombreNinjaRival = input("Ingrese el nombre del ninja que desee: ")
                
                if nombreNinjaRival.isalpha():
                    for ninja in ninjas:
                        if nombreNinjaRival.upper() == ninja["nombre"]:
                            habilidadesNinjaRival = ninja["habilidades"]
                            print("Rival seleccionado: ", nombreNinjaRival)
                            print("La computadora está seleccionando el ataque del rival...")
                            
                            aleatorio = random.randint(1, 3)
                            match aleatorio:
                                case 1:
                                    ataqueRival = Posorder(habilidadesNinjaRival)
                                case 2:
                                    ataqueRival = Preorder(habilidadesNinjaRival)
                                case 3:
                                    ataqueRival = Inorder(habilidadesNinjaRival)

                            print("Ataque del rival: ", ataqueRival)
                            print("El mejor de 3 gana la partida...")
                            print("Si uno gana 2 rondas seguidas gana la partida")
                            print("Si ambos ganan una ronda, la partida sigue hasta la tercera ronda")
                            print("\n-------------------------EL COMBATE HA EMPEZADO----------------------------\n")
                            
                            vidaElegido = 100
                            vidaRival = 100
                            victoriasAmigas = 0
                            victoriasRival = 0
                            rondas = 1
                            contador = 0

                            while True:
                                print("\nContador victorias:    TÚ:", victoriasAmigas, " RIVAL:", victoriasRival)
                                print("\n-------------------------RONDA N°", rondas, "----------------------------\n")
                                print("Tu vida es: ", vidaElegido, " ------- la vida de tu rival es: ", vidaRival)
                                
                                puntajeAmigo = puntajes(ataque[contador])
                                puntajeRival = puntajes(ataqueRival[contador])
                                
                                print(f'''Tu habilidad tirada fue {ataque[contador]} --------------- La habilidad tirada de tu rival fue {ataqueRival[contador]}''')

                                if puntajeAmigo <= 1 and puntajeRival <= 1:
                                    print("Ambos ninjas han tirado habilidades defensivas\n")
                                    print("Empate\n")
                                
                                elif puntajeAmigo <= 1 and puntajeRival > 1:
                                    print("Tu rival ha tirado una habilidad ofensiva y tú una defensiva\n")
                                    vidaElegido -= puntajeRival * puntajeAmigo
                                    vidaRival -= puntajeRival * (puntajeAmigo + 0.2)

                                elif puntajeAmigo > 1 and puntajeRival <= 1:
                                    print("Tu rival ha tirado una habilidad defensiva y tú una ofensiva\n")
                                    vidaRival -= puntajeAmigo * puntajeRival
                                    vidaElegido -= puntajeAmigo * (puntajeRival + 0.2)

                                elif puntajeAmigo > 1 and puntajeRival > 1:
                                    print("Ambos ninjas han tirado habilidades ofensivas\n")
                                    vidaElegido -= puntajeRival
                                    vidaRival -= puntajeAmigo

                                vidaElegido = max(0, vidaElegido)
                                vidaRival = max(0, vidaRival)

                                print("Tu vida es: ", vidaElegido, " ------- la vida de tu rival es: ", vidaRival)

                                if vidaElegido == 0 and vidaRival == 0:
                                    print("Ambos ninjas han muerto\nNinguno obtiene punto")
                                
                                elif vidaElegido == 0:
                                    print("Tu rival ha ganado la ronda\n")
                                    victoriasRival += 1
                                    rondas += 1
                                    vidaElegido = 100
                                    vidaRival = 100
                                
                                elif vidaRival == 0:
                                    print("Tú has ganado la ronda\n")
                                    victoriasAmigas += 1
                                    rondas += 1
                                    vidaElegido = 100
                                    vidaRival = 100
                                
                                print("\n-----------------------------FIN RONDA -------------------------------\n")

                                contador = (contador + 1) % len(ataque)

                                if victoriasAmigas == 2:
                                    print("¡Tú has ganado la partida!\nFelicidades al ganador\n")
                                    return
                                elif victoriasRival == 2:
                                    print("Tu rival ha ganado la partida\nSigamos practicando, has jugado una buena partida\n")
                                    return

                                time.sleep(10)
                else:
                    print("El nombre del rival debe contener solo letras")
                    continue

        print("El nombre del ninja no coincide con ninguno")
        return
    else:
        print("El nombre del ninja solo debe tener letras")


def torneo(archivoNinjas, archivoJugador):
    if len(ninjas) < 2:
        print("Se necesitan al menos 2 ninjas para un torneo.")
        return

    print("\n--- ¡COMIENZA EL GRAN TORNEO NINJA! ---")
    
   
    participantes = ninjas.copy()
    random.shuffle(participantes)
    
    cola_torneo = deque(participantes)
    ronda_actual = 1
    
   
    with open(archivoCombates, "a") as historial:
        while len(cola_torneo) > 1:
            print(f"\n--- RONDA {ronda_actual} --- ({len(cola_torneo)} participantes) ---")
            ganadores = deque()
            
            while len(cola_torneo) >= 2:
                ninja1 = cola_torneo.popleft()
                ninja2 = cola_torneo.popleft()
                
                print(f"\nPróximo combate: {ninja1['nombre']} vs {ninja2['nombre']}")
                time.sleep(2)
                
                
                vida1, vida2 = 100, 100
                habilidades1, habilidades2 = Preorder(ninja1['habilidades']), Preorder(ninja2['habilidades'])
                
                for i in range(min(len(habilidades1), len(habilidades2))):
                    puntaje1 = puntajes(habilidades1[i])
                    puntaje2 = puntajes(habilidades2[i])
                    
                    if puntaje1 > 1: vida2 -= puntaje1
                    if puntaje2 > 1: vida1 -= puntaje2
                
                if vida1 < 0: vida1 = 0
                if vida2 < 0: vida2 = 0
                
                
                if vida1 >= vida2:
                    ganador = ninja1
                    perdedor = ninja2
                else:
                    ganador = ninja2
                    perdedor = ninja1
                
                print(f"Resultado de vida -> {ninja1['nombre']}: {vida1}/100 | {ninja2['nombre']}: {vida2}/100")
                
                print(f"Ganador del combate: {ganador['nombre']}!")
                ganadores.append(ganador) 
                
                
               
                for n in ninjas:
                    if n['nombre'] == ganador['nombre']:
                        n['victorias'] += 1
                        n['posicion'] = f"Ronda {ronda_actual+1}"
                    if n['nombre'] == perdedor['nombre']:
                        n['derrotas'] += 1
                        n['posicion'] = f"Eliminado en Ronda {ronda_actual}"
                
                
                fecha_actual = time.strftime('%d-%m-%Y')
                log = f"{ninja1['nombre']} vs {ninja2['nombre']} – Ganador: {ganador['nombre']} – Fecha: {fecha_actual}\n"
                historial.write(log)

            
            if len(cola_torneo) == 1:
                sobreviviente = cola_torneo.popleft()
                print(f"{sobreviviente['nombre']} pasa a la siguiente ronda sin combatir.")
                ganadores.append(sobreviviente)
            
            cola_torneo = ganadores
            ronda_actual += 1

    campeon = cola_torneo.popleft()
    campeon['posicion'] = "Campeón del Torneo"
    print(f"\n¡¡¡EL CAMPEÓN DEL TORNEO ES {campeon['nombre']}!!!")

    
    with open(archivoNinjas, "w") as archivo:
        for ninja in ninjas:
            archivo.write(str({ninja["nombre"]: ninja}) + "\n")
    
    print("El torneo ha finalizado y los resultados han sido guardados.")


def verRanking(archivoJugador):
    if not ninjas:
        print("No hay ninjas para mostrar un ranking.")
        return
    
    
    lista_ordenada = ninjas.copy()
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j]["victorias"] < lista_ordenada[j + 1]["victorias"]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    
    print("\n--- RANKING DE VICTORIAS ---")
    for i, ninja in enumerate(lista_ordenada):
        print(f"{i+1}. {ninja['nombre']} - Victorias: {ninja['victorias']}, Derrotas: {ninja['derrotas']}")

def guardarProgreso(archivoJugador):
    
    try:
        with open(archivoJugador, 'w') as f:
            f.write(f"Resumen de combates para {archivoJugador.split('.')[0]}:\n")
            
            print(f"Progreso guardado en {archivoJugador}")
    except Exception as e:
        print(f"No se pudo guardar el progreso: {e}")


def accionesJugador(nombre):
    archivoJugador = nombre+".txt"
    if not os.path.exists(archivoJugador):
        pass
    if len(ninjas)==0:
        print("No hay ninjas registrados pide al administrador que genere ninjas apra jugar")
        return
    print("\n-------------MENÚ DE JUEGO-----------\n")
    while True:
        print(f'''
            1. Ver ninjas disponibles
            2. Combate
            3. Torneo
            4. Ver ranking 
            5. Guardar Progreso
            6. Salir''')
        opcion = input("Ingrese la opción que desee: ")
        match opcion:
            case "1":
                verNinjas()
            case "2":
                combate()
            case "3":
                torneo(archivoNinjas, archivoJugador)
            case "4":
                verRanking(archivoJugador)
            case "5":
                guardarProgreso(archivoJugador)
            case "6":
                print("Hasta luego")
                return
            case _:
                print("Opción no válida")
                continue
            

def iniciarSesion(archivoUsuarios):
    if not os.path.exists(archivoUsuarios):
        print("No hay usuarios registrados")
        return

    usuario_input = input("Ingrese su usuario: ")
    contraseña_input = input("Ingrese su contraseña: ")

    autenticado = False
    usuario_encontrado = None

    with open(archivoUsuarios, "r") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue
            
            try:
                
                user_data = eval(linea.strip())
                if user_data.get("usuario") == usuario_input and user_data.get("contraseña") == contraseña_input:
                    autenticado = True
                    usuario_encontrado = user_data
                    break 
            except Exception as e:
                print(f"Advertencia: Se encontró una línea corrupta en el archivo de usuarios. {e}")
    
    if autenticado:
        print(f'''Bienvenido {usuario_encontrado["nombre"]}''')
        accionesJugador(usuario_encontrado["nombre"])
    else:
        print("Usuario o contraseña incorrectos")

def menuJugador():
    while True:
        print(f'''--------MENÚ INICIO DE SESIÓN NINJAS--------
            1. INICIAR SESIÓN
            2. REGISTRARSE
            3. SALIR''')
        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1":
                iniciarSesion(archivoUsuarios)
            case "2":
                registrarse(archivoUsuarios)
            case "3":
                print("Adiós")
                return
            case _:
                print("Opción no válida")
                continue

def menuPrincipal():
    cargarusuarios(archivoUsuarios)
    cargarNinjas(archivoNinjas)
    while True:
        print(f'''--------MENÚ PRINCIPAL--------
              1. Administrador
              2. Jugador
              3. SALIR''')
        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1":
                usuario=input("Ingrese su usuario: ")
                contraseña=input("Ingrese su contraseña: ")
                menuAdministrador(usuario,contraseña)
            case "2":
                menuJugador()
            case "3":
                print("Adiós")
                return
            case _:
                print("Opción no válida")

menuPrincipal()
