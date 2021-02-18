from math import *


def zadani_cilj(): #probaj zadeti cilj.
    oddaljenost=float(input("Vnesi oddaljenost cilja v metrih."))
    while True:
        kot=float(input("Vnesi kot v stopinjah."))
        hitrost = float(input("Vnesi hitrost v metrih na sekundo."))
        poskus=(pow(hitrost,2)* sin(2*kot*pi/180))/10
        print(poskus)
        if(poskus<oddaljenost+5 and poskus>oddaljenost-5):
            print("zadeli ste cilj na ",poskus)
            break




def pujs_in_cilj():   #najde primeren kot in hitrost.
    r_cilja=float(input("vnesi oddaljenost cilja"))
    r_prasicka=float(input("vnesi razdaljo do parasicka"))
    visina_prasicka=float(input("vnesi visino prasicka"))

    hitrost=0
    kotx=asin(visina_prasicka/r_prasicka)

    print("kot je ",kotx/pi*180, "stopinj.")

    hitrost=sqrt((r_cilja*10)/sin(2*kotx))
    print("hitrost ",hitrost, "m/s")


zadani_cilj()
pujs_in_cilj()