speed=25
distance_school=4
Time_required=(distance_school/speed)*60
Busstop=10*2
Actual_time=Time_required+Busstop
print(f"The actual time require to reach school by bus  is {Actual_time} minutes")
#alternate

speed1=7
distance1=1
time1_required=(distance1/speed1)*60
speed2=15
distance2=2
time2_required=(distance2/speed2)*60
speed3=7
distance3=1
time3_required=(distance3/speed3)*60
totaltime_walk=time1_required+time2_required+time3_required
print(f"The total time require to reach school by waking is {totaltime_walk} minutes")

if Actual_time>totaltime_walk:
    print(f"Walking is faster then travelling by bus.")
else:
    print(f"Travelling by bus is faster then walking.")