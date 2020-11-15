

def caseinputs(cases,a):
 if cases > 0:
     program = input()
     if len(program) >= 1 and len(program) <= 2000:
        string_list = list(program)
        Decoding_String(string_list,a,cases)




def Decoding_String(string_list,a,cases):
    temp_string_level = ['']* 1000
    level =0
    for i in range(len(string_list)-1,-1,-1):
        if string_list[i] == 'N' or string_list[i] == 'S' or string_list[i] == 'W' or string_list[i] == 'E':
            temp_string_level[level] = string_list[i] +  temp_string_level[level]
        if string_list[i] == ')':
            level += 1
        if string_list[i] == '(':
            temp_string_level[level]= temp_string_level[level]* int(string_list[i-1])
            temp_string_level[level-1]=temp_string_level[level]+ temp_string_level[level-1]
            temp_string_level[level]=''
            level -= 1

    Final_string = temp_string_level[0]
    Coordinates = [1,1]
    for i in range(0,len(Final_string)):
        if Coordinates[0] == 1 and Final_string[i] == 'N':
            Coordinates[0] = 1000000000
            continue
        if Coordinates[1] == 1 and Final_string[i] == 'W':
            Coordinates[1] = 1000000000
            continue
        if Coordinates[0] == 1000000000 and Final_string[i] == 'S':
            Coordinates[0] = 1
            continue
        if Coordinates[1] == 1000000000 and Final_string[i] == 'E':
            Coordinates[1] = 1
            continue
        if Final_string[i] == 'S':
            Coordinates[0] += 1
        if Final_string[i] == 'E':
            Coordinates[1] += 1
        if Final_string[i] == 'N':
            Coordinates[0] -= 1
        if Final_string[i] == 'W':
            Coordinates[1] -= 1

    print('Case #' + str(a) + ': ' + str(Coordinates[1]) + ' '+ str(Coordinates[0]), flush=True)
    a = a + 1
    if cases > 0:
        cases = cases - 1
        caseinputs(cases, a)














a=1
cases = int(input())
if cases>0 and cases<=100:
    caseinputs(cases,a)