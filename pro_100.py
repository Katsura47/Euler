from math import sqrt

import time

start = time.time()


def tot(b):
    return sqrt(2*(b**2 - b + 1/8)) + 1/2





blue = 15
azalis = 5
azalislar_arasındaki_fark1 = 2
azalislar_arasındaki_fark2 = 12
while True:
    tota = tot(blue)
    blue = 6*blue - azalis
    azalis += azalislar_arasındaki_fark2
    azalislar_arasındaki_fark3 = azalislar_arasındaki_fark2*6 - azalislar_arasındaki_fark1
    azalislar_arasındaki_fark1 = azalislar_arasındaki_fark2
    azalislar_arasındaki_fark2 = azalislar_arasındaki_fark3
    tota = tot(blue)
    if tota > 10**12 and int(tota) == tota:
        print(blue)
        break
end = time.time()

print("code took " + str((end-start)))
# HHAHAHHAAHAHAHAHAHAHAHH!       %30 DU LAN BU!

