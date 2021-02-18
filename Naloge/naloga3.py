prepovedani = [
    (12, 18),
    (2, 5),
    (3, 8),
    (0, 4),
    (15, 19),
    (6, 9),
    (13, 17),
    (4, 8),
]


"""
#1.
    for spodnja, gornja in prepovedani:
        if gornja>najvišja_zgornja_meja:
            najvišja_zgornja_meja=gornja
    print(najvišja_zgornja_meja)

#2.
i=0
while i<20:

    for spodnja, gornja in prepovedani:
        if i>=spodnja and i<=gornja:
            print(i, "je vsebovan v", (spodnja,gornja))
            break
    else:
        print(i, "ni vsebovan")


    i+=1
"""
#3.-dodatna
prepovedani.append((9, 12))
i=0
while True:

    for spodnja, gornja in prepovedani:
        if i>=spodnja and i<=gornja:
            break
    else:
        print(i, "ni vsebovan")
        break

    i+=1
