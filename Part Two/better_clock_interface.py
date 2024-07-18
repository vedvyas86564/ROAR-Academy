## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_clock.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from datetime import datetime
import matplotlib.pyplot as plt
import os
import numpy as np
import time

# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/airplane.bmp'
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig, ax = plt.subplots()

while True:
    plt.gca().set_axis_off()
    plt.imshow(background)
    #retrieve gmt time
    gmt_time = time.gmtime()
    # First retrieve the time
    now_time = datetime.now()
    gmt_hour = gmt_time.tm_hour()
    if gmt_hour > 12: gmt_hour = gmt_hour-12
    hour = now_time.hour
    if hour>12: hour = hour - 12
    minute = now_time.minute
    second = now_time.second
    minute_angle = (minute + second / 60) / 60 * 2 * np.pi
    hour_angle = (hour + minute/60 + second/360) / 12 *2 * np.pi
    # Calculate end points of hour, minute, second
#they think its cool
    hour_vector = clock_hand_vector(hour_angle, hour_hand_length)
    minute_vector = clock_hand_vector(minute_angle, minute_hand_length)
    second_vector = clock_hand_vector(second/60*2*np.pi, second_hand_length)


    gmt_hour_vector = clock_hand_vector(hour_angle, hour_hand_length)
    gmt_minute_vector = clock_hand_vector(minute_angle, minute_hand_length)
    gmt_second_vector = clock_hand_vector(second/60*2*np.pi, second_hand_length)


    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'black')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth = minute_hand_width, color = 'black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth = second_hand_width, color = 'red')
    plt.arrow(center[0], center[1], gmt_hour_vector[0], gmt_hour_vector[1], linewidth= hour_hand_width, color='yellow')

    plt.pause(0.1) #if you dont pause your program will run faster than your screen can see it, the next update will come 
    ax.axis('off')
    plt.clf() #clears the previous plot
#trig malfunction
#short and long one
