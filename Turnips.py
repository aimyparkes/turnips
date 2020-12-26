day = ["Monday_Morning", "Monday_Arvo", "Tuesday_Morning", "Tuesday_Arvo", "Wednesday_Morning", "Wednesday_Arvo", "Thursday_Morning", "Thursday_Arvo", "Friday_Morning", "Friday_Arvo", "Saturday_Morning", "Saturday_Arvo"]

turnips = [
    [55, 56, 48, 127, 101, 102, 107, 98, 59, 55, 126, 104],
    [83, 80, 77, 73, 70, 132, 185, 315, 136, 104, 60, 56],
    [123, 126, 121, 116, 117, 69, 62, 143, 0, 0, 69, 60]
    ]

#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

total_av = []

for i in range(12):
    av_list=[]
    for turnip in turnips:
        if turnip[i] > 0:
            av_list.append(turnip[i])
    if len(av_list) == 0:
        continue
    av = sum(av_list) / len(av_list)
     
    total_av.append(av)




"""
REMOVE OUTLIERS
"""

from statistics import median

turnips = [
    [55, 56, 48, 127, 101, 102, 107, 98, 59, 55, 126, 104],
    [83, 80, 77, 73, 70, 132, 185, 315, 136, 104, 60, 56],
    [123, 126, 121, 116, 117, 69, 62, 143, 114, 78, 69, 60],
    [109, 146, 126, 134, 134, 71, 64, 57, 150, 68, 60, 114],
    [81, 104, 150, 441, 147, 86, 63, 53, 72, 79, 54, 45]
    ]


def day_lister(weeks, time):
    day = 0
    day_list = []
    for i in range(weeks+1):
        if i > 0:
            day_list.append(turnips[day][time])
            day = day + 1
        else:
            continue
    return day_list


len_of_listo = len(turnips)
parsnips = [day_lister(len_of_listo, i) for i in range(12)]

def split_list(a_list):
    half = len(a_list)//2
    return [a_list[:half]] + [a_list[half:]]

count = 0
leek=[]
for i in range(12):
    a= sorted(parsnips[count])
    leek.append(a)
    count= count + 1

count = 0
carrots = []

for i in range(12):
    a = split_list(leek[count])
    carrots.append(a)
    count = count + 1

low_big = []
for i in range(12):
    med = carrots[i][1][0]
    del carrots[i][1][0]

    little_med = median(carrots[i][0])
    big_med = median(carrots[i][1])

    iqr = big_med - little_med
    low_out = little_med - (iqr * 1.5)
    big_out = big_med + (iqr * 1.5)
    low_big.append((low_out, big_out))


pumpkin = []
for turnip in turnips:
    gourd = []
    for i,element in enumerate(turnip):
        low_out,big_out = low_big[i]
        if low_out< element < big_out:
            gourd.append(element)
    pumpkin.append(gourd)



print(low_big)




///
11/8
///


turnips = [
    [55, 56, 48, 127, 101, 102, 107, 98, 59, 55, 126, 104],
    [83, 80, 77, 73, 70, 132, 185, 315, 136, 104, 60, 56],
    [123, 126, 121, 116, 117, 69, 62, 143, 114, 78, 69, 60],
    [109, 146, 126, 134, 134, 71, 64, 57, 150, 68, 60, 114],
    [81, 104, 150, 441, 147, 86, 63, 53, 72, 79, 54, 45],
    [113, 108, 159, 163, 152, 90, 85, 82, 79, 75, 71, 68],
    [96, 91, 87, 83, 0, 75, 71, 126, 185, 441, 0, 152],
    ]
no_turnips = [
    [84, 80, 77, 72, 68, 65, 61, 57, 54, 50, 46, 43],
    [117, 0, 72, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

all_the_turnips = turnips + no_turnips
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#av for tunips
turnip_av = []
no_turnip_av = []
total_av = []

for i in range(12):
    turnip_av_list=[]
    for turnip in turnips:
        if turnip[i] > 0:
            turnip_av_list.append(turnip[i])
    if len(turnip_av_list) == 0:
        continue
    av = sum(turnip_av_list) / len(turnip_av_list)
     
    turnip_av.append(av)
    
for i in range(12):
    no_turnip_list=[]
    for turnip in no_turnips:
        if turnip[i] > 0:
            no_turnip_list.append(turnip[i])
    if len(no_turnip_list) == 0:
        continue
    av = sum(no_turnip_list) / len(no_turnip_list)
     
    no_turnip_av.append(av)
    
for i in range(12):
    total_list=[]
    for turnip in all_the_turnips:
        if turnip[i] > 0:
            total_list.append(turnip[i])
    if len(total_list) == 0:
        continue
    av = sum(total_list) / len(total_list)
     
    total_av.append(av)


    for i in range(len(turnips)):
    if turnips[i][0] == 0:
        turnips[i][0] = turnips[i][1]
    elif turnips[i][-1] == 0:
        turnips[i][-1] = turnips[i][-2]
    for j, turnip in enumerate(turnips[i]):
        if turnip == 0:
            new = (turnips[i][j-1] + turnips[i][j+1])/2
            turnips[i][j] = int(new)