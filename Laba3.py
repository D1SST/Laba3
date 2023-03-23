"""
Формируется матрица F следующим образом: если А симметрична относительно главной диагонали,
то поменять в В симметрично области 1 и 3 местами, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: К * (F+A) * AT – AT + F.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
from math import ceil, floor
import random

def print_matrix(matrix):
    matrix1 = list(map(list, zip(*matrix)))
    for i in range(len(matrix1)):
        k = len(max(list(map(str, matrix1[i])), key=len))
        matrix1[i] = [f'{elem:{k}d}' for elem in matrix1[i]]
    matrix1 = list(map(list, zip(*matrix1)))
    for row in matrix1:
        print(*row)
    print()

try:
    K = int(input("Введите число K, являющееся коэффициентом при умножении: "))
    N = int(input("Введите число число N являющееся порядком квадратной матрицы: "))
    print()
    while N < 2:
        N = int(input("Вы ввели число, неподходящее по условию, введите число N, большее или равное 5:\n"))

    print("Матрица А изначальная:")
    matrix_A = [[random.randint(-10, 10) for i in range(N)] for j in range(N)]
    print_matrix(matrix_A)

    matrix_A_dop = [[elem for elem in raw] for raw in matrix_A]
    matrix_A_trans = [[0 for i in range(N)] for j in range(N)]

    print("Матрица A транспонированная:")

    for i in range(N):
        for j in range(N):
            matrix_A_trans[i][j] = matrix_A_dop[j][i]

    print_matrix(matrix_A_trans)

    print("Матрица F изначально равная матрице A:")

    matrix_F = [[elem for elem in raw] for raw in matrix_A]

    print_matrix(matrix_F)

    print("Проверка матрицы А на симметричность относительно главной диагонали...")
    def isSymmetric(matrix_A_dop, N):
        for i in range(N):
            for j in range(N):
                if matrix_A_dop[i][j] != matrix_A_trans[i][j]:
                    return False
        return True

    if isSymmetric(matrix_A_dop, N):
        sym_check = 1
        print("Результат: симметрична.")
    else:
        sym_check = 0
        print("Результат: несимметрична.")

    matrix_F_dop = [[elem for elem in raw] for raw in matrix_F]

    if sym_check == 1:
        c = 1
        c1 = 1
        print("\nМеняем области 1 и 3 симметрично местами.\n")
        if N % 2 == 0:
            for i in range(ceil(N / 2)):
                for j in range(ceil(N / 2)):
                    matrix_F[i][j] = matrix_F_dop[i][N // 2 - 1 - j]
                    matrix_F[i][N // 2 - 1 - j] = matrix_F_dop[i][j]
            for i in range((N // 2) - 1, (N // 2) - 1, -1):
                for j in range(N // 2):
                    matrix_F[i][j] = matrix_F_dop[i][N // 2 - 1 - j]
                    matrix_F[i][N // 2 - 1 - j] = matrix_F_dop[i][j]
        else:
            for i in range(0, N // 4 + 1, 1):
                for j in range(0, c, 1):
                    matrix_F[i][j] = matrix_F_dop[i][N // 2 - 1 - j]
                    matrix_F[i][N // 2 - 1 - j] = matrix_F_dop[i][j]
                c += 1
            for i in range(N // 2 - 1, N // 4 - 1, -1):
                for j in range(0, c1, 1):
                    matrix_F[i][j] = matrix_F_dop[i][N // 2 - 1 - j]
                    matrix_F[i][N // 2 - 1 - j] = matrix_F_dop[i][j]
                c1 += 1
    else:
        print("\nМеняем области C и E местами несимметрично...")
        if (N % 2) == 0:
            for i in range(0, N // 2):
                for j in range(N // 2, N):
                    matrix_F[i][j] = matrix_F_dop[i + N // 2][j]
                    matrix_F[i + N // 2][j] = matrix_F_dop[i][j]
        else:
            for i in range(0, N // 2, 1):
                for j in range(N // 2 + 1, N, 1):
                    matrix_F[i][j] = matrix_F_dop[i + N // 2 + 1][j]
                    matrix_F[i + N // 2 + 1][j] = matrix_F_dop[i][j]

    print("Матрица F сформирована:")
    print_matrix(matrix_F)

    print("Результат суммы матриц F и A:")
    matrix_C = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_C[i][j] = matrix_F[i][j] + matrix_A[i][j]
    print_matrix(matrix_C)

    print("Результат произведения матрицы C и числа K:")
    matrix_C_multiplied = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_C_multiplied[i][j] = K * matrix_C[i][j]
    print_matrix(matrix_C_multiplied)

    print("Результат произведения матрицы С и транспонированной матрицы А:")
    matrix_C_next = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            for l in range(N):
                matrix_C_next[i][j] += matrix_C_multiplied[i][l] * matrix_A_trans[l][j]
    print_matrix(matrix_C_next)

    print("Результат разности матрицы С и транспонированной матрицы А:")
    matrix_C_result = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_C_result[i][j] = matrix_C_next[i][j] - matrix_A_trans[i][j]
    print_matrix(matrix_C_result)

    print("КОНЕЧНЫЙ РЕЗУЛЬТАТ\nРезультат суммы матриц С и F:")
    matrix_C_end = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_C_end[i][j] = matrix_C_result[i][j] - matrix_F[i][j]
    print_matrix(matrix_C_end)

    print("Работа программы завершена.")

except ValueError:
    print("\nВведенный символ не является числом. Перезапустите программу и введите число заново.")
