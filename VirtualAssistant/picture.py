from PIL import ImageGrab
from .audioinout import speak,takecommand
import time
from .errors import error,timeerror

def takescreenshotnow(filename=None,ext=None):
    if filename is None:
        raise error('''the filename field can't be none''')
    if ext is None:
        raise error('''the filename ext can't be none''')
    image = ImageGrab.grab()
    image.show()
    speak('do you wanna save it?')
    yesno = takecommand()
    if yesno == 'None':
        speak('do you wanna save it?')
        yesno2 = takecommand()
        if yesno2 == 'None':
            speak('ok screenshot not saved')
        elif 'yes' in yesno2:
            try:
                image.save(f'{filename}.{ext}')
                speak('Screenshot saved')
            except  Exception as e:
                speak('''couldn't save screenshot''')
                print(e)
        else:
            speak('screenshot not saved')
    elif 'yes' in yesno:
        try:
            image.save(f'{filename}.{ext}')
            speak('Screenshot saved')
        except  Exception as e:
            speak('''couldn't save screenshot''')
            print(e)
    else:
         speak('screenshot not saved')

def takescreenshot(filename = None,_time = None,ext=None):
    if _time is None:
        raise timeerror('The _time field can not be None')
    else:
        time.sleep(_time)
        takescreenshotnow(filename=filename,ext=ext)
