#Exercise 24: Units of Time
print("Insert number of Days: ")
ND = int(input())
print("Insert number of Hours: ")
NH = int(input())
print("Insert number of Minutes: ")
NM = int(input())
print("Insert number of Seconds: ")
NS = int(input())

#T is time
T = 0
T += int(ND * 86400)
T += int(NH * 3600)
T += int(NM * 60)
T += int(NS)
print("That Duration in Seconds: " + str(T))


#Exercise 25: Units of Time(Again)
print("insert number of seconds: ")
TS = int(input())
#TS is total seconds

Days = TS // 86400
TS %= 86400
Hours = TS // 3600
TS %= 3600
Minutes = TS // 60
TS %= 60
Seconds = TS

print(str(Days).zfill(2) + ":" + str(Hours).zfill(2) + ":" + str(Minutes).zfill(2) + ":" + str(Seconds).zfill(2))
#Exercise 26: Current Time
import time
t = time.localtime()
print("The current time is: " + time.asctime(t))