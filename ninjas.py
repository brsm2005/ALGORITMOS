#Bryan Salvador
import os
import random
archivoUsuarios="usuarios.txt"
archivoNinjas="ninjas.txt"
usuarios=[]
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
    archivo = open(archivousuarios, "r")
    for linea in archivo:
        usuario=linea.strip()
        usuarios.append(usuario)
        
def registrarse(archivoUsuarios):
    if not os.path.exists(archivoUsuarios):
        try:
            nombreUsuario = input("Ingrese su nombre y apellido: ").strip()
            palabras = nombreUsuario.split()
            if len(palabras) != 2:
                print("Debe ingresar solo nombre y apellido")
            else:
                if all(palabra.isalpha() for palabra in palabras):
                    usuario = f"{palabras[0].lower()}.{palabras[1].lower()}@gmail.com"
                else:
                    print("Solo se permiten letras en el nombre y apellido.")
                    return registrarse(archivoUsuarios)
        except:
            print("Ocurrió un error")
        identificacion=input("Ingrese su cédula: ")
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
                print("Solo se permiten números en la cédula.")
                return registrarse(archivoUsuarios)
        except:
            print("Ocurrió un error")
        for i in range(len(usuarios)):
            if usuarios[i]["usuario"]==usuario.lower() or usuarios[i]["identificacion"]==identificacion:
                print("El usuario ya existe")
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
    ninjas=[]
    if not os.path.exists(archivoNinjas):
        return ninjas
    with open(archivoNinjas,"r") as archivo:
        for linea in archivo:
            ninja_dict = eval(linea.strip())
            for ninja in ninja_dict.values():
                ninjas.append(ninja)
    return ninjas

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

def agregarNinjas(archivoNinjas):
    ninjas=cargarNinjas(archivoNinjas)
    nombreNinja = input("Ingrese el nombre del ninja: ").strip()
    if not nombreNinja.isalpha():
        print("Solo se permiten letras en el nombre del ninja.")
        return

    for ninja in ninjas:
        if ninja["nombre"].lower() == nombreNinja.lower():
            print("El ninja ya existe")
            return
    
    while True:
        puntos=0
        fuerza=0
        fuerza=input("Ingrese la fuerza del ninja (1-100): ")
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
            habilidades, puntos=habilidadesDefensivas(habilidadesNinjas,puntos)
            break
        elif estilo == 3:
            estilo = "Mixto"
            puntos+=1
            habilidades, puntos=habilidadesMixtas(habilidadesNinjas,puntos)
            break
        else:
            print("Opción no válida")
            continue
    ninjaNuevo={"nombre": nombreNinja.upper(),"fuerza":fuerza,"agilidad":agilidad,"resistencia":resistencia,"estilo":estilo,"habilidades":habilidades,"puntos":puntos,"vida":100,"victorias":0,"derrotas":0,"posicion":"8vos de final"}
    ninjas.append(ninjaNuevo)
    print(f'''El ninja {nombreNinja} ha sido creado con éxito''')
    with open(archivoNinjas, "w") as archivo:
        for ninja in ninjas:
            formato=str({ninja["nombre"]:ninja})+"\n"
            archivo.write(formato)

