import numpy as np
from datetime import datetime
import csv

# Define Variables
Current_Run = 1
Current_Step = 1
Total_Steps = 10
Table = [[0, 0, 0, 0, 0]]
RunLog = []
CR = 1


# Sudo Picture Code
def Take_Picture():
    P = datetime.now().strftime("%m%d%y%H%M%S")
    Table[C][3] = P
    # file = open(P + ".txt", "w")
    # file.write("Your text goes here")
    # file.close()


# Imports Table
def DataImport(CR):
    data = np.loadtxt("RunLog.csv", delimiter='  ')
    datai = data.astype(int)
    RunLog = datai
    print(RunLog)
    CR = datai[datai.shape] + 1
    print(CR)


# Run Loop
while Current_Run > 0:

    C = Current_Step - 1

    if (Current_Step == 1):
        DataImport(CR)
    if (Current_Run == -1):
        break

    # Takes Picture
    Take_Picture()

    # Gets Timestamp
    now = datetime.now()
    T = int(datetime.timestamp(now))
    Table[C][2] = T

    # Run/Step Check
    if (Current_Step > Total_Steps):
        Last = C - 1
        Table[Last][4] = 1
        print(Table)
        np.savetxt('Table.csv', Table, delimiter='  ', fmt='%s')
        print(CR)
        print(RunLog)
        RunLog = np.append(RunLog, [[CR]])
        print(RunLog)
        np.savetxt('RunLog.csv', RunLog, delimiter='  ', fmt='%s')
        break
    else:
        Table[C][1] = Current_Step
        Table[C][0] = Current_Run
        Table = np.vstack([Table, [0, 0, 0, 0, 0]])
        Current_Step = Current_Step + 1
        print(Table)
