


def caseinputs(cases,a):
 if cases > 0:
     input_list = list(map(int, input().split()))
     Integer_val = int(input_list[0])
     Values = list(map(int, input().split()))
     if len(Values)<=Integer_val:
            Perfect_Subarray(Values,a,cases)


def Perfect_Subarray(Values,a:int,cases:int):
    Count = 0
    Values1 = [[0 for i in range(len(Values))] for j in range(len(Values))]
    for i in range(0,len(Values)):
        for j in range(0,len(Values)):
            if i == 0:
                Values1[i][j]= Values[j]
                if Values1[i][j] == 0 or Values1[i][j] == 1 or Values1[i][j] == 4 or Values1[i][j] == 9 or Values1[i][j] == 16 or Values1[i][j] == 25 or Values1[i][j] == 36 or Values1[i][j] == 49 or Values1[i][j] == 64 or Values1[i][j] == 81 or Values1[i][j] == 100:
                    print(Values1[i][j])
                    Count +=1
                continue
            if j == 0:
                 continue
            if i >= j :
                Values1[i][j] = Values1[i - 1][j - 1] + Values1[0][j]
                if Values1[i][j] == 0 or Values1[i][j] == 1 or Values1[i][j] == 4 or Values1[i][j] == 9 or Values1[i][j] == 16 or Values1[i][j] == 25 or Values1[i][j] == 36 or Values1[i][j] == 49 or Values1[i][j] == 64 or Values1[i][j] == 81 or Values1[i][j] == 100:
                    print(Values1[i][j])
                    Count += 1


    print(Values1)

    print('Case #' + str(a) + ': ' + str(Count),flush=True)
    a = a + 1
    if cases> 0:
        cases = cases - 1
        caseinputs(cases, a)



a=1
cases = int(input())
if cases>0 and cases<=100:
    caseinputs(cases,a)

