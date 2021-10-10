import time



def howManyDays():
    currentTime = int(time.time())
    HaloweenTime = 	1635634800
    timeUntil = (HaloweenTime - currentTime) / 60 / 60 / 24
    print(timeUntil)


howManyDays()
