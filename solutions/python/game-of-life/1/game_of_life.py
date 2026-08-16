def tick(matrix):

    DIRECCIONES = [
        (-1,-1), (-1, 0), (-1, 1),
        (0,-1), (0,1),
        (1, -1), (1,0), (1,1)
    ]

    LEN_X = len(matrix)

    LEN_Y = 0
    if LEN_X > 0:
        LEN_Y = len(matrix[0])

    resultado = [[0 for _ in range(LEN_Y)] for _ in range(LEN_X)]

    for x in range(LEN_X):

        for y in range(LEN_Y):

            vecinos = 0
            
            for dx, dy in DIRECCIONES:

                if 0 <= x+dx < LEN_X and 0 <= y+dy < LEN_Y:

                    vecinos += matrix[x+dx][y+dy]


            if matrix[x][y] and (2 <= vecinos <= 3):
                resultado[x][y] = matrix[x][y]

            elif not matrix[x][y] and vecinos == 3:
                resultado[x][y] = 1

            else:
                resultado[x][y] = 0

    return resultado
