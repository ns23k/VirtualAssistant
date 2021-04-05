import webbrowser
from .audioinout import speak


def opengoogle():
    '''
    it will open google.com on your web browser
    '''
    speak('opening google')
    webbrowser.open('https://www.google.com')



def openyoutube():
    '''
    it opens youtube on your web browser
    '''
    speak('opening youtube')
    webbrowser.open('https://www.youtube.com')



def openwhatsappweb():
    '''
    it will open web.whatsapp.con on your web browser
    '''
    speak('opening whatsapp web')
    webbrowser.open('https://web.whatsapp.com')



def openfacebook():
    '''
    it opens facebook.com on your web browser
    '''
    speak('opening facebook')
    webbrowser.open('https://www.facebook.com')



def openwebsite(url):
    '''it open the url user in form of a string in the default web browser
    using webbrowser module
    '''
    speak(f'opening {url}')
    webbrowser.open(url)



def opengithub():
    '''it opens the github.com website'''
    speak('opening github')
    webbrowser.open('https://www.github.com')



def searchgoogle(query):
    ''' it searches google for the query you gave to it '''
    speak('searching google')
    url = f'https://www.google.com/search?q={query}'
    webbrowser.open(url)
