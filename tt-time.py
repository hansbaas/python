answer = "y"
distance = int(raw_input("Distance in meters: "))
while answer is not "N" :
    speed = int(raw_input("Speed in km/h: "))
    time = distance / (speed / 3.6)
    import datetime
    print str(datetime.timedelta(seconds=time))
    answer = raw_input("Continue [y/N]: ")
