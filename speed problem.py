distance = float(input("enter distance in miles"))
speedlimit =  float(input("enter mph speed limit"))
speed = float(input("enter average mph speed"))

time = distance / speedlimit
speedtime = distance / speed

Minutes_in_hour = 60

speedtimemin = speedtime*Minutes_in_hour
timemin = time*Minutes_in_hour

savedtime = 0

if speed > speedlimit:
    savedtime = timemin - speedtimemin
else:
    print("safe driver no time save")

print(f'time at speed limit {timemin:.2f} minutes')
print(f'time at your speed {speedtimemin:.2f} minutes')

if savedtime > 0:
    print(f'time saved {savedtime:.2f} minutes')
