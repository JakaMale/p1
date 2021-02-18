start_num_ana=0
start_num_berta=0
six=0
berta_meeting_ana=0
for i in range(1000):
    if (start_num_berta % 10 == start_num_ana % 10):
        berta_meeting_ana += 1
    start_num_ana=(start_num_ana*1664525+1013904223)%(2**32)
    start_num_berta= (start_num_berta *22695477 + 1) % (2 ** 32)
    if(start_num_ana%10==6):
        six+=1
print(six,berta_meeting_ana)


