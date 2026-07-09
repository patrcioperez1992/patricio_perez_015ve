libros = {
    'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
    'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
    'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
    'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
    'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
    'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False],
}

prestamos = {
    'L001': [500, 4],
    'L002': [700, 0],
    'L003': [300, 10],
    'L004': [400, 2],
    'L005': [600, 1],
    'L006': [350, 6],
}
def copias_genero(genero):
    total = 0
    genero = genero.lower()

    for codigo in libros:
        if libros[codigo][2].lower() == genero:
            total += prestamos[codigo][1]
    print(f"El total de copias es: {total}")

def busqueda_multa(multa_min, multa_max):
    lista = []
    for codigo in prestamos:
        multa = prestamos[codigo][0]
        copias = prestamos[codigo][1]
        if multa_min <= multa <= multa_max and copias != 0:
            titulo = libros[codigo][0]
            lista.append(titulo + "--" + codigo)

    lista.sort()
    if len(lista) == 0:
        print("No hay libros en ese rango de multa.")
    else:
        print(f"Los libros encontrados son: {lista}")


def actualizar_multa(codigo, nueva_multa):
    codigo = codigo.upper()
    if codigo in prestamos:
        prestamos[codigo][0] = nueva_multa
        return True
    else:
        return False


def agregar_libro(codigo, titulo, autor, genero, anio, editorial,
                  es_novedad, precio_multa, copias_disponibles):

    codigo = codigo.upper()
    if codigo in libros:
        return False
    libros[codigo] = [
        titulo,
        autor,
        genero,
        anio,
        editorial,
        es_novedad
    ]
    prestamos[codigo] = [
        precio_multa,
        copias_disponibles
    ]
    return True

def eliminar_libro(codigo):
    codigo = codigo.upper()

    if codigo in libros:
        del libros[codigo]
        del prestamos[codigo]
        return True
    else:
        return False

def validar_codigo(codigo):
    codigo = codigo.strip()
    if codigo == "":
        return False
    if codigo.upper() in libros:
        return False
    return True

def validar_texto(texto):
    return texto.strip() != ""

def validar_anio(anio):
    return anio > 0

def validar_novedad(valor):
    return valor.lower() == "s" or valor.lower() == "n"

def validar_multa(multa):
    return multa > 0

def validar_copias(copias):
    return copias >= 0

while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Copias por género")
    print("2. Búsqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6. Salir")
    print("=====================================")

    opcion = input("Ingrese opcion: ")
    if opcion == "1":
        genero = input("Ingrese genero a consultar: ")
        copias_genero(genero)

    elif opcion == "2":
        while True:
            try:
                multa_min = int(input("Ingrese multa minima: "))
                multa_max = int(input("Ingrese multa maxima: "))
                if multa_min >= 0 and multa_max >= 0 and multa_min <= multa_max:
                    break
                else:
                    print("Debe ingresar un rango valido.")
            except:
                print("Debe ingresar valores enteros")
        busqueda_multa(multa_min, multa_max)

    elif opcion == "3":
        while True:
            codigo = input("Ingrese codigo del libro: ").upper()
            while True:
                try:
                    nueva_multa = int(input("Ingrese nueva multa: "))
                    if nueva_multa > 0:
                        break
                    else:
                        print("La multa debe ser positiva.")
                except:
                    print("Debe ingresar un numero entero.")
            if actualizar_multa(codigo, nueva_multa):
                print("Multa actualizada")
            else:
                print("El codigo no existe")
            repetir = input("¿Desea actualizar otra multa (s/n)?: ").lower()
            if repetir == "n":
                break

    elif opcion == "4":
        codigo = input("Ingrese codigo del libro: ").upper()
        if not validar_codigo(codigo):
            print("Codigo invalido o ya existe.")
            continue
        titulo = input("Ingrese titulo: ")
        if not validar_texto(titulo):
            print("Titulo invalido.")
            continue
        autor = input("Ingrese autor: ")
        if not validar_texto(autor):
            print("Autor invalido.")
            continue
        genero = input("Ingrese genero: ")
        if not validar_texto(genero):
            print("Genero invalido.")
            continue
        try:
            anio = int(input("Ingrese año de publicación: "))
        except:
            print("Año invalido.")
            continue
        if not validar_anio(anio):
            print("Año invalido.")
            continue
        editorial = input("Ingrese editorial: ")
        if not validar_texto(editorial):
            print("Editorial invalida.")
            continue
        novedad = input("¿Es novedad? (s/n): ").lower()
        if not validar_novedad(novedad):
            print("Valor invalido.")
            continue
        es_novedad = novedad == "s"
        try:
            multa = int(input("Ingrese precio de multa: "))
        except:
            print("Multa invalida.")
            continue
        if not validar_multa(multa):
            print("Multa invalida.")
            continue
        try:
            copias = int(input("Ingrese copias disponibles: "))
        except:
            print("Cantidad invalida.")
            continue
        if not validar_copias(copias):
            print("Cantidad invalida.")
            continue
        if agregar_libro(codigo, titulo, autor, genero, anio,
                         editorial, es_novedad, multa, copias):
            print("Libro agregado")
        else:
            print("El codigo ya existe")

    elif opcion == "5":
        codigo = input("Ingrese codigo del libro: ").upper()
        if eliminar_libro(codigo):
            print("Libro eliminado")
        else:
            print("El codigo no existe")

    elif opcion == "6":
        print("Programa finalizado.")
        break
    else:
        print("Debe seleccionar una opcion valida")
















