def verNinjas(archivoNinjas):
    ninjas=cargarNinjas(archivoNinjas)
    if len(ninjas)==0:
        print("No hay ninjas creados")
        return
    print(f'''Elija la foma de lsitar los ninjas:
          1. Orden de inscripción
          2. Puntos
          3. Nombre''')
    forma=int(input("Ingrese el número de la opción: "))
    if forma == 1:
        for i, ninja in enumerate(ninjas):
            print(f'''--------------------Ninja {i+1}--------------------:
                Nombre: {ninja["nombre"]}
                Fuerza: {ninja["fuerza"]}
                Agilidad: {ninja["agilidad"]}
                Resistencia: {ninja["resistencia"]}
                Estilo: {ninja["estilo"]}
                Habilidades: {ninja["habilidades"]}
                Puntos: {ninja["puntos"]}
                Victorias: {ninja["victorias"]}
                Derrotas: {ninja["derrotas"]}
                Posicion: {ninja["posicion"]}''')
            print("--------------------------------------------------------\n")
    elif forma == 2:
        lista_ninjas = ninjas.copy()
        n = len(lista_ninjas)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista_ninjas[j]["puntos"] < lista_ninjas[j + 1]["puntos"]:
                    lista_ninjas[j], lista_ninjas[j + 1] = lista_ninjas[j + 1], lista_ninjas[j]
            print("Puntos de los ninjas ordenados de mayor a menor:")
            for ninja in lista_ninjas:
                print(f'''--------------------Ninjas con {ninja["puntos"]} puntos--------------------:
            Nombre: {ninja["nombre"]}
            Fuerza: {ninja["fuerza"]}
            Agilidad: {ninja["agilidad"]}
            Resistencia: {ninja["resistencia"]}
            Estilo: {ninja["estilo"]}
            Habilidades: {ninja["habilidades"]}
            --------------------------------------------------------------------------------\n''')
    elif forma == 3:
        lista_ninjas = ninjas.copy()
        n = len(lista_ninjas)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista_ninjas[j]["nombre"].lower() > lista_ninjas[j + 1]["nombre"].lower():
                    lista_ninjas[j], lista_ninjas[j + 1] = lista_ninjas[j + 1], lista_ninjas[j]

            print("Ninjas ordenados por nombre (alfabéticamente):")
            for ninja in lista_ninjas:
                print(f'''-------------------- Ninja: {ninja["nombre"]} --------------------:
            Puntos: {ninja["puntos"]}
            Fuerza: {ninja["fuerza"]}
            Agilidad: {ninja["agilidad"]}
            Resistencia: {ninja["resistencia"]}
            Estilo: {ninja["estilo"]}
            Habilidades: {ninja["habilidades"]}
            --------------------------------------------------------------------------------\n''')
    else:
        print("Opción no válida.")
        return

def buscarNinja(archivoNinjas):
    ninjas=cargarNinjas(archivoNinjas)
    if len(ninjas)==0:
        print("No hay ninjas")
        return
    nombre = input("Ingrese el nombre del ninja que desea buscar: ")
    encontrado=False
    for ninja in ninjas:
        if ninja["nombre"].lower() == nombre.lower():
            print(f'''-------------------- Ninja: {ninja["nombre"]} --------------------:
                    Puntos: {ninja["puntos"]}
                    Fuerza: {ninja["fuerza"]}
                    Agilidad: {ninja["agilidad"]}
                    Resistencia: {ninja["resistencia"]}
                    Estilo: {ninja["estilo"]}
                    Habilidades: {ninja["habilidades"]}
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
    ninjas = cargarNinjas(archivoNinjas)
    if len(ninjas) == 0:
        print("No hay ninjas registrados.")
        return
    nombre = input("Ingrese el nombre del ninja que desea actualizar: ").strip()
    encontrado = False

    for i, ninja in enumerate(ninjas):
        if ninja["nombre"].lower() == nombre.lower():
            print(f"----------- Ninja encontrado: {ninja['nombre']} -----------")
            encontrado = True
            if ninja["puntos"]>0:
                print("El ninja tiene puntos, no puede ser actualizado")
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

            ninjaNuevo = {
                "nombre": nombreNinja.upper(),
                "fuerza": fuerza,
                "agilidad": agilidad,
                "resistencia": resistencia,
                "estilo": estilo,
                "habilidades": habilidades,
                "puntos": puntos,
                "vida":100,
                "victorias":0,
                "derrotas":0
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
    ninjas = cargarNinjas(archivoNinjas)
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
                    verNinjas(archivoNinjas)
                case "3":
                    buscarNinja(archivoNinjas)
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

def iniciarSesion(archivoUsuarios):
    if not os.path.exists(archivoUsuarios):
        print("No hay usuarios registrados")
        return
    with open(archivoUsuarios,"r") as archivo:
        while True:    
            usuario=input("Ingrese su usuario: ")
            contraseña=input("Ingrese su contraseña: ")
            for linea in archivo:
                User=eval(linea.strip())
            if User["usuario"]==usuario and User["contraseña"]==contraseña:
                print(f'''Bienvenido {User["nombre"]}''')
                return #MENU
            else:
                print("Usuario o contraseña incorrectos")
                continue

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

#PUNTAJES: VICTORIAS +11, DERROTAS -5.5, A.MIXTO 1, A.OFENSIVO 1.5, A.DEFENSIVO 2