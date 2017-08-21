import speech_recognition as sr
import string

def analize_it(result, template):
    res_len = len(result)
    tmp_len = len(template)
    result = result.lower()
    template = template.lower()
    if res_len == tmp_len:
        print "Lenght  is OK. Lenght = ", res_len
        tmp = template.split(' ')
        res = result.split(' ')
        word = 0
        while word < len(tmp):
            if res[word] == tmp[word]:
                print 'Word #', word + 1, 'is OK. Word = ', res[word]
            else:
                print 'Word #', word + 1, 'is bad. Word in result = ', res[word], ' Word should be "', tmp[word],'"'
            word += 1
    else:
        print 'Lenght is not OK.'

# obtain audio from the microphone
r = sr.Recognizer()
cout = 0
speaches = []
while cout < 7:
    with sr.Microphone(device_index=0) as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Sphinx
    try:
        print("You said :" + r.recognize_google(audio))
        speaches.append(str(r.recognize_google(audio)))
    except:
        cout-=1
        pass

    cout+=1


speach_result = [
    "what are you going to do after you graduate from high school",
    "i'm going to enter the university",
    "i'm going to go to college",
    "what university did you choose",
    "to get some information",
    "are you going to apply for financial aid",
    "although i don't think i qualify i still will apply"]

for index in range(len(speaches)):
    speaches[index] = str(speaches[index])
    speaches[index] =  speaches[index].lower()
    if speaches[index] == speach_result[index]:
        print "Index ", index, "is OK"
    else:
        print "Speach ", index, ' is bad. ', speaches[index], ' <> ', speach_result[index]
        analize_it(speaches[index],speach_result[index])
