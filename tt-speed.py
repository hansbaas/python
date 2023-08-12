answer = "y"
distance = int(raw_input("Distance in meters: "))
while answer is not "N" :
    minutes = int(raw_input("Minutes: "))
    seconds = int(raw_input("Seconds: "))
    seconds = 60 * minutes + seconds
    speed = distance * 3.6 / float(seconds)
    print(speed)
    answer = raw_input("Continue [y/N]: ")
