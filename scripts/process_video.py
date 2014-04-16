#!/usr/bin/env python

import roslib; roslib.load_manifest('simple_navigation_goals')
import rospy
from sensor_msgs.msg import Image
#from cv_bridge import CvBridge, CvBridgeError
#from time import sleep
import time
import Image as image
import numpy, scipy


def array2image(data, img):
    pixels = img.load()
    for x in range(data.width):
        for y in range(data.height):
            index = y*data.step + x*3
            r = ord(data.data[index])
            g = ord(data.data[index + 1])
            b = ord(data.data[index + 2])
            pixels[x,y] = (r,g,b)
    return img

def process_frame(data):
    last_ok = 0   
    img = image.new('RGB', (data.width, data.height))
    img = array2image(data, img) 
    if (last_ok-time.time()) > 5:
        img = array2image(data, img) 
    cmd = raw_input("Enter yes   ")
    if cmd == 'yes':
        last_ok = time.time()
        img.show()
    time.sleep(1)
        
def main():
    rospy.init_node('process_image')
    rospy.Subscriber("camera/rgb/image_raw", Image, process_frame)
    print "Waiting for commands!"

    rospy.spin()
        
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass