import numpy as np
import csv


def mode(data1, data2, data3, data4):
    modenum = data1
    twocount = 0
    two = np.zeros(2)
    arr = np.zeros(39)
    data1 = int(data1)
    data2 = int(data2)
    data3 = int(data3)
    data4 = int(data4)
    arr[data1] += 1
    arr[data2] += 1
    arr[data3] += 1
    arr[data4] += 1
    if(max(arr) == 3 or max(arr) == 4):
        for i in range(39):
            if(arr[i] == max(arr)):
                modenum = i
    elif(max(arr) == 2):
        for i in range(39):
            if(arr[i] == 2):
                two[twocount] = i
                twocount += 1
        if(twocount == 2):
            modenum = data1
        else:
            modenum = two[0]

    else:
        modenum = data1

    modenum = int(modenum)
    modenum = str(modenum)

    return modenum


arr1 = []
arr2 = []
arr3 = []
arr4 = []
final = []
with open('./hw2_csv/hw2-1.csv', newline='') as csv1:
    rows1 = csv.reader(csv1)

    for row1 in rows1:
        arr1.append(row1[1])

with open('./hw2_csv/test1.csv', newline='') as csv2:
    rows2 = csv.reader(csv2)

    for row2 in rows2:
        arr2.append(row2[1])
with open('./hw2_csv/test3.csv', newline='') as csv3:
    rows3 = csv.reader(csv3)
    for row3 in rows3:
        arr3.append(row3[1])
with open('./hw2_csv/test4.csv', newline='') as csv4:
    rows4 = csv.reader(csv4)
    for row4 in rows4:
        arr4.append(row4[1])


for i in range(451552):
    final.append([str(i), mode(arr1[i], arr2[i], arr3[i], arr4[i])])
    print(i)

with open("./hw2_csv/output3.csv", "w", newline="") as f:
    f.write('Id,Class\n')
    writer = csv.writer(f)
    writer.writerows(final)
    print('ok')
