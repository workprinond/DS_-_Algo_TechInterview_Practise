import heapq


def kNearestPostOffices(myLocation, postOffices, k):
    '''
    # case 1 - example input
    >>> postOfficesA = [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
    >>> kNearestPostOffices([0, 0], postOfficesA, 3)
    [[4, 3], [-1, 2], [0, 3]]

    # case 2 - empty input 1
    >>> postOfficesB = []
    >>> kNearestPostOffices([0, 0], postOfficesB, 3)
    []

    # case 3 - empty input 2
    >>> postOfficesC = [[]]
    >>> kNearestPostOffices([0, 0], postOfficesC, 3)
    []

    # case 4 - larger k than number of offices
    >>> postOfficesD = [[-16, 5], [-1, 2]]
    >>> kNearestPostOffices([0, 0], postOfficesD, 5)
    [[-16, 5], [-1, 2]]
    '''
    # for empty input
    if not postOffices or not postOffices[0]:
        return []

    heap = []

    for eachOffice in postOffices:
        distance = -((myLocation[0] - eachOffice[0]) ** 2 + (myLocation[1] - eachOffice[1]) ** 2)
        if len(heap) == k:
            heapq.heappushpop(heap, [distance, eachOffice])
        else:
            heapq.heappush(heap, [distance, eachOffice])

    return [eachOffice for distance, eachOffice in heap]


# modified version
def kClosest(postOffices, k):
    '''
    # case 1 - simple input
    >>> postOfficesA = [[1, 3], [-2, 2]]
    >>> kClosest(postOfficesA, 1)
    [[-2, 2]]
    # case 2 - simple input 2
    >>> postOfficesB = [[3, 3], [5, -1], [-2, 4]]
    >>> kClosest(postOfficesB, 2)
    [[-2, 4], [3, 3]]

    # case 3 - larger k than number of offices
    >>> postOfficesC = [[3, 3], [5, -1], [-2, 4]]
    >>> kClosest(postOfficesC, 5)
    [[5, -1], [3, 3], [-2, 4]]

    # case 4 - empty input 1
    >>> postOfficesD = []
    >>> kNearestPostOffices([0, 0], postOfficesD, 3)
    []

    # case 5 - empty input 2
    >>> postOfficesE = [[]]
    >>> kNearestPostOffices([0, 0], postOfficesE, 3)
    []
    '''
    # for empty input
    if not postOffices or not postOffices[0]:
        return []

    heap = []

    for eachOffice in postOffices:
        distance = -(eachOffice[0] ** 2 + eachOffice[1] ** 2)
        if len(heap) == k:
            heapq.heappushpop(heap, [distance, eachOffice])
        else:
            heapq.heappush(heap, [distance, eachOffice])

    return [eachOffice for distance, eachOffice in heap]


if __name__ == '__main__':
    import doctest

    doctest.testmod()