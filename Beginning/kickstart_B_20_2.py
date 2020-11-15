
import math


def caseinputs(cases,a):
 if cases > 0:
     input_list = list(map(int, input().split()))
     if len(input_list) == 2:
        N_busroutes = input_list[0]
        D_days = input_list[1]
        Bus_days = list(map(int, input().split()))
        if len(Bus_days)<=N_busroutes:
            if N_busroutes>=1 and N_busroutes<=1000 and D_days>=1 and D_days<=1000000000000:
                Bus_Routes(D_days,Bus_days,a,cases)


def Bus_Routes( D_days:int,Bus_days,a :int,cases:int):
    count1 = 0
    for i in range(len(Bus_days)-1,-1,-1):
        count1 = count1 + 1
        if Bus_days[i] <= D_days:
            if i == len(Bus_days)-1:
                Bus_days[i] = Bus_days[i] * math.floor(D_days/ Bus_days[i])
            else:
                Bus_days[i] = Bus_days[i] * math.floor(Bus_days[i + 1] / Bus_days[i])





    print('Case #' + str(a) + ': ' + str(Bus_days[0]),flush=True)
    a = a + 1
    if cases> 0:
        cases = cases - 1
        caseinputs(cases, a)



a=1
cases = int(input())
if cases>0 and cases<=100:
    caseinputs(cases,a)

