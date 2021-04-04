'''this file would contain code that would fetch data and return it to user'''
# work in progress
import datetime
from .audioinout import speak

def speaktime(format= 'thour'):
    if format == 'thour':
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif  format == 'tfhour':
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
