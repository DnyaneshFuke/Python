import time
Wt=1
RT=5
AT=0
while(AT<RT):
    print("Attempt",AT+1,"Wait_Time",Wt)
    time.sleep(Wt)
    Wt*=2
    AT+=1
