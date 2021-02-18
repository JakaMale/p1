from math import *

hitrost=float(input("vnesi hitrost (m/s)"))
kot=float(input("vnesi kot (v stopinjah)"))
radijani=kot*pi/180
razdalja =(pow(hitrost,2)* sin(2*radijani))/10  #
print("dolžina je",razdalja, "m")