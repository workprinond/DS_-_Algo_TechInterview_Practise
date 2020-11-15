def moviesOnFlight(movieDurations, d):
    d = d - 30
    newM = movieDurations
    newM = sorted(newM, reverse=True)
    maximum = 0
    ans = []
    for i in range(len(newM)):
        for j in range(len(newM) - 1, i, -1):
            sum = newM[i] + newM[j]
            if sum <= d:
                if sum > maximum:
                    maximum = newM[i] + newM[j]
                    ans = [movieDurations.index(newM[i]), len(movieDurations) - movieDurations[::-1].index(newM[j]) - 1]
            else:
                break

    return sorted(ans)