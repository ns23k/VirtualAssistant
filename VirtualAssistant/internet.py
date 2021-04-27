import webbrowser
from .audioinout import speak,takecommand
import pywhatkit
import wikipedia
import smtplib
import requests


def speakweatherdata():
    api_key = 'ed5c7180267b2b9bef91544f9592ce45'
    speak("you want weather forcast for which city?")
    city = takecommand()
    if city == 'None':
        pass # i would fix bugs in 0.0.4
    json_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
    temp = int(json_data['main']['temp'] - 273.15)
    condition = json_data['weather'][0]['main']
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    sr = sunrise.split(":")
    ss = sunset.split(":")
    if '0' in sr:
        sr = sr.replace('0','')
    if '0' in ss:
        ss = ss.replace('0','')
    sunrise = f"{ss[0]} o clock {ss[1]} minuites {ss[2]} seconds"
    sunset = f"{sr[0]} o clock {sr[1]} minuites {sr[2]}seconds"
    speak(f"""the condition in {city} is {condition}, 
    the temprature is {temp} celsius,
    the minimum temperature is {min_temp} celsius,
    the maximum temperature is {max_temp} celsius,
    the pressure is {pressure},
    the humidity is {humidity} percent,
    the wind speed is {wind} kilometer per hour,
    the sunrise is at {sunrise},
    the sunset is at {sunset}.
          """)
   
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
    it will open web.whatsapp.com on your web browser
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



def searchgoogle():
    ''' it searches google for the query you gave to it '''
    speak('on which topic you wanna search google?')
    query = takecommand()
    speak(f'searching google for {query}')
    url = f'https://www.google.com/search?q={query}'
    webbrowser.open(url)


def playvidonyt():
    speak('please tell on which topic you want to see a video')
    topic = takecommand()
    speak(f'opening video on {topic}')
    pywhatkit.playonyt(topic)

def speakwikisummary(sentences=2):
    speak('what would you like to search on wikipedia?')
    thing = takecommand()
    summary = wikipedia.summary(thing,sentences=sentences)
    speak(summary)
    
def sendemail(email=None,password=None):
    # little buggy version
    # email = <youremail@gmail.com>
    # password = <youpass>
    #  if email is blah@gmail.com so just say blah the @gmail.com would be added automatically
    def remove(string):
        return "".join(string.split())
    if password is None:
        print(f'''{warning} please enter your password,password field can't be empty''')
    if email is None:
        print(f'''{warning} please enter your email,email field can't be empty''')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email,password)
    speak('to whom you wanna send the email?')
    emailaddress = takecommand()
    if '@gmail.com' not in emailaddress:
        emailaddress = emailaddress + '@gmail.com'
    emailaddress = remove(emailaddress)
    speak('what do you wanna say?')
    content = takecommand()
    speak(f'email would be sent to {emailaddress},the content in the mail would be {content}.Do you want me to send it?')
    print(f'email would be sent to {emailaddress},the content in the mail would be {content}.Do you want me to send it?')
    yesno = takecommand()
    if yesno == 'yes':
        try:
            server.sendmail(email,emailaddress,content)
            server.close()
            speak('email sent')
        except Exception as e:
            speak(f'''couldn't send mail to {emailaddress} ''')
            print(e)
    else:
        speak('Ok the email is canceled')
        server.close()
