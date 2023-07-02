import picar_4wd as fc
import time

# Hands-on Internet of Things Specialization  https://www.coursera.org/specializations/uiuc-iot
# IOT Devices Course
# Code for Hardware Lab
#

# speed = forward speed
# speed2 = backward speed
#
speed = 30
speed2 = 10

def main():

# Set up distance sensor to have full readings since start
#
    dist1 = fc.get_distance_at (90)
    scan_list = fc.scan_step(35)
    scan_list = fc.scan_step(35)
    scan_list = fc.scan_step(35)
    scan_list = fc.scan_step(35)
    scan_list = fc.scan_step(35)
    scan_list = fc.scan_step(35)
    scan_list = fc.scan_step(35)

#    time.sleep (5)
#

    while True:
        scan_list = fc.scan_step(35)
# scan_list is an array with obstacle data
#
        if not scan_list:
            continue

        tmp = scan_list[3:7]
 # gets the central portion of the obstacle array to find obstacles ahead
 # print info for debugging
 #
        print(scan_list)
        print(tmp)
        if tmp != [2,2,2,2]:
 # If finds obstacles, stop, wait, go backwards for a second and turn left
 #
            fc.stop()
            time.sleep(1)
            fc.backward(speed2)
            time.sleep (1)
            fc.turn_left(speed)
        else:
 # If does not find obstacle, go forward
 #
            fc.forward(speed)

# Call main function. If Ctrl+C is pressed, stop the car
#
if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
