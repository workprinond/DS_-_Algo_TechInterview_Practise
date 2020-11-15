'''
------------------------------------------------------------------------------------------------------------------------------------------------------
Question: Movies on Flight
You are on a flight and wanna watch two movies during this flight.
You are given int[] movie_duration which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).
Find the pair of movies with the longest total duration. If multiple found, return the pair with the longest movie.
e.g.
Input
movie_duration: [90, 85, 75, 60, 120, 150, 125]
d: 250
Output
[90, 125]
90min + 125min = 215 is the maximum number within 220 (250min - 30min)
*** Also try modified version: return the indexes of the pair instead of actual movie duration
------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def longestPair(ary, d):
    '''
    # case 1 - example input
    >>> longestPair([90, 85, 75, 60, 120, 150, 125], 250)
    [90, 125]
    # case 2 - empty array
    >>> longestPair([], 250)
    []
    # case 3 - all duplicates
    >>> longestPair([90, 10, 80, 20, 70, 30, 60, 40, 50, 50], 130)
    [10, 90]
    # case 4 - short flight duration
    >>> longestPair([90, 10, 80, 20, 70, 30, 60, 40, 50, 50], 5)
    []
    '''
    d = d - 30
    ary = sorted(ary)
    left, right = 0, len(ary) - 1
    maxDuration = 0
    # default maxPair value differs by desired return value
    maxPair = [] # it could be None

    while left < right:
        curDuration = ary[left] + ary[right]
        if curDuration <= d:
            if curDuration > maxDuration:
                maxPair = [ary[left], ary[right]]
                maxDuration = curDuration
            left += 1
        else:
            right -= 1

    return maxPair


# modified version
def longestPair2(ary, d):
    '''
    # case 1 - example input
    >>> longestPair2([90, 85, 75, 60, 120, 150, 125], 250)
    [0, 6]
    # case 2 - empty array
    >>> longestPair2([], 250)
    [-1, -1]
    # case 3 - all duplicates
    >>> longestPair2([90, 10, 80, 20, 70, 30, 60, 40, 50, 50], 130)
    [0, 1]
    # case 4 - short flight duration, no movies can watch
    >>> longestPair2([90, 10, 80, 20, 70, 30, 60, 40, 50, 50], 5)
    [-1, -1]
    '''
    d = d - 30
    origIndex = {duration: index for index, duration in enumerate(ary)}
    ary = sorted(ary)
    left, right = 0, len(ary) - 1
    maxDuration = 0
    maxPair = []

    while left < right:
        curDuration = ary[left] + ary[right]
        if curDuration <= d:
            if curDuration > maxDuration:
                maxPair = [ary[left], ary[right]]
                maxDuration = curDuration
            left += 1
        else:
            right -= 1

    if not maxPair:
        return [-1, -1]

    return sorted([origIndex[maxPair[0]], origIndex[maxPair[1]]])


if __name__ == '__main__':
    import doctest
    doctest.testmod()