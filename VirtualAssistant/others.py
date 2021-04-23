from .audioinout import speak
import sys
import time


def virtualassistquit(quit_time,assistname = None):
    if assistname == None:
        speak(f'assistant will quit in {quit_time}')
    else:
        speak(f"{assistname} will quit in {quit_time}")
    time.sleep(quit_time)
    quit()
    sys.exit()
