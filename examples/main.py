import VirtualAssistant as va


if __name__ == '__main__':
    va.wishme()
    while True:
        query = va.takecommand()
        if 'wikipedia' in query:
            va.speakwikisummary()
        elif 'the time' in query:
            va.speaktime()
        elif 'the date' in query:
            va.speakdate()
        elif 'search google' in query:
            va.searchgoogle()
        elif 'take screenshot now' in query:
            va.takescreenshotnow(filename='blah',ext='jpg')
        elif 'take screenshot' in query:
            va.takescreenshot(_time=2,filename='yay',ext='png')
        elif 'open google' in query:
            va.opengoogle()
        elif 'open facebook' in query:
            va.openfacebook()
        elif 'open github' in query:
            va.opengithub()
        elif 'open youtube' in query:
            va.openyoutube()
        elif 'open stackoverflow' in query:
            va.openwebsite('https://www.stackoverflow.com')
        elif 'open whatsapp' in query:
            va.openwhatsappweb()
        elif 'open calculator' in query:
            va.opencalc()
        elif 'open file ' in query:
            va.openfile('C:\\Users\\Sony\\IdeaProjects\\VirtualAssistant\\examples\\yesnomo.png')
        elif 'open word' in query:
            va.openmsword()
        elif 'open code' in query:
            va.openvscode()
        elif 'play video on youtube' in query:
            va.playvidonyt()
        elif 'send email' in query:
            va.sendemail()
