from setuptools import setup

def readme():
    with open(r'README.md') as f:
        README = f.read()
    return README
# contributer = Devansh Sareen
setup(
    name='VirtualAssistant',
    version='0.0.3',
    packages=['VirtualAssistant'],
    install_requires=['pyttsx3','SpeechRecognition','colorama','pywhatkit'],
    url='https://github.com/Naman23-coder/VirtualAssistant',
    license='MIT',
    author='Naman Sharma',
    author_email = "namansharma232009@gmail.com",
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    description='VirtualAssistant is a python package that allows user to make simple Virtual Assistants with already defined commands with only one import.'
    
)


