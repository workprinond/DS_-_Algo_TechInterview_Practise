from heapq import *


def buildString(A, B, C):
    h = [[-A, "a"], [-B, "b"], [-C, "c"]]
    heapify(h)

    res = []
    prev1 = prev2 = None
    while h:
        maxCh = h[0][1]
        if prev1 == prev2 == maxCh and len(h) > 1:
            maxEl = heappop(h)
            secondEl = heappop(h)
            secondEl[0] += 1
            cur = secondEl[1]
            if secondEl[0] != 0: heappush(h, secondEl)
            heappush(h, maxEl)
        elif prev1 == prev2 == maxCh and len(h) <= 1:
            break
        else:
            maxEl = heappop(h)
            maxEl[0] += 1
            cur = maxEl[1]
            if maxEl[0] != 0: heappush(h, maxEl)
        res.append(cur)
        prev1, prev2 = prev2, cur

    return "".join(res)