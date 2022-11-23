def uniquePathsWithObstacles(obstacleGrid):
    pole = [[1 if i == 0 else 0 for i in obstacleGrid[q]] for q in range(len(obstacleGrid))]
    for i in range(1, len(pole)):
        for j in range(1, len(pole[i])):
            if pole[i][j] != 0:
                pole[i][j] = pole[i-1][j] + pole[i][j-1]
    return pole[-1][-1]


print(uniquePathsWithObstacles([[[[1,0],[0,0]]]]))
