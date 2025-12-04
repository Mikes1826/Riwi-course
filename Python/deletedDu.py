def deletDup():
    large = int(input("¿Cuántas palabras quieres ingresar?: "))
    array = []
    sinDup = []
    
    # 1. Primero recoger todos los datos
    for i in range(large):
        text = input(f"Ingresa palabra {i+1}: ")
        array.append(text)
    
    # 2. Luego eliminar duplicados
    for palabra in array:
        # Verificar si la palabra ya está en sinDup
        encontrada = False
        for existente in sinDup:
            if palabra == existente:
                encontrada = True
                break
        
        # Si no fue encontrada, añadirla
        if not encontrada:
            sinDup.append(palabra)
    
    return f"Lista completa: {array}, Lista sin duplicados: {sinDup}"

print(deletDup())