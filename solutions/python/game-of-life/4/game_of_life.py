def tick(matrix):

    direciones = [
        (-1,-1), (-1, 0), (-1, 1),
        (0,-1), (0,1),
        (1, -1), (1,0), (1,1)
    ]

    len_x = len(matrix)

    len_y = 0
    if len_x > 0:
        len_y = len(matrix[0])

    resultado = [[0 for i in range(len_y)] for e in range(len_x)]

    for indice_x in range(len_x):

        for indice_y in range(len_y):

            vecinos = 0
            
            for dx, dy in direciones:

                if 0 <= indice_x+dx < len_x and 0 <= indice_y+dy < len_y:

                    vecinos += matrix[indice_x+dx][indice_y+dy]


            if matrix[indice_x][indice_y] and (2 <= vecinos <= 3):
                resultado[indice_x][indice_y] = matrix[indice_x][indice_y]

            elif not matrix[indice_x][indice_y] and vecinos == 3:
                resultado[indice_x][indice_y] = 1

            else:
                resultado[indice_x][indice_y] = 0

    return resultado
