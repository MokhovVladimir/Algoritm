""" Алгоритм основан на динамеческом программировании. В качестве значений в списке dp используется количество путей в эту вершину.
Способов попасть в вершины dp[i][0] и dp[0][j] 1 (тк робот может двигаться только вправа и вниз."""

def uniquePathsWithObstacles(obstacleGrid):
    pole = [[1 if i == 0 else 0 for i in obstacleGrid[q]] for q in range(len(obstacleGrid))]  # Меняем матрицу таким образом, чтоб камни были 0, а пути 1
    for i in range(1, len(pole)):
        for j in range(1, len(pole[i])):
            if pole[i][j] != 0:
                pole[i][j] = pole[i-1][j] + pole[i][j-1]  # Суммируем количество путей в точку, как кол-во путей в соседние вершины
    return pole[-1][-1]  # Возвращаем последний элемент


print(uniquePathsWithObstacles([[[[1,0],[0,0]]]]))

""" Сложность O(n**2)"""
