from pulseSensor import PulseSensor
import time

p = PulseSensor()
p.startAsyncBPM()

try:
    while True:
        bpm = p.readBPM()
        if bpm > 0:
            print("BPM: %d" % bpm)
        else:
            print("No Heartbeat found")
        time.sleep(1)
except:
    p.stopAsyncBPM()
