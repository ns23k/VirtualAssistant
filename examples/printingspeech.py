# this is an example for VirtualAssistant python package which recognizes and prints the recognized speech,it is basically a speech to text
import VirtualAssistant as va

if __name__ == '__main__':
  while True:
    speech = va.takecommand()
    print(speech)
