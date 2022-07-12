#! /usr/bin/env python3

import datetime
import multiprocessing

from playsound import playsound
p = multiprocessing.Process(target=playsound, args=("audio/hl2-one-guard-down.mp3",))

set_time = input("set the time: \n")

while (str(datetime.datetime.now().strftime("%H:%M")) != set_time):
	print("waiting")

print("wake up")
p.start()
input("press Enter to stop playback")
p.terminate()
