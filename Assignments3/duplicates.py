list = [40,'java','root',54,30,54,30]
i=0
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            print "duplicate is", list[i]
