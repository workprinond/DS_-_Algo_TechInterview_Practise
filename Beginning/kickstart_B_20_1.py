






def caseinputs(cases,a):
 if cases > 0:
    int(input())

 if cases <= 100 and cases > 0:
    checkpoint_height = list(map(int,input().split()))
    if len(checkpoint_height)>=3 and len(checkpoint_height)<=100:
        tour(checkpoint_height, cases,a)


def tour(checkpoints, cases:int,a :int):
    peak = 0
    count = 0
    for i in range(len(checkpoints)):
        if i != 0 and i != len(checkpoints)-1:
            if checkpoints[i]>=1 and checkpoints[i]<=100:
                if checkpoints[i] > checkpoints[i - 1] and checkpoints[i] > checkpoints[i + 1]:
                    temp = checkpoints[i]
                    if  temp == peak:
                        count = count + 1
                    if temp > peak:
                        count = 1
                        peak = temp


    print('Case #' + str(a) + ': ' + str(count),flush=True)
    a = a+1
    if cases >0:
        cases = cases - 1
        caseinputs(cases,a)

a = 1
cases = int(input())
caseinputs(cases,a)

