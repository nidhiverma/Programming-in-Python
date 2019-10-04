    n = int(input())
    arr = map(int, input().split())

    sortedScores = sorted(arr, reverse = True)
    max = sortedScores[0]
    for i in range(1, n):
        if sortedScores[i] < max:
            print(sortedScores[i])
            break
