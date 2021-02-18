######jst nevem ce je tu prou rezultat pride 675####

import collections
text = open("pot_hoje.txt", "r")            #berem datoteko
text= text.read()
text= text.split(",")                       #nrdim seznam iz kerga nrdim dict
text=collections.Counter(text)
up_down=text['n']-text['s']               #pol pa pokrajšam nasprotne vrednosti
nw_se = text['se']-text['nw']
ne_sw = text['ne']-text['sw']
if (ne_sw<0 and nw_se<0 and up_down>0)or(ne_sw>0 and nw_se>0 and up_down<0):      #pogoj da dela za vse primere(se mi zdi nism 100%) bres tega bi delalo samo za to datoteko.(ce sploh dela)
    ne_sw=ne_sw * (-1)
    nw_se = nw_se * (-1)
up_down-=nw_se                              #pa seštejem u najkrajše premike
ne_sw+=nw_se
rez = ne_sw+up_down
print(rez)                                  #izpiše rezultat

