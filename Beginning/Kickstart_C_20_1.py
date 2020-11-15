


def caseinputs(cases,a):
 if cases > 0:
     input_list = list(map(int, input().split()))
     if len(input_list) == 2:
        Integer_val = int(input_list[0])
        Countdowns = int(input_list[1])
        Values = list(map(int, input().split()))
        if len(Values)<=Integer_val and Countdowns <= Integer_val and Countdowns>=2 and Integer_val>=2 and Integer_val<=1000:
                CountDown_Freq(Values,Countdowns,a,cases)


def CountDown_Freq(Values,Countdowns :int,a:int,cases:int):
    Alerts = 0
    Count = 0
    Values = Values + [100]
    Track = Countdowns
    for i in range(0,len(Values)):
        if Values[i] <= 200000 and Values[i]>0:
            if Values[i] == Track:
                if Values[i+1] ==Track - 1 or Values[i]==1:
                    Track = Track - 1
                    Alerts = 1
                    if Values[i] == 1 and Alerts == 1:
                        Count +=1
                        Track = Countdowns
            Alerts =0


    print('Case #' + str(a) + ': ' + str(Count),flush=True)
    a = a + 1
    if cases> 0:
        cases = cases - 1
        caseinputs(cases, a)



a=1
cases = int(input())
if cases>0 and cases<=100:
    caseinputs(cases,a)

