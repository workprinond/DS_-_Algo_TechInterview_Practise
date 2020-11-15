

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

    Final_string = temp_string_level[0] + ' '
    if len(Final_string)<=10000:
        Coordinates = [1, 1]
        for i in range(0, len(Final_string)):
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
    else:
        Final_short_string = ''
        count = 1

        for i in range(0, len(Final_string) - 1):
            if Final_string[i] == Final_string[i + 1]:
                count += 1
                continue
            if count > 1:
                Final_short_string = Final_short_string + str(count) + Final_string[i]
                count = 1
            else:
                Final_short_string = Final_short_string + Final_string[i]

        Final_short_string = ' ' + Final_short_string
        Coordinates = [1, 1]
        for i in range(0, len(Final_short_string)):
            if Final_short_string[i] == 'S':
                if Final_short_string[i - 1].isdigit() == True:
                    Coordinates[0] += int(Final_short_string[i - 1])
                else:
                    Coordinates[0] += 1
                Coordinates[0] %= 1000000000

            if Final_short_string[i] == 'E':
                if Final_short_string[i - 1].isdigit() == True:
                    Coordinates[1] += int(Final_short_string[i - 1])
                else:
                    Coordinates[1] += 1
                Coordinates[1] %= 1000000000

            if Final_short_string[i] == 'N':
                if Final_short_string[i - 1].isdigit() == True:
                    Coordinates[0] -= int(Final_short_string[i - 1])
                else:
                    Coordinates[0] -= 1
                if Coordinates[0] < 0:
                    Coordinates[0] = 1000000000 + Coordinates[0]

            if Final_short_string[i] == 'W':
                if Final_short_string[i - 1].isdigit() == True:
                    Coordinates[1] -= int(Final_short_string[i - 1])
                else:
                    Coordinates[1] -= 1
                if Coordinates[1] < 0:
                    Coordinates[1] = 1000000000 + Coordinates[1]

            if Coordinates[0] == 0:
                Coordinates[0] = 1000000000
            if Coordinates[1] == 0:
                Coordinates[1] = 1000000000

    print('Case #' + str(a) + ': ' + str(Coordinates[1]) + ' '+ str(Coordinates[0]), flush=True)
    a = a + 1
    if cases > 0:
        cases = cases - 1
        caseinputs(cases, a)




a=1
cases = int(input())
if cases>0 and cases<=100:
    caseinputs(cases,a)