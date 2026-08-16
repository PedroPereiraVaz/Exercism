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

    resultado = [[0 for _ in range(len_y)] for _ in range(len_x)]

    for x in range(len_x):

        for y in range(len_y):

            vecinos = 0
            
            for dx, dy in direciones:

                if 0 <= x+dx < len_x and 0 <= y+dy < len_y:

                    vecinos += matrix[x+dx][y+dy]


            if matrix[x][y] and (2 <= vecinos <= 3):
                resultado[x][y] = matrix[x][y]

            elif not matrix[x][y] and vecinos == 3:
                resultado[x][y] = 1

            else:
                resultado[x][y] = 0

    return resultado
