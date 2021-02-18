
"""""
#vsote
stevilo=int(input("vnesi stevilo"))
stevka=0
skupaj=0
while stevka<=stevilo:
    skupaj+=stevka
    stevka+=1
print(skupaj)

#kocke
velikost_skatle=0
stevec=0
st_kock=int(input("vnesi stevilo kock"))
while st_kock>velikost_skatle:
    stevec+=1
    velikost_skatle=stevec**2
prostora=velikost_skatle-st_kock
print("potrebujemo skatlo sirine",stevec,"v kateri je prostora se za",prostora)


#delitelji


x=int(input("vnesi stevilo"))
stevec=1
while stevec<=x:
    if x%stevec==0:
        print(stevec)
    stevec+=1




#kvadrati

stevilo=int(input("vnesi stevilo"))
stevec=1

while stevec**2<stevilo:
    stevec += 1
    if stevec**2==stevilo:
        print("stevilo je kvadrat", stevec)
        break
        
if stevec**2!=stevilo:
    print("stevilo NI kvadrat")


#*
#**
#***
#****

visina=int(input("vnesi visino"))
stevec=0
trikotnik=""
while stevec<visina:
    trikotnik+="*"
    stevec+=1
    print(trikotnik)



#    *
#   ***
#  *****
# *******




visina=int(input("vnesi visino"))
stevec=0
zamik=visina
x=1
while stevec<visina:
    trikotnik = " "*zamik
    trikotnik+="*"*x
    x+=2
    stevec+=1
    zamik-=1
    print(trikotnik)


#postevanka


stevec=0
while stevec<100:
    stevec+=1
    if stevec%7==0:
        print("BUM")
    elif '7'in str(stevec):
        print("BUM")
    else:
        print(stevec)


"""""
import math

a=float(input("vnesi a:"))
b=float(input("vnesi b:"))
c=float(input("vnesi c:"))

D=b**2-4*a*c
if D<0:
    print("enacba nima realnih resitev")
else:
    x_ena=(-b+ math.sqrt(D))/2*a
    x_dva=(-b- math.sqrt(D))/2*a
    if(x_ena==x_dva):
        print("ima eno resitev", x_ena)
    else:
        print(x_ena,x_dva)



