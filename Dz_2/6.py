""" Задача решена при помощи динамического программирования. Создаю матрицу, в которой занчениями являются максимальной длинны квадраты из 1"""

def countSquares(matrix):
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 1:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1  # Смотрю на соседние величины и беру из них минимальное значение + 1, что и будет являться квадратом из 1
    count = 0
    for i in matrix:
        count += sum(i)  # Пробегаю по своей матрице и суммирую значения
    return count


""" Сложность алгоритма O(n**2)"""
