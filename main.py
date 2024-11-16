from random import randint as rand
from time import sleep

# все символы
"█░▓▒"


# функция по добавлению и обнулению матрицы
def create_matrix():
    return [['░' for i in range(50)]
            for j in range(25)]


# функция по созданию новой рандомной жизни (семечко)
def new_life(pole):
    iplace_with_life = rand(1, 23)
    jplace_with_life = rand(1, 48)
    pole[iplace_with_life][jplace_with_life] = '█'
    if rand(1, 2) == 1:
        pole[iplace_with_life - 1][jplace_with_life - 1] = '█'
    if rand(1, 2) == 1:
        pole[iplace_with_life - 1][jplace_with_life] = '█'
    if rand(1, 2) == 1:
        pole[iplace_with_life - 1][jplace_with_life + 1] = '█'
    if rand(1, 2) == 1:
        pole[iplace_with_life][jplace_with_life - 1] = '█'
    if rand(1, 2) == 1:
        pole[iplace_with_life][jplace_with_life + 1] = '█'
    if rand(1, 2) == 1:
        pole[iplace_with_life + 1][jplace_with_life - 1] = '█'
    if rand(1, 2) == 1:
        pole[iplace_with_life + 1][jplace_with_life] = '█'
    if rand(1, 2) == 1:
        pole[iplace_with_life + 1][jplace_with_life + 1] = '█'


def new_life_2(pole):
    iplac_with_life = rand(1, 23)
    jplac_with_life = rand(1, 48)
    pole[iplac_with_life][jplac_with_life] = '▒'
    if rand(1, 2) == 1:
        pole[iplac_with_life - 1][jplac_with_life - 1] = '▒'
    if rand(1, 2) == 1:
        pole[iplac_with_life - 1][jplac_with_life] = '▒'
    if rand(1, 2) == 1:
        pole[iplac_with_life - 1][jplac_with_life + 1] = '▒'
    if rand(1, 2) == 1:
        pole[iplac_with_life][jplac_with_life - 1] = '▒'
    if rand(1, 2) == 1:
        pole[iplac_with_life][jplac_with_life + 1] = '▒'
    if rand(1, 2) == 1:
        pole[iplac_with_life + 1][jplac_with_life - 1] = '▒'
    if rand(1, 2) == 1:
        pole[iplac_with_life + 1][jplac_with_life] = '▒'
    if rand(1, 2) == 1:
        pole[iplac_with_life + 1][jplac_with_life + 1] = '▒'


# стенки
def wall(pole):
    for i in range(25):
        pole[i][0] = '▓'
        pole[i][49] = '▓'
    for j in range(50):
        pole[0][j] = '▓'
        pole[0][24] = '▓'


# функция для осмотра ближайших клеток
def osmotr(matrix, ii, jj):
    kk = 0
    if matrix[ii - 1][jj - 1] == '█':
        kk += 1
    if matrix[ii - 1][jj] == '█':
        kk += 1
    if matrix[ii - 1][jj + 1] == '█':
        kk += 1
    if matrix[ii][jj - 1] == '█':
        kk += 1
    if matrix[ii][jj + 1] == '█':
        kk += 1
    if matrix[ii + 1][jj - 1] == '█':
        kk += 1
    if matrix[ii + 1][jj] == '█':
        kk += 1
    if matrix[ii + 1][jj + 1] == '█':
        kk += 1
    return kk


def osmotr2(matrix, ii, jj):
    pp = 0
    if matrix[ii - 1][jj - 1] == '▒':
        pp += 1
    if matrix[ii - 1][jj] == '▒':
        pp += 1
    if matrix[ii - 1][jj + 1] == '▒':
        pp += 1
    if matrix[ii][jj - 1] == '▒':
        pp += 1
    if matrix[ii][jj + 1] == '▒':
        pp += 1
    if matrix[ii + 1][jj - 1] == '▒':
        pp += 1
    if matrix[ii + 1][jj] == '▒':
        pp += 1
    if matrix[ii + 1][jj + 1] == '▒':
        pp += 1
    return pp


def second_matrix(old_matrix):
    new_matrix = create_matrix()
    for i in range(24):
        for j in range(49):
            new_matrix[i][j] = old_matrix[i][j]
    return new_matrix


matr = create_matrix()
new_life(matr)
new_life(matr)
new_life(matr)
new_life_2(matr)
matrix1 = second_matrix(matr)
wall(matr)
wall(matrix1)

for t in range(100):
    sleep(0.5)
    matrix1 = second_matrix(matr)
    lif_belie = 0
    lif_chernie = 0
    for i in range(24):
        for j in range(49):
            if matr[i][j] == '█':
                lif_belie += 1
            if matr[i][j] == '▒':
                lif_chernie += 1
            k = osmotr(matrix1, i, j)
            p = osmotr2(matrix1, i, j)
            if k == 3 and p < k and (matrix1[i][j] == '░' or matrix1[i][j] == '▒'):
                matr[i][j] = '█'
            if p == 3 and k < p and (matrix1[i][j] == '░' or matrix1[i][j] == '█'):
                matr[i][j] = '▒'
            if k > 3 and matrix1[i][j] == '█':
                matr[i][j] = '░'
            if k < 2 and matrix1[i][j] == '█':
                matr[i][j] = '░'
            if p > 3 and matrix1[i][j] == '▒':
                matr[i][j] = '░'
            if p < 2 and matrix1[i][j] == '▒':
                matr[i][j] = '░'
            print(matrix1[i][j], end='')
        print()
    if matrix1 == second_matrix(matr):
        matr = create_matrix()
        new_life(matr)
        new_life(matr)
        new_life(matr)
        new_life_2(matr)
        new_life_2(matr)
        new_life_2(matr)
        matrix1 = second_matrix(matr)
        wall(matr)

    new_life(matr)
    new_life_2(matr)
    wall(matr)
    print(f'Этап {t + 1}')
    print(f'Живо: {lif_belie} белые       {lif_chernie} черные')
