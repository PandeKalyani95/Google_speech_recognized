import speech_recognition as sr

r1 = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak')
    audio = r1.listen(source)

    try:
        get = r1.recognize_google(audio)
        print(get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('Failed'.format(e))