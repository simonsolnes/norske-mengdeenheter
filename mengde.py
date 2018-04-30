#!/usr/bin/env python3
import sys

def mengde(num):
    assert(isinstance(num, int))
    if num == 0:
        return 'ingen'
    mengder = [
        [1, 'en', '', ''],
        [2, 'et', 'par', 'par'],
        [4, 'en', 'kast', 'kaster'],
        [10, 'en', 'deger', 'deger'],
        [12, 'et', 'dusin', 'dusin'],
        [16, 'en', 'pakke', 'pakker'],
        [20, 'et', 'snes', 'snes'],
        [30, 'et', 'vedde', 'vedder'],
        [40, 'en', 'simmer', 'simmer'],
        [48, 'en', 'kiste', 'kister'],
        [60, 'en', 'skokk', 'skokk'],
        [80, 'en', 'ol', 'ol'],
        [100, 'ett', 'smalt hundre', 'smale hundrer'],
        [120, 'ett', 'stort hundre', 'smale hundrer'],
        [144, 'en', 'gross', 'gross'],
        [200, 'et', 'balle', 'balle'],
        [1200, 'ett', 'stort tusen', 'store tusener'],
        [1728, 'en', 'storgross', 'storgross'],
        [14400, 'en', 'lest', 'lest'],
    ]
    converted = []
    while num > 0:
        for i in mengder[::-1]:
            if num >= i[0]:
                converted.append(i)
                num -= i[0]
                break
    counted_record = []
    counted = []
    for i in converted:
        if i not in counted_record:
            counted.append([converted.count(i), i])
            counted_record.append(i)

    for i in range(len(counted)):
        for m in mengder:
            if counted[i][0] == m[0] and m[0] != 1:
                counted[i][0] = m

    formatted = []
    for i in counted:
        if isinstance(i[0], list):
            formatted.append(i[0][1] + ' ' + i[0][2] + ' ' + i[1][3])
        elif i[0] == 1:
            if len(i[1][2]) == 0:
                formatted.append(i[1][1])
            else:
                formatted.append(i[1][1] + ' ' + i[1][2])
        else:
            formatted.append(mengde(i[0]) + ' ' + i[1][3])
    if len(formatted) == 1:
        return formatted[0]
    else:
        return ', '.join(formatted[:-1]) + ' og ' + formatted[-1]
def _help():
    print('Konverter et tall til en norsk mengdeenhet')
    print('./mengde.py tall')
    exit()


if len(sys.argv) == 2:
    try:
        int(sys.argv[1])
    except ValueError:
        _help()
else:
    _help()

print(mengde(int(sys.argv[1])))
