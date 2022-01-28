from jeanne import room_information, pourtour

info_1 = [[10,10], 3, 3]
info_2 = [[200,200], 30, 30]

murs = []
for i in (info_1, info_2):
    for j in pourtour(i):
        murs.append(i)

print(murs)